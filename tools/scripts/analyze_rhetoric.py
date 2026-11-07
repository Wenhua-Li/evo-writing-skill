#!/usr/bin/env python3
"""Aggregate rhetorical-move evidence from abstracts, introductions, and conclusions.

The classifiers are transparent cue-based approximations used to prioritize manual
review; they are not presented as perfect discourse annotation.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

ABSTRACT_RULES = [
    ("result_evidence", r"\b(?:results?|experiments?|simulations?)\b.*\b(?:show|demonstrate|indicate|suggest|validate)\b|\bcompared (?:with|to)\b"),
    ("purpose_method", r"\b(?:this|the present) (?:paper|article|study)\b.*\b(?:propos|present|introduc|develop|investigat)|\bwe (?:propos|present|introduc|develop)\b"),
    ("problem_gap", r"\bhowever\b|\bbut\b|\balthough\b|\bremain|challeng|difficult|existing|most existing|lack|limitation"),
    ("background", r"\b(?:many|most|various|widely|increasingly|recent|recently|real-world|over the past|in recent years)\b"),
    ("scope_boundary", r"\boverall\b|\bin particular\b|\bspecifically\b|\bto this end\b|\bin this context\b"),
]
INTRO_RULES = [
    ("roadmap", r"\b(?:remainder|organized|organisation|organized as follows)\b"),
    ("contribution", r"\bcontributions?\b|\bmain (?:contributions|features)\b|\bwe (?:propos|present|introduc|develop)\b|\bthis (?:paper|article) (?:propos|present|introduc)\b"),
    ("gap", r"\bhowever\b|\bbut\b|\balthough\b|\blimitation|shortcoming|remain|challeng|difficult|little (?:research|attention)|not (?:been|well)"),
    ("literature", r"\b(?:existing|previous|related|recent|literature|survey|review|studies|methods|algorithms)\b"),
    ("context", r"\b(?:real-world|application|widely|increasingly|important|many|over the past|in recent years)\b"),
]
TITLE_PATTERNS = [
    ("colon", r":"),
    ("a_method_for", r"^a\b.*\bfor\b"),
    ("method_based", r"\bbased on\b|\busing\b|\bvia\b|\bwith\b"),
    ("toward", r"^toward\b"),
    ("review_or_survey", r"\b(?:survey|review|taxonomy)\b"),
    ("analysis_or_study", r"\b(?:analysis|study|investigation|evaluation)\b"),
]


def split_sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9(])", text) if len(s.split()) >= 4]


def label(text: str, rules: list[tuple[str, str]]) -> str:
    for name, pattern in rules:
        if re.search(pattern, text, flags=re.IGNORECASE):
            return name
    return "other"


def era(year: int) -> str:
    if year <= 2004:
        return "1997-2004"
    if year <= 2012:
        return "2005-2012"
    if year <= 2019:
        return "2013-2019"
    return "2020-2023"


def write(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
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
    corpus = [json.loads(x) for x in corpus_path.open(encoding="utf-8")]
    sections = {json.loads(x)["source_id"]: json.loads(x) for x in sections_path.open(encoding="utf-8")}

    abstract_moves: dict[str, Counter[str]] = defaultdict(Counter)
    abstract_sequences: Counter[str] = Counter()
    intro_position: dict[str, Counter[str]] = defaultdict(Counter)
    conclusion_moves: Counter[str] = Counter()
    title_rows: list[dict[str, object]] = []
    total = len(corpus)

    for doc in corpus:
        e = era(int(doc["year"]))
        sentences = split_sentences(str(doc.get("abstract", "")))
        labels = [label(s, ABSTRACT_RULES) for s in sentences]
        if labels:
            abstract_sequences[">".join(labels[:6])] += 1
            for i, move in enumerate(labels):
                position = "first" if i == 0 else ("last" if i == len(labels) - 1 else "middle")
                abstract_moves[e][f"{position}:{move}"] += 1
        intro = str(sections[doc["source_id"]]["sections"].get("introduction", ""))
        paragraphs = [p.strip() for p in intro.split("\n\n") if len(p.split()) >= 25]
        for i, p in enumerate(paragraphs[:8]):
            intro_position[e][f"p{i+1}:{label(p, INTRO_RULES)}"] += 1
        conclusion = str(sections[doc["source_id"]]["sections"].get("conclusion", ""))
        if conclusion:
            conclusion_moves[label(conclusion, INTRO_RULES)] += 1

    for name, pattern in TITLE_PATTERNS:
        count = sum(1 for d in corpus if re.search(pattern, str(d["title"]), flags=re.IGNORECASE))
        title_rows.append({"pattern": name, "documents": count, "share_pct": round(100 * count / total, 2)})

    move_rows = []
    for e in ("1997-2004", "2005-2012", "2013-2019", "2020-2023"):
        for key, count in abstract_moves[e].most_common():
            position, move = key.split(":", 1)
            move_rows.append({"era": e, "position": position, "move": move, "documents": count})
    write(root / "data" / "abstract-rhetorical-moves.csv", ["era", "position", "move", "documents"], move_rows)

    seq_rows = [{"sequence": seq, "documents": count} for seq, count in abstract_sequences.most_common(80)]
    write(root / "data" / "abstract-move-sequences.csv", ["sequence", "documents"], seq_rows)

    intro_rows = []
    for e in ("1997-2004", "2005-2012", "2013-2019", "2020-2023"):
        for key, count in intro_position[e].most_common():
            position, move = key.split(":", 1)
            intro_rows.append({"era": e, "paragraph_position": position, "move": move, "documents": count})
    write(root / "data" / "introduction-paragraph-moves.csv", ["era", "paragraph_position", "move", "documents"], intro_rows)
    write(root / "data" / "title-patterns.csv", ["pattern", "documents", "share_pct"], title_rows)

    print(json.dumps({
        "documents": total,
        "abstracts": sum(1 for d in corpus if d.get("abstract")),
        "outputs": [
            "data/abstract-rhetorical-moves.csv", "data/abstract-move-sequences.csv",
            "data/introduction-paragraph-moves.csv", "data/title-patterns.csv",
        ],
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
