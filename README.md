<div align="center">

<img src="assets/banner.svg" alt="EvoWrite banner" width="100%">

# EvoWrite

**Natural, evidence-aware writing for Evolutionary Computation papers.**

Distilled from **1,517 TEVC papers (1997–2023)** and a stratified review of 150 papers. EvoWrite removes AI tells and defensive prose while preserving claims, evidence, EC terminology, and the author's voice.

[简体中文](README.zh-CN.md) · [Quick start](#quick-start) · [Examples](examples/) · [Docs](docs/)

[![Release](https://img.shields.io/badge/release-v0.3.0-38bdf8)](https://github.com/Wenhua-Li/evo-writing-skill/releases)
[![Agent Skills](https://img.shields.io/badge/agent--skills-compatible-14b8a6)](https://agentskills.io)
[![License](https://img.shields.io/badge/license-MIT%20%2F%20CC--BY--4.0-blue)](LICENSE)
[![Corpus](https://img.shields.io/badge/TEVC%20corpus-1997--2023-94a3b8)](references/evidence/methodology.md)

</div>

---

## See the difference

<table>
<tr>
<th>Before — AI-sounding and defensive</th>
<th>After — natural EC prose</th>
</tr>
<tr>
<td>

> With the rapid development of evolutionary computation, large-scale multiobjective optimization has become a hot topic. It is worth noting that our proposed method may potentially significantly outperform state-of-the-art algorithms, although we do not claim that it is universally optimal for all problems. The main contributions are as follows: 1) We propose a novel framework. 2) We design an efficient operator. 3) We conduct extensive experiments.

</td>
<td>

> Large-scale multiobjective optimization remains challenging for evolutionary algorithms as the number of decision variables increases. This paper addresses this setting and makes three contributions: a framework for large-scale multiobjective optimization, an efficient search operator, and an extensive experimental evaluation. On the tested problems, the proposed algorithm outperforms the state-of-the-art algorithms included in the comparison.

</td>
</tr>
</table>

**No invented results. No defensive disclaimer. No generic AI phrasing.**

## Why EvoWrite?

Generic humanizers can make text smoother, but they do not know what makes an EC claim technically wrong. EvoWrite checks both **human readability** and **field-specific evidence use**:

- Distinguishes `function evaluations`, wall-clock runtime, model-training cost, and implementation complexity.
- Distinguishes convergence, diversity, feasibility, objective value, and fitness.
- Understands surrogate-assisted, constrained, dynamic, large-scale, multimodal, and multiobjective optimization.
- Removes AI tells, forced templates, boilerplate openings, stacked hedges, and defensive disclaimers.
- Keeps necessary methodological boundaries once, in the section where the reader needs them.
- Can match the rhythm and habits of your own English writing sample.

## Quick start

### Install with one command

```bash
npx skills add Wenhua-Li/evo-writing-skill
```

Or use the installer:

```bash
curl -fsSL https://raw.githubusercontent.com/Wenhua-Li/evo-writing-skill/main/install.sh | bash
```

Windows PowerShell:

```powershell
iwr https://raw.githubusercontent.com/Wenhua-Li/evo-writing-skill/main/install.ps1 | iex
```

For manual installation, copy this repository to your agent's skill directory as `evo-write/`. For Kimi Code on Windows:

```text
%USERPROFILE%\.agents\skills\evo-write\
```

### First rewrite

```text
Use evo-write. Rewrite this introduction to remove AI tells and defensive writing.
Return only the revised English.
```

### Voice matching

```text
Use evo-write. Here are two paragraphs from my previous paper. Match their rhythm and terminology, then rewrite the following method section.
```

### Evidence audit

```text
Use evo-write in Audit mode. Check this abstract for unsupported significance, robustness, scalability, and cost claims.
```

## What it does

### 1. Humanizes EC prose

Removes EC-specific AI tells:

- grand openings and “hot topic” framing;
- forced three-part contribution lists and mechanical RQs;
- `It is worth noting that`, `plays a crucial role`, and empty importance claims;
- vague `novel`, `efficient`, `robust`, `scalable`, and `state-of-the-art` claims;
- repetitive transitions, uniform paragraphs, and template-like results prose.

### 2. Removes defensive writing

Converts defensive scope into positive, evidence-bound scope:

- `We do not claim...` → `The evaluation focuses on...`
- `may potentially suggest` → `suggests`, `indicates`, or a precise bounded statement
- repeated limitations in abstracts and conclusions → one concrete limitation in the right section

### 3. Preserves scientific meaning

EvoWrite does not invent or silently strengthen research. It preserves:

- citations, DOIs, numerical results, uncertainty, negative results, and theorem conditions;
- benchmark names, baselines, indicators, budgets, and statistical tests;
- algorithm mechanisms, assumptions, and application constraints.

### 4. Audits claim strength when asked

Audit mode flags unsupported or over-scoped claims such as:

- `statistically significant` without a named test;
- `optimal` without a formal guarantee;
- `robust` without a perturbation model;
- `scalable` without dimension and budget ranges;
- `efficient` without a defined cost measure.

## How it works

```mermaid
flowchart LR
    A[Your draft] --> B[Preserve claims and evidence]
    B --> C[Remove AI tells]
    C --> D[Remove defensive prose]
    D --> E[Calibrate EC terminology]
    E --> F[Natural paper text]
```

EvoWrite reads only the references needed for the task:

- rewriting: AI-tell, anti-defensive, and scholarly-voice rules;
- drafting: article type, target section, and domain logic;
- voice matching: the supplied author sample;
- audit: claim calibration and submission checks.

## Evidence base

The public package contains aggregate evidence and original guidance, not the source papers.

- Corpus: 1,517 TEVC Markdown papers from 1997–2023
- Language analysis: 1,358 quality-controlled papers
- Qualitative review: 150 stratified papers across periods, paper types, and research settings
- Excluded: 2024+ papers and unassigned early-access material
- Purpose: domain grounding, not template extraction

See [`references/evidence/methodology.md`](references/evidence/methodology.md), [`corpus-findings.md`](references/evidence/corpus-findings.md), and [`limitations.md`](references/evidence/limitations.md).

## Why not just use a generic humanizer?

| Generic humanizer | EvoWrite |
|---|---|
| Removes general AI tells | Removes general and EC-specific AI tells |
| Keeps prose factual | Keeps prose factual and technically calibrated for EC |
| No domain evidence model | Distinguishes FEs, runtime, surrogate cost, convergence, diversity, and feasibility |
| One style for every field | Supports algorithm, theory, benchmark, survey, and application papers |
| Optional voice matching | Voice matching plus EC voice profiles |

See [`docs/comparison.md`](docs/comparison.md).

## Repository layout

```text
├── SKILL.md          # evo-write entry point
├── references/       # article types, sections, domains, style, evidence
├── voice/            # voice profiles for major EC paper types
├── examples/         # before/after examples
├── templates/        # intake and review templates
├── scripts/          # reproducible corpus analysis and release tools
├── data/             # aggregate corpus statistics
├── docs/             # guides and comparisons
└── assets/           # logo and social artwork
```

## Limits

- EvoWrite improves readability and claim calibration; it does not guarantee publication.
- It does not aim to fool AI detectors; it aims to read naturally to human reviewers.
- The corpus evidence is TEVC-specific and independent of IEEE or TEVC editorial policy.
- Source papers are not included. Aggregate statistics and original guidance are included instead.
- Voice matching depends on the quality of the supplied writing sample.

## Contributing

Contributions are welcome, especially:

- EC-specific before/after examples;
- behavior cases for unsupported claims;
- domain guides for under-covered EC subfields;
- installer and compatibility improvements.

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Citation

If EvoWrite helps your research workflow, please cite it:

```bibtex
@software{li_evowrite_2026,
  author  = {Li, Wenhua},
  title   = {EvoWrite: Natural Evolutionary Computation Paper Writing},
  year    = {2026},
  version = {0.3.0},
  url     = {https://github.com/Wenhua-Li/evo-writing-skill},
  license = {MIT and CC-BY-4.0}
}
```

## Acknowledgements

EvoWrite's structural AI-tell pipeline was inspired by [blader/humanizer](https://github.com/blader/humanizer), and its claim-forward and positive-scope treatment was inspired by [Kiterlin/anti-defensive-writing](https://github.com/Kiterlin/anti-defensive-writing). The rules, examples, and domain evidence here are redesigned for Evolutionary Computation.

## License

- Scripts: [MIT License](LICENSE)
- Skill documentation, rules, templates, examples, and aggregate data: [CC BY 4.0](LICENSE-CC-BY-4.0)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Wenhua-Li/evo-writing-skill&type=Date)](https://star-history.com/#Wenhua-Li/evo-writing-skill&Date)
