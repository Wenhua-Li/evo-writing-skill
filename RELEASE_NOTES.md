# Release Notes — v0.3.1

## Summary

`EvoWrite` is an Agent Skill for natural, evidence-aware Evolutionary Computation paper writing. This patch release improves the public installer so one-command installation works even when GitHub tarball/codeload downloads are blocked.

## What changed in v0.3.1

- Added `install-manifest.txt` with the complete public file list.
- Reworked `install.sh` to download each public file from `raw.githubusercontent.com` when installing from a ref.
- Reworked `install.ps1` to use the same manifest-based remote installation strategy.
- Kept local-source installation unchanged.

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

- Public repository created and verified.
- Release archive checked for skill name, install layout, raw corpus exclusion, private paths, and required files.
- Public GitHub Pages page verified.
- Installer fallback changed after detecting codeload/network failure; manifest-based raw download is the intended public installation path.

## Known limitations

- Naturalness has not yet been evaluated through a multi-rater blind study.
- Voice matching depends on the supplied sample.
- PowerShell installation was statically reviewed but not executed in the local validation environment.
