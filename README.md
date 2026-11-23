<div align="center">

<img src="docs/assets/banner.svg" alt="EvoWrite banner" width="100%">

# EvoWrite

**Natural writing for Evolutionary Computation papers, with the evidence left intact.**

Built from **1,517 TEVC papers (1997–2023)** and a close reading of 150 papers sampled across periods and paper types. EvoWrite rebuilds AI-sounding paragraphs, removes software metaphors and repeated LLM phrasing, and keeps your claims, citations, standard EC terminology, and voice unchanged.

[简体中文](README.zh-CN.md) · [Quick start](docs/quickstart.md) · [Cases](docs/cases.html) · [Docs](docs/)

[![Release](https://img.shields.io/badge/release-v0.6.0-38bdf8)](https://github.com/Wenhua-Li/evo-writing-skill/releases)
[![Agent Skills](https://img.shields.io/badge/agent--skills-compatible-14b8a6)](https://agentskills.io)
[![License](https://img.shields.io/badge/license-MIT%20%2B%20CC--BY--4.0-blue)](LICENSE)
[![Corpus](https://img.shields.io/badge/TEVC%20corpus-1997--2023-94a3b8)](skill/references/evidence/methodology.md)

</div>

---

## See the difference

<table>
<tr><th>Before — AI-sounding and defensive</th><th>After — plain EC prose</th></tr>
<tr><td>

> With the rapid development of evolutionary computation, large-scale multiobjective optimization has become a hot topic. It is worth noting that our proposed method may potentially significantly outperform state-of-the-art algorithms, although we do not claim that it is universally optimal for all problems. The main contributions are as follows: 1) We propose a novel framework. 2) We design an efficient operator. 3) We conduct extensive experiments.

</td><td>

> Large-scale multiobjective optimization becomes harder as the number of decision variables increases. This paper presents a search framework and a variation operator for this setting. On the tested problems, the proposed algorithm outperforms the algorithms included in the comparison.

</td></tr>
</table>

Nothing is invented, and the defensive hedging is gone.

## Why EvoWrite?

A generic humanizer can make a paragraph smoother and still keep the abstract, inflated, engineering-flavored wording. EvoWrite rebuilds the paragraph first and then checks it against fixed rules:

- Rewrites from the research meaning when light editing is not enough.
- Rejects software, management, and promotional metaphors in paper prose.
- Sends blocked wording and formulaic contrasts back for another rewrite; they never ship as warnings.
- Keeps `function evaluations`, wall-clock runtime, model-training cost, and implementation complexity apart.
- Keeps convergence, diversity, feasibility, objective value, and fitness apart.
- Knows the vocabulary of surrogate-assisted, constrained, dynamic, large-scale, multimodal, and multiobjective optimization.
- Keeps a necessary methodological limitation once, in the section where the reader needs it.
- Matches the rhythm of an author's writing sample without copying wording the gate blocks.

## Quick start

```bash
npx skills add Wenhua-Li/evo-writing-skill
```

Or:

```bash
curl -fsSL https://raw.githubusercontent.com/Wenhua-Li/evo-writing-skill/main/install.sh | bash
```

Windows PowerShell:

```powershell
iwr https://raw.githubusercontent.com/Wenhua-Li/evo-writing-skill/main/install.ps1 | iex
```

Then ask:

```text
Use evo-write. Rewrite this introduction to remove AI tells and defensive writing.
Return only the revised English.
```

More options: [`docs/install.html`](docs/install.html) and [`docs/quickstart.md`](docs/quickstart.md).

## What it does

### Rebuilds AI-sounding prose

When a draft is full of AI phrasing, EvoWrite notes what each paragraph actually says and writes it again. Swapping adjectives and connectors on the old sentence skeleton does not count as a rewrite.

### Enforces plain EC English

The blocked list covers the reported terms `axes`, `synthetic`, `provenance`, `admission`, `extreme`, `declared`, `protocol`, `tie`, `saturated`, `trajectories`, `certified`, `menus`, `audit`, `inferred`, `rather than`, `trial`, `rival`, and `refinement`, together with common inflections and related LLM wording.

A hit sends the text back; nothing is delivered with warnings attached. Narrow technical exceptions protect standard usage such as the DE `trial vector`, an actual robot trajectory, a stated `synthetic data` category, coordinate axes, and established `extreme solutions`. The complete rules are in [`skill/data/prose-gate.json`](skill/data/prose-gate.json).

### Checks structure and repetition

The gate also rejects formulaic `rather than`, `instead of`, and `not X but Y` contrasts, empty research-interest openings, `do not claim` disclaimers, `robustness` and `scalability` claims with no stated evidence, repeated sentence-opening connectors, three sentences in a row with the same two-word opening, and repeated six-word sequences. A clean scan does not prove the text reads well, so human review is still needed.

### Removes defensive writing

- `We do not claim...` → a direct statement of the evaluation scope;
- `may potentially suggest` → `suggests`, `indicates`, or a precise bounded statement;
- repeated limitations → one concrete limitation in the right section.

### Preserves scientific meaning

EvoWrite does not invent research, and it does not quietly strengthen claims. Citations, DOIs, numerical results, uncertainty, negative results, theorem conditions, benchmark names, baselines, indicators, budgets, statistical tests, algorithm mechanisms, assumptions, and application constraints are carried over unchanged.

### Checks claim strength when asked

On request, Audit mode flags claims the evidence does not support: `statistically significant` with no test, `optimal` with no guarantee, `robust` with no perturbation model, `scalable` with no dimension and budget ranges, and `efficient` with no defined cost measure.

## How it works

```mermaid
flowchart LR
    A[Your draft] --> B[Record claims and evidence]
    B --> C[Rebuild from meaning]
    C --> D[Plain EC language pass]
    D --> E[Hard prose gate]
    E --> F[Fact and terminology check]
    F --> G[Final paper text]
    E -- blocked wording --> C
```

If your setup can run Python, the exact candidate text can be checked with:

```bash
python tools/scripts/check_prose.py -
```

The checker uses the Python standard library only. Where nothing can be executed, the same JSON rules are applied by hand.

## Evidence base

The public package contains aggregate statistics and original guidance, never the source papers.

- Corpus: 1,517 TEVC Markdown papers from 1997–2023
- Language analysis: 1,358 quality-controlled papers
- Qualitative review: 150 papers sampled across periods, paper types, and research settings
- Excluded: 2024+ papers and unassigned early-access material
- Purpose: grounding the rules in real EC writing and confirming common expressions; corpus frequency never overrides the blocked list

See [`skill/references/evidence/methodology.md`](skill/references/evidence/methodology.md), [`corpus-findings.md`](skill/references/evidence/corpus-findings.md), and [`limitations.md`](skill/references/evidence/limitations.md).

## Repository layout

```text
├── SKILL.md          # evo-write entry point
├── skill/            # runtime references, voices, examples, templates, data
├── docs/             # website, guides, cases, release notes, public assets
├── tools/            # corpus analysis, prose gate, and behavior evaluations
├── install.sh
├── install.ps1
└── install-manifest.txt
```

## Limits

- EvoWrite improves readability and claim calibration; it does not guarantee publication.
- The goal is prose that reads naturally to human reviewers, not AI-detector evasion.
- The corpus evidence is TEVC-specific and independent of IEEE or TEVC editorial policy.
- Source papers are not included; aggregate statistics and original guidance are.
- Voice matching depends on the quality of the supplied writing sample.

## Contributing

Contributions are welcome, especially EC-specific before/after examples, behavior cases for unsupported claims, domain guides, and installer improvements. See [`.github/CONTRIBUTING.md`](.github/CONTRIBUTING.md).

## Citation

```bibtex
@software{li_evowrite_2026,
  author  = {Li, Wenhua},
  title   = {EvoWrite: Natural Evolutionary Computation Paper Writing},
  year    = {2026},
  version = {0.6.0},
  url     = {https://github.com/Wenhua-Li/evo-writing-skill},
  license = {MIT and CC-BY-4.0}
}
```

## Acknowledgements

EvoWrite's structural analysis of AI tells was inspired by [blader/humanizer](https://github.com/blader/humanizer), and its claim-forward and positive-scope treatment was inspired by [Kiterlin/anti-defensive-writing](https://github.com/Kiterlin/anti-defensive-writing). The rules, examples, and domain evidence here are redesigned for Evolutionary Computation.

## License

- Scripts: [MIT License](LICENSE)
- Skill documentation, rules, templates, examples, and aggregate data: [CC BY 4.0](LICENSE-CC-BY-4.0)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Wenhua-Li/evo-writing-skill&type=Date)](https://star-history.com/#Wenhua-Li/evo-writing-skill&Date)
