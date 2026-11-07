# Release Notes — v0.3.2

## Summary

`EvoWrite` is an Agent Skill for natural, evidence-aware Evolutionary Computation paper writing. This patch makes the public installer resilient in restricted networks.

## What changed in v0.3.2

- The installer now downloads the Release ZIP by default instead of a Git source archive.
- If the Release archive is unavailable, it falls back to `install-manifest.txt` and per-file downloads from `raw.githubusercontent.com`.
- Remote downloads now use retry logic.
- Local installation from a cloned repository remains unchanged.

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
- Public installer strategy was changed after live network tests showed source-archive and repeated raw downloads could fail while Release assets remained reachable.
- The Release ZIP path is the intended default installation source for this version.

## Known limitations

- Naturalness has not yet been evaluated through a multi-rater blind study.
- Voice matching depends on the supplied sample.
- PowerShell installation was statically reviewed but not executed in the local validation environment.
