# Release Notes — v0.5.0

## Summary

EvoWrite v0.5.0 replaces advisory humanizing rules with a mandatory rewrite and output-gate system. It targets incomplete polishing, engineering-flavored vocabulary, administrative metaphors, repeated stock contrasts, and persistent LLM phrasing while preserving research meaning and standard EC terminology.

## Full paragraph rebuilding

AI-heavy text is now rebuilt from a silent record of the research meaning. The Skill no longer accepts isolated synonym replacement as a sufficient rewrite. Clean technical prose is left alone when further editing would add no value.

## Hard language gate

- New `plain-ec-english.md` defines plain, concrete EC academic English.
- New `revision-gate.md` defines delivery-blocking vocabulary, phrase, repetition, and structure failures.
- New `skill/data/prose-gate.json` is the single source of machine-checkable rules and narrow technical exceptions.
- New `tools/scripts/check_prose.py` checks exact candidate text and returns a nonzero status on any unapproved hit.
- `rather than`, stock `not X but Y`, repeated transitions, repeated sentence openings, and repeated non-technical n-grams are covered.

The gate applies to drafting, rewriting, and voice matching. Original wording does not receive an exemption. Standard technical usage such as DE `trial vector` and actual physical trajectories is protected by narrow exceptions.

Paired fresh-agent evaluation also exposed and fixed subtler bypasses: `instead of` cannot replace `rather than` as a stock contrast, robustness and scalability claims cannot survive through paraphrase, method names cannot be expanded into invented implementation steps, and Audit revisions cannot assert experiments or comparisons that were never supplied.

Release archives are now built strictly from `install-manifest.txt`, so unrelated development assets are not packaged into the Skill.

## References and examples

Overlapping style documents have been consolidated. Method and experiment guides no longer encourage one fixed paragraph shape or mandatory RQ lists. Every recommended After example is checked by the release build.

## Evaluation

- Added 12 realistic language-rewrite cases to the existing evidence and terminology cases.
- Added deterministic clean/blocked fixtures and unit tests for inflections, case, exceptions, repeated patterns, and command-line exit status.
- Release validation checks the lexicon, fixtures, and all recommended After examples.

## Compatibility

- Skill name remains `evo-write`.
- Normal rewriting still returns English paper text only.
- Audit reports remain available only when requested.
- Installers default to `v0.5.0`.
- The checker uses only the Python standard library; no new package dependency is introduced.

## Evidence and safety boundary

- Source TEVC papers are not included.
- 2024+ and unassigned early-access material remain excluded.
- Public data are aggregate statistics and original guidance, not reconstructable raw corpus text.
- EvoWrite is independent of IEEE and TEVC editorial policy.
- It does not guarantee publication or AI-detector outcomes.

---

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
