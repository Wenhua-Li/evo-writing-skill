# EvoWrite behavior and language evaluations

These cases describe observable behavior expected from `evo-write`. They are evaluation prompts and acceptance checks, not a substitute for human review.

## Files

- `behavior-cases.json`: original evidence, terminology, drafting, and Audit behavior cases.
- `language-rewrite-cases.json`: 12 realistic cases for engineering vocabulary, stock contrasts, full rewriting, factual preservation, voice matching, and technical exceptions.
- `prose-gate-fixtures.json`: deterministic clean and blocked inputs for the checker.
- `test_prose_gate.py`: standard-library unit tests, including all recommended After examples.

Run the deterministic suite from the repository root:

```bash
python -m unittest discover -s tools/evals -p "test_*.py" -v
```

Run the checker on a complete candidate text:

```bash
python tools/scripts/check_prose.py -
```

Add `--json` for structured output. Exit status 0 means no finding; status 1 means at least one rule failed.

## Fresh-agent comparison

Run old and new Skill versions in separate fresh sessions with the same prompts. For each case, check:

1. factual and numerical preservation;
2. no invented evidence;
3. zero unapproved prose-gate findings;
4. substantial rebuilding when the source has heavy AI phrasing;
5. EC terminology and narrow technical exceptions;
6. correct output mode;
7. human readability after the automatic gate has passed.

The JSON prompt files use this schema:

- `id`: short identifier;
- `mode`: rewrite, draft, voice-match, or audit;
- `input`: prompt material;
- `must`: required behavior;
- `must_not`: forbidden behavior;
- `notes`: review guidance.

A clean automatic scan is necessary but not sufficient. Any remaining engineering tone, unintelligible metaphor, mechanical rhythm, or loss of meaning requires another iteration.
