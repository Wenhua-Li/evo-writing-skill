# Release Notes — v0.3.0

## Summary

`EvoWrite` is the open-source launch release of the Evolutionary Computation writing Skill formerly called `ec-writing`.

This release rebrands the project, adds a product-quality README and landing page, provides cross-platform installers, and packages the v0.2 natural-writing redesign for public use.

## Highlights

- New identity: `EvoWrite`, invoked as `evo-write`.
- Product README in English and Simplified Chinese.
- Brand banner, logo, and social preview artwork.
- GitHub Pages landing page under `docs/`.
- One-command installation via Skills CLI, Bash, or PowerShell.
- Comparison page explaining when to use EvoWrite instead of a generic humanizer.
- Behavior evaluation cases for rewriting, drafting, terminology, cost calibration, and audit mode.
- Citation metadata and community contribution files.

## Included writing behavior

- Removes AI tells and template-like EC prose.
- Removes defensive writing while preserving necessary scientific scope.
- Preserves claims, citations, numbers, negative results, and theorem conditions.
- Calibrates EC-specific claims about significance, robustness, scalability, efficiency, optimality, convergence, diversity, and cost.
- Supports author voice matching.
- Returns English paper text by default; diagnostics are opt-in.

## Evidence boundary

- Source TEVC papers are not included.
- Corpus evidence remains limited to 1997–2023.
- 2024+ and unassigned early-access material are excluded.
- Aggregate statistics and original guidance are included; raw corpus text is not.
- EvoWrite is independent of IEEE and TEVC editorial policy.

## Verification

- Release archive built with private build data excluded.
- Cross-platform installer scripts included and syntax-checked.
- Package validated for skill name, entrypoint, archive structure, and private-path markers.
- Local installation refreshed and checked against repository files.
- Real CLI calls tested default rewriting and explicit Audit behavior.

## Known limitations

- EvoWrite improves readability and claim calibration; it does not guarantee publication.
- It does not aim to bypass AI detectors.
- Naturalness has not yet been evaluated through a multi-rater blind study.
- Voice matching depends on the supplied sample.
