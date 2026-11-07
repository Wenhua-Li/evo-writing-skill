# Release Notes — v0.3.3

## Summary

`EvoWrite` is an Agent Skill for natural, evidence-aware Evolutionary Computation paper writing. This patch fixes a Bash installer path-handling bug found during live public installation testing.

## What changed in v0.3.3

- Download progress and error messages are now written to stderr.
- The remote source path is the only stdout value returned by the Bash download function.
- Fixed a failure where the Release ZIP downloaded successfully but the installer could not locate `SKILL.md`.

## Included in the v0.3 series

- Natural EC prose rewriting with AI-tell removal.
- Anti-defensive academic writing with positive scope.
- EC-specific claim calibration for significance, robustness, scalability, efficiency, optimality, convergence, diversity, and cost.
- Optional author voice matching.
- English and Simplified Chinese README.
- GitHub Pages landing page.
- Behavior evaluation cases.
- Reproducible aggregate corpus evidence from 1,517 TEVC papers (1997–2023).

## Evidence and safety boundary

- Source TEVC papers are not included.
- 2024+ and unassigned early-access material are excluded.
- Public data are aggregate statistics and original guidance, not reconstructable raw corpus text.
- EvoWrite is independent of IEEE and TEVC editorial policy.
- It does not guarantee publication or AI-detector outcomes.

## Verification

- Public repository and GitHub Pages were created and verified.
- Release archive checked for skill name, install layout, raw corpus exclusion, private paths, and required files.
- Public installer strategy was tested against live network conditions and adjusted to use Release assets by default.
- The Bash path-handling issue found by the live installer test is fixed in this release.

## Known limitations

- Naturalness has not yet been evaluated through a multi-rater blind study.
- Voice matching depends on the supplied sample.
- PowerShell installation was statically reviewed but not executed in the local validation environment.
