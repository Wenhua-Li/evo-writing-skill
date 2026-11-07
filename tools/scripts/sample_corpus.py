#!/usr/bin/env python3
"""Create a deterministic, stratified qualitative-review sample."""

from __future__ import annotations

import argparse
import csv
import json
import re
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ERAS = {
    "1997-2004": (1997, 2004, 38),
    "2005-2012": (2005, 2012, 38),
    "2013-2019": (2013, 2019, 37),
    "2020-2023": (2020, 2023, 37),
}
CONTRIBUTION_PRIORITY = [
    "survey", "theory", "benchmark_indicator", "application",
    "new_or_improved_algorithm", "operator_representation",
    "parameter_adaptation", "software_framework",
]
PROBLEM_PRIORITY = [
    "multiobjective", "constrained", "dynamic", "uncertain_robust",
    "expensive_surrogate", "large_scale", "multimodal", "combinatorial_discrete",
    "continuous_real", "bilevel", "multitask_transfer", "machine_learning_task",
    "real_world_application", "unlabeled",
]


def era_name(year: int) -> str:
    for name, (start, end, _quota) in ERAS.items():
        if start <= year <= end:
            return name
    return "unknown"


def first_label(labels: str, priority: list[str]) -> str:
    present = set(filter(None, labels.split(";")))
    for label in priority:
        if label in present:
            return label
    return "unlabeled"


def title_contribution(title: str) -> str:
    t = title.lower()
    if re.search(r"\b(survey|review|taxonomy)\b", t):
        return "survey"
    if re.search(r"\b(theoretical analysis|theory|runtime analysis|run time analysis|convergence analysis|markov chain|proof|no free lunch|stability)\b", t):
        return "theory"
    if re.search(r"\b(benchmark|test suite|test problems?|performance (?:metric|assessment|evaluation)|indicator|experimental comparison)\b", t):
        return "benchmark_indicator"
    if re.search(r"\b(application|real-world|design of|optimization of|scheduling|routing|forecast|classification|control)\b", t):
        return "application"
    if re.search(r"\b(operator|crossover|mutation|representation|encoding|selection)\b", t):
        return "operator_representation"
    if re.search(r"\b(parameter control|self-adaptive|adaptive parameter|parameter adaptation)\b", t):
        return "parameter_adaptation"
    return "new_or_improved_algorithm"


def choose_key(row: dict[str, str]) -> tuple[str, str]:
    contribution = title_contribution(row["title"])
    problem = first_label(row["problem_labels"], PROBLEM_PRIORITY)
    return contribution, problem


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    root = args.output_root.resolve()
    manifest_path = root / "build" / "private" / "manifest.csv"
    labels_path = root / "build" / "private" / "document-domains.csv"
    if not manifest_path.is_file() or not labels_path.is_file():
        raise SystemExit("Run build_corpus.py and classify_domains.py first.")

    manifest = {r["source_id"]: r for r in csv.DictReader(manifest_path.open(encoding="utf-8"))}
    candidates = [r for r in csv.DictReader(labels_path.open(encoding="utf-8")) if r["source_id"] in manifest]
    for row in candidates:
        m = manifest[row["source_id"]]
        row["sections"] = m["sections"]
        row["language_tokens"] = m["language_tokens"]
        row["quality_reasons"] = m["quality_reasons"]
    candidates = [r for r in candidates if r["quality_status"] == "usable"]

    selected: list[dict[str, str]] = []
    selected_ids: set[str] = set()
    for name, (start, end, quota) in ERAS.items():
        era_rows = [r for r in candidates if start <= int(r["year"]) <= end]
        if not era_rows:
            continue
        median_tokens = statistics.median(int(r["language_tokens"]) for r in era_rows)
        groups: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
        for row in era_rows:
            groups[choose_key(row)].append(row)
        for rows in groups.values():
            rows.sort(key=lambda r: (
                abs(int(r["language_tokens"]) - median_tokens),
                r["year"],
                r["source_id"],
            ))
        era_selected: list[dict[str, str]] = []

        def take_by_contribution(contribution: str, limit: int) -> None:
            if limit <= 0:
                return
            pools: dict[str, list[dict[str, str]]] = defaultdict(list)
            for row in era_rows:
                if row["source_id"] in selected_ids or title_contribution(row["title"]) != contribution:
                    continue
                problem = first_label(row["problem_labels"], PROBLEM_PRIORITY)
                pools[problem].append(row)
            for rows in pools.values():
                rows.sort(key=lambda r: (abs(int(r["language_tokens"]) - median_tokens), r["year"], r["source_id"]))
            taken = 0
            while taken < limit:
                progressed = False
                for problem in PROBLEM_PRIORITY:
                    rows = pools.get(problem, [])
                    if not rows:
                        continue
                    row = rows.pop(0)
                    selected_ids.add(row["source_id"])
                    row["sampled_contribution"] = contribution
                    era_selected.append(row)
                    taken += 1
                    progressed = True
                    if taken >= limit or len(era_selected) >= quota:
                        break
                if not progressed:
                    break

        targets = {
            "new_or_improved_algorithm": 12 if quota == 38 else 11,
            "application": 8,
            "benchmark_indicator": 6,
            "survey": 4,
            "theory": 4,
            "operator_representation": 3,
            "parameter_adaptation": 1,
        }
        for contribution, limit in targets.items():
            take_by_contribution(contribution, limit)

        groups: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
        for row in era_rows:
            if row["source_id"] not in selected_ids:
                groups[choose_key(row)].append(row)
        for rows in groups.values():
            rows.sort(key=lambda r: (
                abs(int(r["language_tokens"]) - median_tokens),
                r["year"],
                r["source_id"],
            ))
        while len(era_selected) < min(quota, len(era_rows)):
            progressed = False
            for key in sorted(groups):
                rows = groups[key]
                if rows and len(era_selected) < quota:
                    row = rows.pop(0)
                    selected_ids.add(row["source_id"])
                    era_selected.append(row)
                    progressed = True
            if not progressed:
                break
        for index, row in enumerate(era_selected):
            contribution, problem = choose_key(row)
            row["era"] = name
            row["sample_role"] = "calibration" if index < 10 else "core"
            row["primary_contribution"] = row.pop("sampled_contribution", contribution)
            row["primary_problem"] = problem
            row["selection_reason"] = "deterministic stratification by era, guaranteed contribution quotas, problem diversity, and median-length prose"
            selected.append(row)

    fields = [
        "source_id", "year", "era", "sample_role", "title", "primary_contribution", "primary_problem",
        "problem_labels", "method_labels", "contribution_labels", "selection_reason",
    ]
    private_path = root / "build" / "private" / "qualitative-sample.csv"
    with private_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(selected)

    summary_counts: Counter[tuple[str, str]] = Counter((r["era"], r["primary_contribution"]) for r in selected)
    summary_rows = [
        {"era": era, "primary_contribution": contribution, "documents": count}
        for (era, contribution), count in sorted(summary_counts.items())
    ]
    with (root / "data" / "sample-summary.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["era", "primary_contribution", "documents"])
        writer.writeheader()
        writer.writerows(summary_rows)

    print(json.dumps({
        "sample_documents": len(selected),
        "calibration": sum(r["sample_role"] == "calibration" for r in selected),
        "core": sum(r["sample_role"] == "core" for r in selected),
        "by_era": dict(Counter(r["era"] for r in selected)),
        "private_output": "build/private/qualitative-sample.csv",
        "public_output": "data/sample-summary.csv",
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
