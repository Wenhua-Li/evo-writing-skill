# Contributing

Thanks for helping improve EvoWrite.

## Best contributions

- EC-specific before/after examples;
- behavior cases where the Skill overclaims, invents evidence, or sounds templated;
- clearer guidance for under-covered EC subfields;
- installer, compatibility, and documentation fixes;
- bug reports with a minimal input and the actual output.

## Ground rules

1. Do not add copyrighted paper text or large excerpts.
2. Do not add rules that require fabricating citations, experiments, values, statistical tests, or results.
3. Keep necessary scientific boundaries; anti-defensive editing must not become overclaiming.
4. Prefer concrete examples and observed failures over general style opinions.
5. If behavior changes, add or update an example or behavior case.

## Development checks

Run these before submitting:

```bash
python -m py_compile tools/scripts/*.py
python tools/scripts/build_release.py --root . --version v0.4.0
```

If you edit corpus analysis outputs, rerun the relevant analysis script and explain the change.

## Pull requests

Please include:

- the user-facing problem;
- what changed;
- before/after behavior where applicable;
- whether public aggregate data or only guidance changed.
