#!/usr/bin/env python3
"""Reject blocked wording and repetitive templates in candidate paper prose."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_LEXICON = ROOT / "skill" / "data" / "prose-gate.json"
PROTECTED_RE = re.compile(
    r"\$\$[\s\S]*?\$\$|\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)|"
    r"\$[^$\n]+\$|`[^`\n]*`|https?://\S+|\"(?:\\.|[^\"\\])*\"|“[^”]*”"
)
WORD_RE = re.compile(r"\b[A-Za-z]+(?:[-'][A-Za-z]+)?\b")
SENTENCE_PREFIX = r"(?:\A|(?<=[.!?])[ \t]+|\n[ \t]*\n[ \t]*)"
EC_CONTENT_WORDS = {
    "algorithm",
    "algorithms",
    "benchmark",
    "constraint",
    "constraints",
    "convergence",
    "decision",
    "diversity",
    "evaluation",
    "evaluations",
    "evolutionary",
    "fitness",
    "function",
    "functions",
    "hypervolume",
    "igd",
    "multiobjective",
    "nondominated",
    "objective",
    "objectives",
    "optimization",
    "pareto",
    "population",
    "solution",
    "solutions",
    "surrogate",
    "variable",
    "variables",
}


def mask_protected(text: str) -> str:
    def mask(match: re.Match[str]) -> str:
        return "".join("\n" if char == "\n" else " " for char in match.group(0))

    return PROTECTED_RE.sub(mask, text)


def location(text: str, position: int) -> tuple[int, int]:
    line = text.count("\n", 0, position) + 1
    previous_newline = text.rfind("\n", 0, position)
    return line, position - previous_newline


def finding(
    text: str,
    position: int,
    rule: str,
    matched: str,
    message: str,
    category: str,
) -> dict[str, Any]:
    line, column = location(text, position)
    return {
        "line": line,
        "column": column,
        "rule": rule,
        "match": matched,
        "message": message,
        "category": category,
    }


def overlaps(start: int, end: int, spans: list[tuple[int, int]]) -> bool:
    return any(start < span_end and end > span_start for span_start, span_end in spans)


def check_patterns(text: str, masked: str, rules: dict[str, Any]) -> list[dict[str, Any]]:
    findings = []
    for category, key in (("term", "blocked_terms"), ("phrase", "blocked_phrases")):
        for rule in rules[key]:
            allowed_spans = []
            for allowed in rule.get("allow_patterns", []):
                allowed_spans.extend(match.span() for match in re.finditer(allowed, masked, re.IGNORECASE))
            for match in re.finditer(rule["pattern"], masked, re.IGNORECASE):
                if overlaps(match.start(), match.end(), allowed_spans):
                    continue
                findings.append(
                    finding(
                        text,
                        match.start(),
                        rule["id"],
                        text[match.start() : match.end()],
                        rule["message"],
                        category,
                    )
                )
    return findings


def sentence_starts(masked: str, expression: str) -> list[re.Match[str]]:
    return list(re.finditer(SENTENCE_PREFIX + expression, masked, re.IGNORECASE))


def check_transitions(text: str, masked: str, structure: dict[str, Any]) -> list[dict[str, Any]]:
    findings = []
    occurrences = []
    single_use = set(structure["single_use_sentence_initial_transitions"])
    for transition in structure["sentence_initial_transitions"]:
        matches = sentence_starts(masked, re.escape(transition) + r"\b")
        occurrences.extend((match.start(), transition, match) for match in matches)
        if transition in single_use and len(matches) > 1:
            for match in matches[1:]:
                findings.append(
                    finding(
                        text,
                        match.start(),
                        "repeated-transition",
                        transition,
                        f"Use '{transition}' at the start of at most one sentence in the candidate text.",
                        "structure",
                    )
                )
    occurrences.sort(key=lambda item: item[0])
    for previous, current in zip(occurrences, occurrences[1:]):
        if previous[1] == current[1] and previous[1] not in single_use:
            findings.append(
                finding(
                    text,
                    current[0],
                    "adjacent-transition",
                    current[1],
                    f"Avoid consecutive sentences beginning with '{current[1]}'.",
                    "structure",
                )
            )
    return findings


def check_openings(text: str, masked: str, structure: dict[str, Any]) -> list[dict[str, Any]]:
    expression = r"([A-Za-z]+(?:[-'][A-Za-z]+)?)[ \t]+([A-Za-z]+(?:[-'][A-Za-z]+)?)\b"
    matches = sentence_starts(masked, expression)
    findings = []
    previous_opening = None
    run_length = 0
    maximum = structure["max_consecutive_same_two_word_opening"]
    for match in matches:
        opening = f"{match.group(1)} {match.group(2)}".casefold()
        if opening == previous_opening:
            run_length += 1
        else:
            previous_opening = opening
            run_length = 1
        if run_length == maximum + 1:
            findings.append(
                finding(
                    text,
                    match.start(),
                    "repeated-sentence-opening",
                    opening,
                    f"More than {maximum} consecutive sentences begin with '{opening}'.",
                    "structure",
                )
            )
    return findings


def check_repeated_ngrams(text: str, masked: str, structure: dict[str, Any]) -> list[dict[str, Any]]:
    size = structure["repeated_ngram_size"]
    maximum = structure["max_repeated_ngram_occurrences"]
    words = list(WORD_RE.finditer(masked))
    occurrences: dict[tuple[str, ...], list[re.Match[str]]] = {}
    for index in range(len(words) - size + 1):
        window = words[index : index + size]
        segment = masked[window[0].start() : window[-1].end()]
        if re.search(r"[.!?]\s|\n[ \t]*\n", segment):
            continue
        normalized = tuple(word.group(0).casefold() for word in window)
        if any(word in EC_CONTENT_WORDS for word in normalized):
            continue
        occurrences.setdefault(normalized, []).append(window[0])
    findings = []
    for normalized, matches in occurrences.items():
        if len(matches) <= maximum:
            continue
        for match in matches[maximum:]:
            findings.append(
                finding(
                    text,
                    match.start(),
                    "repeated-ngram",
                    " ".join(normalized),
                    f"This non-technical {size}-word sequence occurs more than {maximum} time(s).",
                    "structure",
                )
            )
    return findings


def check_text(
    text: str,
    rules: dict[str, Any],
    include_structure: bool = True,
) -> list[dict[str, Any]]:
    masked = mask_protected(text)
    findings = check_patterns(text, masked, rules)
    if include_structure:
        structure = rules["structure"]
        findings.extend(check_transitions(text, masked, structure))
        findings.extend(check_openings(text, masked, structure))
        findings.extend(check_repeated_ngrams(text, masked, structure))
    findings.sort(key=lambda item: (item["line"], item["column"], item["rule"]))
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", default=["-"], help="Text files, or - for standard input.")
    parser.add_argument("--lexicon", type=Path, default=DEFAULT_LEXICON)
    parser.add_argument("--no-structure", action="store_true", help="Only check blocked terms and phrases.")
    parser.add_argument("--json", action="store_true", help="Write machine-readable results.")
    args = parser.parse_args(argv)
    try:
        rules = json.loads(args.lexicon.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        parser.exit(2, f"Cannot load lexicon: {error}\n")
    results = []
    for filename in args.files:
        try:
            text = sys.stdin.read() if filename == "-" else Path(filename).read_text(encoding="utf-8")
        except OSError as error:
            parser.exit(2, f"Cannot read {filename}: {error}\n")
        findings = check_text(text, rules, include_structure=not args.no_structure)
        results.append({"file": filename, "passed": not findings, "findings": findings})
    if args.json:
        print(json.dumps({"passed": all(item["passed"] for item in results), "results": results}, ensure_ascii=False, indent=2))
    else:
        for result in results:
            for item in result["findings"]:
                print(
                    f"{result['file']}:{item['line']}:{item['column']}: "
                    f"{item['rule']}: {item['match']!r} -- {item['message']}"
                )
    return 0 if all(result["passed"] for result in results) else 1


if __name__ == "__main__":
    sys.exit(main())
