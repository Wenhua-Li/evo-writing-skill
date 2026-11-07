#!/usr/bin/env python3
"""Build a quality-controlled, section-aware manifest from local TEVC Markdown files.

The raw corpus is never modified. Detailed section text is written only to the
ignored private build directory; public output is aggregate-only.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable

SECTION_ORDER = [
    "abstract",
    "introduction",
    "related_work",
    "preliminaries",
    "method",
    "theory",
    "experiments",
    "results",
    "discussion",
    "conclusion",
    "other",
]

TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9]*(?:[-'][A-Za-z0-9]+)*")
HEADING_RE = re.compile(r"^(#{2,6})\s+(.+?)\s*$")
DOI_RE = re.compile(r"10\.1109/TEVC\.\d{4}\.\d+", re.IGNORECASE)


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def default_corpus_root() -> Path:
    return repo_root().parent


def strip_markup(text: str) -> str:
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)
    text = re.sub(r"</?(?:em|strong|u|sup|sub|span|br)\b[^>]*>", " ", text, flags=re.IGNORECASE)
    text = text.replace("&nbsp;", " ").replace("&amp;", "&")
    text = re.sub(r"[*_]{1,3}", "", text)
    return re.sub(r"\s+", " ", text).strip()


def normalize_heading(title: str) -> str:
    title = strip_markup(title)
    title = re.sub(r"^[-–—\s]*(?:[IVXLCDM]+|[A-Z]|\d+)\s*[.)]?\s+", "", title, flags=re.IGNORECASE)
    return re.sub(r"\s+", " ", title).strip()


def categorize_heading(title: str) -> str:
    t = normalize_heading(title).lower()
    compact = re.sub(r"[^a-z0-9]+", " ", t)
    if re.search(r"\b(references?|bibliography)\b", compact):
        return "references"
    if re.search(r"\b(introduction|background and motivation)\b", compact):
        return "introduction"
    if re.search(r"\b(related work|literature review|prior work|previous work)\b", compact):
        return "related_work"
    if re.search(r"\b(preliminar|background|problem formulation|problem definition|basic concepts|notation|motivations?)\b", compact):
        return "preliminaries"
    if re.search(r"\b(conclusion|concluding remarks|summary and future|final remarks)\b", compact):
        return "conclusion"
    if re.search(r"\b(experiment|simulation|numerical|empirical|evaluation|performance study|comparative study|computational study)\b", compact):
        return "experiments"
    if re.search(r"\b(results?|findings?)\b", compact):
        return "results"
    if re.search(r"\b(discussion|limitations?|parameter analysis|sensitivity analysis)\b", compact):
        return "discussion"
    if re.search(r"\b(theor|proof|convergence analysis|runtime analysis|run time analysis|markov chain)\b", compact):
        return "theory"
    if re.search(r"\b(method|methodology|approach|algorithm|framework|model|design|proposed|implementation|operator|procedure|system)\b", compact):
        return "method"
    return "other"


def clean_heading_text(raw: str) -> str:
    return normalize_heading(raw)


def extract_title(lines: list[str], fallback: str) -> str:
    for line in lines[:40]:
        m = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if not m:
            continue
        title = strip_markup(m.group(1))
        # Some converted PDFs expose a decorative drop capital as a heading.
        if len(title) >= 8 and not title.isupper():
            return title
    return fallback


def extract_labeled_block(lines: list[str], label: str) -> str:
    start = -1
    for i, line in enumerate(lines[:120]):
        plain = strip_markup(line)
        if re.search(rf"\b{re.escape(label)}\b", plain, re.IGNORECASE):
            start = i
            break
    if start < 0:
        return ""
    parts = [lines[start]]
    for j in range(start + 1, min(len(lines), start + 12)):
        plain = strip_markup(lines[j])
        if HEADING_RE.match(lines[j]):
            break
        if label.lower() == "abstract" and re.search(r"\bIndex Terms\b", plain, re.IGNORECASE):
            break
        if label.lower() == "index terms" and (not plain or re.search(r"\b(?:I\.|1\.)\s+INTRODUCTION\b", plain, re.IGNORECASE)):
            break
        parts.append(lines[j])
    text = strip_markup("\n".join(parts))
    text = re.sub(rf"^{label}\s*[—\-:]?\s*", "", text, flags=re.IGNORECASE)
    if label.lower() == "index terms":
        text = re.sub(r"^Index Terms\s*[—\-:]?\s*", "", text, flags=re.IGNORECASE)
    return text.strip(" —-")


def is_caption_or_metadata(line: str) -> bool:
    s = strip_markup(line)
    if not s:
        return True
    if re.match(r"^(?:Fig(?:ure)?\.?|TABLE|Table|ALGORITHM|Algorithm)\s*[-:\w(]?", s):
        return True
    if DOI_RE.search(s) or "Digital Object Identifier" in s or "Color versions of" in s:
        return True
    if re.search(r"@(?:[A-Za-z0-9.-]+)", s) and len(s) < 220:
        return True
    if re.match(r"^\d{3,4}[–-]\d{3,4}/\d{2}\$", s):
        return True
    if re.match(r"^[A-Z¨´’' .&-]{2,80}\s+et al\.\s*:", s):
        return True
    if re.match(r"^\|?[-:| ]+\|?$", s):
        return True
    if re.match(r"^\(?[ivxlcdmIVXLCDM0-9]{1,6}\)?$", s):
        return True
    return False


def prose_candidate(line: str) -> str:
    if is_caption_or_metadata(line):
        return ""
    s = strip_markup(line)
    if s.startswith(">"):
        return ""
    # Remove lines that are mostly punctuation or mathematical debris.
    alnum = sum(ch.isalnum() for ch in s)
    if len(s) > 0 and alnum / len(s) < 0.25:
        return ""
    # Remove isolated table/rule fragments while retaining ordinary prose.
    if len(s) < 4 and not re.search(r"[a-zA-Z]", s):
        return ""
    return s


def split_sections(lines: list[str]) -> tuple[dict[str, str], list[dict[str, object]], list[str]]:
    sections: dict[str, list[str]] = defaultdict(list)
    headings: list[dict[str, object]] = []
    captions: list[str] = []
    current: str | None = None
    in_picture = False
    stopped = False

    for raw in lines:
        if "Start of picture text" in raw:
            in_picture = True
            continue
        if "End of picture text" in raw:
            in_picture = False
            continue
        if in_picture:
            continue

        plain = strip_markup(raw)
        if re.match(r"^(?:Fig(?:ure)?\.?|TABLE|Table)\s*[-:\w(]?", plain):
            if plain:
                captions.append(plain)
            continue

        hm = HEADING_RE.match(raw)
        if hm:
            title = clean_heading_text(hm.group(2))
            category = categorize_heading(title)
            headings.append({"level": len(hm.group(1)), "title": title, "category": category})
            if category == "references":
                stopped = True
                current = None
                break
            current = category
            continue
        if stopped:
            continue
        if current is None:
            continue
        candidate = prose_candidate(raw)
        if candidate:
            sections[current].append(candidate)

    return ({k: "\n\n".join(v) for k, v in sections.items() if v}, headings, captions)


def issue_from_name(name: str) -> str:
    m = re.match(r"\d{4}_i(\d+)_", name)
    return m.group(1) if m else ""


def slug_from_name(name: str) -> str:
    stem = Path(name).stem
    stem = re.sub(r"^\d{4}_i\d+_?", "", stem)
    stem = re.sub(r"_[0-9a-f]{8}$", "", stem)
    return re.sub(r"[^A-Za-z0-9]+", "-", stem).strip("-").lower()[:80]


def quality_metrics(text: str) -> dict[str, object]:
    tokens = TOKEN_RE.findall(text)
    replacement = text.count("\ufffd")
    very_long = sum(1 for t in tokens if len(t) > 28)
    weird = sum(1 for ch in text if ord(ch) > 1000)
    denominator = max(1, len(tokens))
    return {
        "tokens": len(tokens),
        "replacement_chars": replacement,
        "very_long_tokens": very_long,
        "high_unicode_chars": weird,
        "noise_score": round((replacement * 10 + very_long * 2 + weird) / denominator, 6),
    }


def iter_corpus_files(corpus_root: Path, cutoff: int) -> Iterable[Path]:
    for year in range(1997, cutoff + 1):
        directory = corpus_root / str(year)
        if not directory.is_dir():
            continue
        yield from sorted(directory.glob("*.md"))


def process_file(path: Path, corpus_root: Path) -> tuple[dict[str, object], dict[str, object], dict[str, object]]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    lines = raw.splitlines()
    title = extract_title(lines, path.stem)
    abstract = extract_labeled_block(lines, "abstract")
    keywords = extract_labeled_block(lines, "index terms")
    sections, headings, captions = split_sections(lines)
    prose = "\n\n".join(sections.get(k, "") for k in SECTION_ORDER if k in sections)
    metrics = quality_metrics(prose)
    doi_match = DOI_RE.search(raw)

    present = set(sections)
    reasons: list[str] = []
    if not abstract:
        reasons.append("missing_abstract")
    if "introduction" not in present:
        reasons.append("missing_introduction")
    if "conclusion" not in present:
        reasons.append("missing_conclusion")
    if metrics["tokens"] < 500:
        reasons.append("short_body")
    if float(metrics["noise_score"]) > 0.08:
        reasons.append("high_ocr_noise")

    if "short_body" in reasons:
        status = "metadata_only"
    elif "high_ocr_noise" in reasons:
        status = "review"
    else:
        status = "usable"
    year = int(path.parent.name)
    source_id = f"{year}-i{issue_from_name(path.name) or 'x'}-{slug_from_name(path.name)}"

    document = {
        "source_id": source_id,
        "year": year,
        "issue": issue_from_name(path.name),
        "title": title,
        "relative_path": path.relative_to(corpus_root).as_posix(),
        "doi": doi_match.group(0) if doi_match else "",
        "abstract": abstract,
        "keywords": keywords,
        "headings": headings,
        "captions": captions,
        "section_categories": [k for k in SECTION_ORDER if k in present],
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "quality": metrics,
        "quality_status": status,
        "quality_reasons": reasons,
    }
    section_record = {
        "source_id": source_id,
        "year": year,
        "title": title,
        "quality_status": status,
        "sections": sections,
    }
    manifest_row = {
        "source_id": source_id,
        "year": year,
        "issue": issue_from_name(path.name),
        "title": title,
        "relative_path": path.relative_to(corpus_root).as_posix(),
        "doi": document["doi"],
        "bytes": path.stat().st_size,
        "sha256": document["sha256"],
        "sections": ";".join(document["section_categories"]),
        "language_tokens": metrics["tokens"],
        "quality_status": status,
        "quality_reasons": ";".join(reasons),
    }
    return document, section_record, manifest_row


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(path.open("w", encoding="utf-8", newline=""), fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus-root", type=Path, default=default_corpus_root())
    parser.add_argument("--output-root", type=Path, default=repo_root())
    parser.add_argument("--cutoff", type=int, default=2023)
    args = parser.parse_args(argv)

    if args.cutoff > 2023:
        raise SystemExit("This evidence build intentionally refuses a cutoff after 2023.")

    corpus_root = args.corpus_root.resolve()
    output_root = args.output_root.resolve()
    private_dir = output_root / "build" / "private"
    public_data = output_root / "data"
    private_dir.mkdir(parents=True, exist_ok=True)
    public_data.mkdir(parents=True, exist_ok=True)

    files = list(iter_corpus_files(corpus_root, args.cutoff))
    if not files:
        raise SystemExit(f"No Markdown files found under {corpus_root} for 1997–{args.cutoff}.")

    documents: list[dict[str, object]] = []
    section_records: list[dict[str, object]] = []
    manifest_rows: list[dict[str, object]] = []
    per_year: dict[int, Counter[str]] = defaultdict(Counter)

    for path in files:
        document, section_record, manifest_row = process_file(path, corpus_root)
        documents.append(document)
        section_records.append(section_record)
        manifest_rows.append(manifest_row)
        year = int(document["year"])
        per_year[year]["files"] += 1
        per_year[year]["language_tokens"] += int(document["quality"]["tokens"])
        per_year[year][str(document["quality_status"])] += 1

    with (private_dir / "corpus.jsonl").open("w", encoding="utf-8") as fh:
        for row in documents:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    with (private_dir / "sections.jsonl").open("w", encoding="utf-8") as fh:
        for row in section_records:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")

    manifest_fields = [
        "source_id", "year", "issue", "title", "relative_path", "doi", "bytes", "sha256",
        "sections", "language_tokens", "quality_status", "quality_reasons",
    ]
    with (private_dir / "manifest.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=manifest_fields)
        writer.writeheader()
        writer.writerows(manifest_rows)

    overview_rows = []
    for year in sorted(per_year):
        counts = per_year[year]
        overview_rows.append({
            "year": year,
            "files": counts["files"],
            "usable": counts["usable"],
            "review": counts["review"],
            "metadata_only": counts["metadata_only"],
            "language_tokens": counts["language_tokens"],
        })
    with (public_data / "corpus-overview.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["year", "files", "usable", "review", "metadata_only", "language_tokens"])
        writer.writeheader()
        writer.writerows(overview_rows)

    status_counts = Counter(str(row["quality_status"]) for row in manifest_rows)
    summary = {
        "corpus_root": str(corpus_root),
        "cutoff": args.cutoff,
        "files": len(files),
        "status_counts": dict(status_counts),
        "language_tokens": sum(int(row["language_tokens"]) for row in manifest_rows),
        "years": [min(per_year), max(per_year)] if per_year else [],
        "private_outputs": ["build/private/corpus.jsonl", "build/private/sections.jsonl", "build/private/manifest.csv"],
        "public_outputs": ["data/corpus-overview.csv"],
    }
    (private_dir / "build-summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
