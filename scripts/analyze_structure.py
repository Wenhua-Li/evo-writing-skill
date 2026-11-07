#!/usr/bin/env python3
"""Summarize section coverage, heading conventions, and article-level organization."""

from __future__ import annotations

import argparse
import csv
import json
import re
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9]*(?:[-'][A-Za-z0-9]+)*")
MAIN_CATEGORIES = [
    "introduction", "related_work", "preliminaries", "method", "theory",
    "experiments", "results", "discussion", "conclusion", "other",
]


def era(year: int) -> str:
    if year <= 2004:
        return "1997-2004"
    if year <= 2012:
        return "2005-2012"
    if year <= 2019:
        return "2013-2019"
    return "2020-2023"


def sentence_count(text: str) -> int:
    pieces = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9(])", text.strip())
    return sum(1 for p in pieces if len(TOKEN_RE.findall(p)) >= 3)


def median_int(values: list[int]) -> int:
    return int(statistics.median(values)) if values else 0


def write_rows(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    root = args.output_root.resolve()
    corpus_path = root / "build" / "private" / "corpus.jsonl"
    sections_path = root / "build" / "private" / "sections.jsonl"
    if not corpus_path.is_file() or not sections_path.is_file():
        raise SystemExit("Run scripts/build_corpus.py first.")

    documents = [json.loads(line) for line in corpus_path.open(encoding="utf-8")]
    sections = [json.loads(line) for line in sections_path.open(encoding="utf-8")]
    section_by_id = {row["source_id"]: row for row in sections}

    category_stats: dict[str, dict[str, object]] = {
        c: {"docs": 0, "tokens": [], "prev": Counter(), "next": Counter(), "years": []}
        for c in ["abstract", *MAIN_CATEGORIES]
    }
    sequences: Counter[str] = Counter()
    heading_counts: Counter[str] = Counter()
    heading_docs: dict[str, set[str]] = defaultdict(set)
    heading_years: dict[str, list[int]] = defaultdict(list)
    coverage_by_era: dict[str, Counter[str]] = defaultdict(Counter)
    era_docs: Counter[str] = Counter()
    abstract_by_era: dict[str, dict[str, list[int]]] = defaultdict(lambda: {"sentences": [], "words": []})

    for doc in documents:
        source_id = str(doc["source_id"])
        year = int(doc["year"])
        era_name = era(year)
        era_docs[era_name] += 1
        heading_records = doc.get("headings", [])
        first_categories: list[str] = []
        previous = "front_matter"
        for h in heading_records:
            title = str(h.get("title", "")).strip().lower()
            category = str(h.get("category", "other"))
            if title:
                heading_counts[title] += 1
                heading_docs[title].add(source_id)
                heading_years[title].append(year)
            if category not in category_stats:
                continue
            if category not in first_categories:
                first_categories.append(category)
                stats = category_stats[category]
                stats["prev"][previous] += 1
                previous = category
        if first_categories:
            category_stats[first_categories[-1]]["next"]["end"] += 1
        for i, category in enumerate(first_categories[:-1]):
            category_stats[category]["next"][first_categories[i + 1]] += 1
        compact_sequence = [c for c in first_categories if c != "other"]
        if compact_sequence:
            sequences[" > ".join(compact_sequence)] += 1

        sec = section_by_id[source_id]["sections"]
        for category, text in sec.items():
            stats = category_stats[category]
            stats["docs"] += 1
            stats["tokens"].append(len(TOKEN_RE.findall(str(text))))
            stats["years"].append(year)
            coverage_by_era[era_name][category] += 1

        abstract = str(doc.get("abstract", ""))
        if abstract:
            category_stats["abstract"]["docs"] += 1
            words = TOKEN_RE.findall(abstract)
            category_stats["abstract"]["tokens"].append(len(words))
            category_stats["abstract"]["years"].append(year)
            abstract_by_era[era_name]["sentences"].append(sentence_count(abstract))
            abstract_by_era[era_name]["words"].append(len(words))

    pattern_rows: list[dict[str, object]] = []
    total = len(documents)
    for category in ["abstract", *MAIN_CATEGORIES]:
        stats = category_stats[category]
        docs = int(stats["docs"])
        tokens = stats["tokens"]
        years = stats["years"]
        prev = stats["prev"].most_common(1)[0][0] if stats["prev"] else ""
        nxt = stats["next"].most_common(1)[0][0] if stats["next"] else ""
        pattern_rows.append({
            "section": category,
            "documents": docs,
            "coverage_pct": round(100 * docs / total, 2),
            "median_tokens": median_int(tokens),
            "first_year": min(years) if years else "",
            "last_year": max(years) if years else "",
            "common_previous": prev,
            "common_next": nxt,
        })
    write_rows(root / "data" / "section-patterns.csv", list(pattern_rows[0]), pattern_rows)

    sequence_rows = [
        {"sequence": seq, "documents": count, "share_pct": round(100 * count / total, 2)}
        for seq, count in sequences.most_common(100)
    ]
    write_rows(root / "data" / "section-sequences.csv", ["sequence", "documents", "share_pct"], sequence_rows)

    heading_rows = []
    for title, count in heading_counts.most_common(300):
        years = heading_years[title]
        heading_rows.append({
            "normalized_heading": title,
            "occurrences": count,
            "documents": len(heading_docs[title]),
            "first_year": min(years),
            "last_year": max(years),
        })
    write_rows(root / "data" / "section-heading-frequency.csv", list(heading_rows[0]), heading_rows)

    coverage_rows = []
    for era_name in ("1997-2004", "2005-2012", "2013-2019", "2020-2023"):
        n = era_docs[era_name]
        for category in ["abstract", *MAIN_CATEGORIES]:
            count = coverage_by_era[era_name][category]
            coverage_rows.append({
                "era": era_name,
                "section": category,
                "documents": count,
                "coverage_pct": round(100 * count / n, 2) if n else 0,
            })
    write_rows(root / "data" / "section-coverage-by-era.csv", list(coverage_rows[0]), coverage_rows)

    abstract_rows = []
    for era_name in ("1997-2004", "2005-2012", "2013-2019", "2020-2023"):
        vals = abstract_by_era[era_name]
        abstract_rows.append({
            "era": era_name,
            "documents": len(vals["words"]),
            "median_words": median_int(vals["words"]),
            "median_sentences": median_int(vals["sentences"]),
        })
    write_rows(root / "data" / "abstract-stats-by-era.csv", list(abstract_rows[0]), abstract_rows)

    print(json.dumps({
        "documents": total,
        "abstracts": int(category_stats["abstract"]["docs"]),
        "introduction_sections": int(category_stats["introduction"]["docs"]),
        "conclusion_sections": int(category_stats["conclusion"]["docs"]),
        "outputs": ["data/section-patterns.csv", "data/section-sequences.csv", "data/section-heading-frequency.csv"],
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
