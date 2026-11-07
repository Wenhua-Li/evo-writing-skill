# Release Notes — v0.4.0

## Summary

`EvoWrite` v0.4.0 is the product-structure and presentation release. It simplifies the GitHub repository landing view, upgrades the brand artwork, and turns the GitHub Pages site into a full product landing page.

## Repository structure

The root directory now focuses on the files visitors need first:

- `README.md` / `README.zh-CN.md`
- `SKILL.md`
- `LICENSE` / `LICENSE-CC-BY-4.0`
- `CITATION.cff`
- `install.sh` / `install.ps1` / `install-manifest.txt`
- `docs/`, `skill/`, `tools/`, `.github/`

Skill runtime material now lives in `skill/`. Documentation, cases, release notes, and public artwork live in `docs/`. Corpus analysis and behavior evaluation tools live in `tools/`.

## Visual upgrade

- New banner, logo, and social preview artwork.
- Dark academic visual system with Pareto-front and evolutionary motifs.
- GitHub Pages now includes a hero, verification statistics, interactive before/after cases, use cases, EC domain tags, install cards, evidence boundary, comparison, and FAQ.
- Added `docs/cases.html` and `docs/install.html`.

## Compatibility

- Skill name remains `evo-write`.
- Release ZIP still installs with `evo-write/SKILL.md` at the top level.
- Runtime references are now under `evo-write/skill/`.
- `install.sh` and `install.ps1` default to `v0.4.0`.

## Evidence and safety boundary

- Source TEVC papers are not included.
- 2024+ and unassigned early-access material remain excluded.
- Public data are aggregate statistics and original guidance, not reconstructable raw corpus text.
- EvoWrite is independent of IEEE and TEVC editorial policy.
- It does not guarantee publication or AI-detector outcomes.

## Verification

- Repository restructure validated with Git rename history.
- Skill paths updated from `references/` to `skill/references/`.
- Release package checked for required entrypoint, payload layout, private paths, and excluded raw corpus data.
- Local installer and doctor checks run against the restructured package.
- Public installation and Pages verification performed after release.
