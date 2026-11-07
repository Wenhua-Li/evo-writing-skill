#!/usr/bin/env python3
"""Assign auditable multi-axis candidate labels to TEVC documents.

Labels are dictionary-assisted candidates, not a substitute for expert judgment.
Public output is aggregate-only; document-level labels remain in build/private.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

AXES: dict[str, dict[str, list[str]]] = {
    "problem": {
        "multiobjective": [r"\bmulti[- ]objective\b", r"\bmany[- ]objective\b", r"\bpareto\b", r"\bmoea\b", r"\bemoa\b"],
        "many_objective": [r"\bmany[- ]objective\b", r"\bmaop\b", r"\bmaoea\b"],
        "constrained": [r"\bconstrain(?:t|ed|ts)\b", r"\bconstraint handling\b", r"\bfeasib"],
        "dynamic": [r"\bdynamic\b", r"\bnon[- ]stationary\b", r"\btime[- ]varying\b", r"\bchanging environment"],
        "uncertain_robust": [r"\buncertain", r"\bnoise\b", r"\bnoisy\b", r"\brobust\b"],
        "expensive_surrogate": [r"\bexpensive\b", r"\bsurrogate", r"\bmetamodel", r"\bdata[- ]driven\b"],
        "large_scale": [r"\blarge[- ]scale\b", r"\bhigh[- ]dimensional\b", r"\bscalab"],
        "multimodal": [r"\bmultimodal\b", r"\bnich", r"\bspeciation\b"],
        "combinatorial_discrete": [r"\bcombinatorial\b", r"\bdiscrete\b", r"\bschedul", r"\brouting\b", r"\bspanning tree\b", r"\bknapsack\b"],
        "continuous_real": [r"\bcontinuous\b", r"\breal[- ]parameter\b", r"\breal[- ]coded\b", r"\bnumerical optimization\b"],
        "bilevel": [r"\bbi[- ]level\b", r"\bblevel\b"],
        "multitask_transfer": [r"\bmultitask", r"\bmulti[- ]task", r"\btransfer\b", r"\bmulti[- ]form"],
        "machine_learning_task": [r"\bclassification\b", r"\bfeature selection\b", r"\bclustering\b", r"\bneural network", r"\bimage\b", r"\bdata mining\b"],
        "real_world_application": [r"\breal[- ]world\b", r"\bapplication\b", r"\bindustrial\b", r"\bengineering\b", r"\bpower\b", r"\bmedical\b"],
    },
    "method": {
        "genetic_algorithm": [r"\bgenetic algorithms?\b", r"\bga\b"],
        "differential_evolution": [r"\bdifferential evolution\b", r"\bde[-/]", r"\bde\b"],
        "evolution_strategy": [r"\bevolution strateg", r"\bes\b", r"\bcma[- ]es\b"],
        "evolutionary_programming": [r"\bevolutionary programming\b", r"\bep\b"],
        "genetic_programming": [r"\bgenetic programming\b", r"\bgp\b"],
        "learning_classifier": [r"\blearning classifier", r"\bxcs\b", r"\blcs\b"],
        "swarm_intelligence": [r"\bparticle swarm\b", r"\bpso\b", r"\bswarm intelligence\b"],
        "ant_colony": [r"\bant colon", r"\baco\b"],
        "estimation_distribution": [r"\bestimation of distribution", r"\beda\b", r"\bmodel[- ]based\b"],
        "memetic_local_search": [r"\bmemetic\b", r"\blocal search\b", r"\bhybrid"],
        "coevolution": [r"\bcoevolution", r"\bco[- ]evolution"],
        "artificial_immune": [r"\bartificial immune\b", r"\bimmune algorithm", r"\bimmune clonal"],
        "neuroevolution": [r"\bneuroevolution\b", r"\bevolv(?:e|ing|ed) neural\b", r"\bneural architecture search\b"],
        "machine_learning_hybrid": [r"\bmachine learning\b", r"\bneural network", r"\bdeep\b", r"\breinforcement learning\b", r"\blearning[- ](?:based|to)\b"],
    },
    "contribution": {
        "new_or_improved_algorithm": [r"\bpropos", r"\bpresent", r"\bintroduc", r"\balgorithm\b", r"\bframework\b", r"\boptimizer\b"],
        "theory": [r"\btheor", r"\bproof\b", r"\bconvergence analysis\b", r"\bruntime analysis\b", r"\brun[- ]time analysis\b", r"\bmarkov\b"],
        "benchmark_indicator": [r"\bbenchmark", r"\btest (?:problem|function|suite|instance)", r"\bindicator\b", r"\bmetric\b", r"\bperformance assessment\b"],
        "survey": [r"\bsurvey\b", r"\breview\b", r"\btaxonomy\b", r"\bstate[- ]of[- ]the[- ]art\b"],
        "application": [r"\bapplication\b", r"\breal[- ]world\b", r"\bdesign of\b", r"\boptimization of\b", r"\bindustrial\b"],
        "operator_representation": [r"\boperator", r"\brepresentation\b", r"\bencoding\b", r"\bvariation\b", r"\bcrossover\b", r"\bmutation\b"],
        "parameter_adaptation": [r"\bparameter control\b", r"\bself[- ]adaptive\b", r"\badaptive\b", r"\bparameter tuning\b"],
        "software_framework": [r"\bplatform\b", r"\bsoftware\b", r"\btool\b", r"\bframework\b"],
    },
}


def norm_text(document: dict[str, object]) -> str:
    text = " ".join(str(document.get(k, "")) for k in ("title", "keywords", "abstract"))
    text = text.lower().replace("_", " ")
    text = re.sub(r"[\u2010-\u2015]", "-", text)
    return text


def matches(text: str, pattern: str) -> bool:
    return re.search(pattern, text, flags=re.IGNORECASE) is not None


def era(year: int) -> str:
    if year <= 2004:
        return "1997-2004"
    if year <= 2012:
        return "2005-2012"
    if year <= 2019:
        return "2013-2019"
    return "2020-2023"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    root = args.output_root.resolve()
    corpus_path = root / "build" / "private" / "corpus.jsonl"
    if not corpus_path.is_file():
        raise SystemExit("Run scripts/build_corpus.py first.")

    documents = [json.loads(line) for line in corpus_path.open(encoding="utf-8")]
    private_rows: list[dict[str, object]] = []
    axis_counts: dict[str, Counter[str]] = {axis: Counter() for axis in AXES}
    era_counts: dict[tuple[str, str], Counter[str]] = defaultdict(Counter)
    unlabeled = Counter()

    for doc in documents:
        text = norm_text(doc)
        labels_by_axis: dict[str, list[str]] = {}
        for axis, labels in AXES.items():
            found = [label for label, patterns in labels.items() if any(matches(text, p) for p in patterns)]
            labels_by_axis[axis] = found
            for label in found:
                axis_counts[axis][label] += 1
                era_counts[(axis, era(int(doc["year"])))][label] += 1
        if not labels_by_axis["problem"]:
            unlabeled["problem"] += 1
        if not labels_by_axis["method"]:
            unlabeled["method"] += 1
        if not labels_by_axis["contribution"]:
            unlabeled["contribution"] += 1
        private_rows.append({
            "source_id": doc["source_id"],
            "year": doc["year"],
            "title": doc["title"],
            "problem_labels": ";".join(labels_by_axis["problem"]),
            "method_labels": ";".join(labels_by_axis["method"]),
            "contribution_labels": ";".join(labels_by_axis["contribution"]),
            "quality_status": doc["quality_status"],
        })

    private_path = root / "build" / "private" / "document-domains.csv"
    private_rows.sort(key=lambda r: (int(r["year"]), str(r["source_id"])))
    with private_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(private_rows[0]))
        writer.writeheader()
        writer.writerows(private_rows)

    public_rows: list[dict[str, object]] = []
    for axis in AXES:
        for era_name in ("1997-2004", "2005-2012", "2013-2019", "2020-2023"):
            counts = era_counts.get((axis, era_name), Counter())
            for label, count in sorted(counts.items()):
                public_rows.append({"axis": axis, "era": era_name, "label": label, "documents": count})
        for label, count in sorted(axis_counts[axis].items()):
            public_rows.append({"axis": axis, "era": "all", "label": label, "documents": count})
        public_rows.append({"axis": axis, "era": "all", "label": "unlabeled", "documents": unlabeled[axis]})

    data_path = root / "data" / "domain-summary.csv"
    with data_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["axis", "era", "label", "documents"])
        writer.writeheader()
        writer.writerows(public_rows)

    print(json.dumps({
        "documents": len(documents),
        "unlabeled": dict(unlabeled),
        "output": str(data_path.relative_to(root)),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
