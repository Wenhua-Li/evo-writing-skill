#!/usr/bin/env python3
"""Compute section-aware lexical, collocation, terminology, and rhetorical summaries."""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9]*(?:[-'][A-Za-z0-9]+)*")

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "been", "by", "can", "could", "do", "does",
    "for", "from", "had", "has", "have", "he", "her", "his", "i", "if", "in", "into", "is",
    "it", "its", "may", "might", "must", "no", "not", "of", "on", "or", "our", "she", "so",
    "such", "that", "the", "their", "them", "then", "there", "these", "they", "this", "those",
    "to", "was", "we", "were", "when", "where", "which", "while", "who", "will", "with", "would",
    "also", "however", "thus", "therefore", "moreover", "furthermore", "respectively", "using",
    "used", "use", "based", "via", "between", "among", "within", "without", "each", "all", "any",
    "one", "two", "three", "first", "second", "third", "new", "proposed", "paper", "section",
    "other", "more", "most", "much", "many", "than", "but", "only", "some", "both", "same",
    "different", "well", "very", "further", "through", "over", "given", "existing", "another",
    "addition", "case", "order", "way", "found", "shown", "show", "shows", "should", "being",
    "due", "rather", "either", "whether", "although", "since", "while", "per", "et", "al",
    "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "xi", "xii", "xiii", "xiv", "xv", "xvi",
}

TERMS: dict[str, str] = {
    "evolutionary algorithm": r"\bevolutionary algorithms?\b|\beas?\b",
    "evolutionary computation": r"\bevolutionary computation\b|\bec\b",
    "genetic algorithm": r"\bgenetic algorithms?\b|\bgas?\b",
    "differential evolution": r"\bdifferential evolution\b|\bde\b",
    "evolution strategy": r"\bevolution strategies\b|\bevolution strategy\b|\bess?\b",
    "evolutionary programming": r"\bevolutionary programming\b|\bep\b",
    "genetic programming": r"\bgenetic programming\b|\bgp\b",
    "particle swarm optimization": r"\bparticle swarm optimization\b|\bpso\b",
    "ant colony optimization": r"\bant colony optimization\b|\baco\b",
    "estimation of distribution algorithm": r"\bestimation of distribution algorithms?\b|\bedas?\b",
    "multiobjective optimization": r"\bmulti[- ]objective optimization\b|\bmoo\b",
    "many-objective optimization": r"\bmany[- ]objective optimization\b|\bmaop\b",
    "multiobjective evolutionary algorithm": r"\bmulti[- ]objective evolutionary algorithms?\b|\bmoeas?\b",
    "Pareto front": r"\bpareto[- ](?:optimal )?front\b|\bpf\b",
    "Pareto optimal set": r"\bpareto[- ]optimal set\b|\bps\b",
    "nondominated sorting": r"\bnondominated sorting\b",
    "constraint handling": r"\bconstraint[- ]handling\b|\bconstraint handling\b",
    "surrogate-assisted": r"\bsurrogate[- ]assisted\b|\bsurrogate model",
    "large-scale optimization": r"\blarge[- ]scale (?:global )?optimization\b|\blsgo\b",
    "dynamic optimization": r"\bdynamic optimization\b|\bdynamic environment",
    "multimodal optimization": r"\bmultimodal optimization\b",
    "hypervolume": r"\bhypervolume\b|\bhv\b",
    "inverted generational distance": r"\binverted generational distance\b|\bigd\b",
    "function evaluations": r"\bfunction evaluations?\b|\bfitness evaluations?\b|\bfes\b",
    "population size": r"\bpopulation size\b",
    "selection operator": r"\bselection operators?\b",
    "crossover operator": r"\bcrossover operators?\b|\brecombination operators?\b",
    "mutation operator": r"\bmutation operators?\b",
    "convergence": r"\bconvergence\b|\bconverge(?:d|s|nce)?\b",
    "diversity": r"\bdiversity\b|\bdiverse\b",
    "robustness": r"\brobustness\b|\brobust\b",
    "scalability": r"\bscalability\b|\bscalable\b",
    "benchmark problem": r"\bbenchmark (?:problems?|functions?|instances?)\b|\btest (?:problems?|functions?|instances?)\b",
    "statistical test": r"\bstatistical tests?\b|\bwilcoxon\b|\bfriedman\b|\bsignificance\b",
    "ablation study": r"\bablation (?:study|studies|experiment)",
    "time complexity": r"\btime complexity\b|\bcomputational complexity\b",
}

RHETORICAL: dict[str, str] = {
    "in this paper": r"\bin this (?:paper|article)\b",
    "we propose": r"\bwe propos(?:e|ed)\b",
    "we present": r"\bwe present(?:ed)?\b",
    "experimental results show": r"\bexperimental results (?:show|demonstrate|indicate)\b",
    "compared with": r"\bcompared with\b|\bin comparison with\b",
    "to the best of our knowledge": r"\bto the best of our knowledge\b",
    "the remainder of this paper": r"\bthe remainder of this (?:paper|article)\b",
    "without loss of generality": r"\bwithout loss of generality\b",
    "it should be noted": r"\bit should be noted\b",
    "as can be seen": r"\bas can be seen\b",
    "future work": r"\bfuture (?:work|research)\b",
    "significantly outperforms": r"\bsignificantly outperform\w*\b",
    "state-of-the-art": r"\bstate[- ]of[- ]the[- ]art\b",
}


def era(year: int) -> str:
    if year <= 2004:
        return "1997-2004"
    if year <= 2012:
        return "2005-2012"
    if year <= 2019:
        return "2013-2019"
    return "2020-2023"


def tokens(text: str) -> list[str]:
    return [t.lower() for t in TOKEN_RE.findall(text)]


def valid_token(token: str) -> bool:
    return 2 <= len(token) <= 30 and token not in STOPWORDS and not token.isdigit()


def ngram_is_useful(parts: tuple[str, ...]) -> bool:
    if any(not (1 <= len(t) <= 30) or t.isdigit() for t in parts):
        return False
    content = sum(t not in STOPWORDS for t in parts)
    if len(parts) == 2:
        return content >= 1
    return content >= max(2, math.ceil(len(parts) * 0.45))


def write_rows(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def phrase_counts(pattern: str, text: str) -> int:
    return len(re.findall(pattern, text, flags=re.IGNORECASE))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", type=Path, default=ROOT)
    parser.add_argument("--min-documents", type=int, default=5)
    args = parser.parse_args(argv)
    root = args.output_root.resolve()
    sections_path = root / "build" / "private" / "sections.jsonl"
    if not sections_path.is_file():
        raise SystemExit("Run scripts/build_corpus.py first.")

    records = [json.loads(line) for line in sections_path.open(encoding="utf-8")]
    usable = [r for r in records if r.get("quality_status") == "usable"]

    section_token_counts: Counter[str] = Counter()
    unigram_counts: dict[str, Counter[str]] = defaultdict(Counter)
    unigram_docs: dict[str, Counter[str]] = defaultdict(Counter)
    unigram_years: dict[str, dict[str, set[int]]] = defaultdict(lambda: defaultdict(set))
    ngram_counts: dict[str, Counter[tuple[str, ...]]] = defaultdict(Counter)
    ngram_docs: dict[str, Counter[tuple[str, ...]]] = defaultdict(Counter)
    ngram_years: dict[str, dict[tuple[str, ...], set[int]]] = defaultdict(lambda: defaultdict(set))

    term_stats: dict[tuple[str, str], dict[str, object]] = defaultdict(lambda: {"occurrences": 0, "docs": set(), "years": set()})
    rhet_stats: dict[tuple[str, str], dict[str, object]] = defaultdict(lambda: {"occurrences": 0, "docs": set(), "years": set()})

    for rec in usable:
        source_id = str(rec["source_id"])
        year = int(rec["year"])
        for section, text in rec["sections"].items():
            text = str(text)
            ts = tokens(text)
            if not ts:
                continue
            section_token_counts[section] += len(ts)
            doc_unigrams = set(t for t in ts if valid_token(t))
            unigram_counts[section].update(t for t in ts if valid_token(t))
            doc_ngram_counts: Counter[tuple[str, ...]] = Counter()
            for n in range(2, 6):
                for i in range(0, len(ts) - n + 1):
                    gram = tuple(ts[i:i + n])
                    if ngram_is_useful(gram):
                        doc_ngram_counts[gram] += 1
            ngram_counts[section].update(doc_ngram_counts)
            for gram in doc_ngram_counts:
                ngram_docs[section][gram] += 1
                ngram_years[section][gram].add(year)
            for token in doc_unigrams:
                unigram_docs[section][token] += 1
                unigram_years[section][token].add(year)

            lowered = text.lower()
            for term, pattern in TERMS.items():
                count = phrase_counts(pattern, lowered)
                if count:
                    key = (section, term)
                    term_stats[key]["occurrences"] += count
                    term_stats[key]["docs"].add(source_id)
                    term_stats[key]["years"].add(year)
            for phrase, pattern in RHETORICAL.items():
                count = phrase_counts(pattern, lowered)
                if count:
                    key = (section, phrase)
                    rhet_stats[key]["occurrences"] += count
                    rhet_stats[key]["docs"].add(source_id)
                    rhet_stats[key]["years"].add(year)

    lexicon_rows: list[dict[str, object]] = []
    for section in sorted(unigram_counts):
        total_tokens = section_token_counts[section]
        candidates = [
            (token, count) for token, count in unigram_counts[section].items()
            if unigram_docs[section][token] >= args.min_documents
        ]
        candidates.sort(key=lambda item: (unigram_docs[section][item[0]], item[1]), reverse=True)
        for rank, (token, count) in enumerate(candidates[:120], start=1):
            years = unigram_years[section][token]
            lexicon_rows.append({
                "section": section,
                "rank": rank,
                "term": token,
                "occurrences": count,
                "documents": unigram_docs[section][token],
                "per_10k_tokens": round(10000 * count / total_tokens, 3),
                "first_year": min(years),
                "last_year": max(years),
                "present_before_2020": int(any(y <= 2019 for y in years)),
            })
    write_rows(root / "data" / "section-lexicon.csv", list(lexicon_rows[0]), lexicon_rows)

    collocation_rows: list[dict[str, object]] = []
    for section in sorted(ngram_counts):
        total_tokens = section_token_counts[section]
        candidates = [
            (gram, count) for gram, count in ngram_counts[section].items()
            if ngram_docs[section][gram] >= args.min_documents
        ]
        candidates.sort(key=lambda item: (ngram_docs[section][item[0]], item[1]), reverse=True)
        for rank, (gram, count) in enumerate(candidates[:160], start=1):
            years = ngram_years[section][gram]
            collocation_rows.append({
                "section": section,
                "rank": rank,
                "ngram": " ".join(gram),
                "n": len(gram),
                "occurrences": count,
                "documents": ngram_docs[section][gram],
                "per_10k_tokens": round(10000 * count / total_tokens, 3),
                "first_year": min(years),
                "last_year": max(years),
                "present_before_2020": int(any(y <= 2019 for y in years)),
            })
    write_rows(root / "data" / "collocations.csv", list(collocation_rows[0]), collocation_rows)

    term_rows = []
    for (section, term), stats in term_stats.items():
        years = stats["years"]
        term_rows.append({
            "section": section,
            "term": term,
            "occurrences": stats["occurrences"],
            "documents": len(stats["docs"]),
            "first_year": min(years),
            "last_year": max(years),
            "present_before_2020": int(any(y <= 2019 for y in years)),
        })
    term_rows.sort(key=lambda r: (str(r["section"]), -int(r["documents"]), -int(r["occurrences"])))
    write_rows(root / "data" / "terminology-frequency.csv", list(term_rows[0]), term_rows)

    rhet_rows = []
    for (section, phrase), stats in rhet_stats.items():
        years = stats["years"]
        rhet_rows.append({
            "section": section,
            "phrase": phrase,
            "occurrences": stats["occurrences"],
            "documents": len(stats["docs"]),
            "first_year": min(years),
            "last_year": max(years),
            "present_before_2020": int(any(y <= 2019 for y in years)),
        })
    rhet_rows.sort(key=lambda r: (str(r["section"]), -int(r["documents"]), -int(r["occurrences"])))
    write_rows(root / "data" / "rhetorical-phrases.csv", list(rhet_rows[0]), rhet_rows)

    print(json.dumps({
        "usable_documents": len(usable),
        "section_tokens": dict(section_token_counts),
        "outputs": [
            "data/section-lexicon.csv", "data/collocations.csv",
            "data/terminology-frequency.csv", "data/rhetorical-phrases.csv",
        ],
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
