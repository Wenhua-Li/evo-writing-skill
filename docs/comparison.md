# Why not just use a generic humanizer?

Generic humanizers are useful, but Evolutionary Computation papers fail in ways that generic prose rules cannot detect.

## The short answer

Use a generic humanizer when your only problem is that the text sounds machine-generated.

Use EvoWrite when the text also has to respect EC-specific evidence, terminology, and evaluation logic.

## What generic humanizers usually miss

### 1. Cost claims

A generic editor may keep:

> The algorithm is highly efficient.

EvoWrite asks what cost measure supports that claim:

- exact function evaluations;
- generations;
- wall-clock runtime;
- surrogate model training time;
- memory;
- implementation complexity.

### 2. Multiobjective claims

A generic editor may keep:

> The algorithm improves both convergence and diversity.

EvoWrite checks whether the manuscript actually measures both, and whether it confuses objective-space diversity with decision-space diversity.

### 3. Constraint claims

A generic editor may smooth a result paragraph without noticing that it reports objective quality but not feasibility or constraint violation.

### 4. Expensive optimization claims

A generic editor may treat surrogate-assisted optimization as ordinary EA writing. EvoWrite checks the real evaluation budget, model-management strategy, and model overhead.

### 5. Defensive academic framing

Generic AI-tell removal does not always distinguish necessary scientific boundaries from defensive writing. EvoWrite removes repeated disclaimers but keeps validity-relevant scope once, in the correct section.

## Compared with Humanizer

[blader/humanizer](https://github.com/blader/humanizer) is the strongest general-purpose reference point. It provides an excellent structural taxonomy for AI-sounding prose.

EvoWrite adapts that idea for EC papers and adds:

- EC-specific AI tells;
- anti-defensive academic rewriting;
- cost and evidence calibration;
- domain routing for constrained, dynamic, expensive, large-scale, multimodal, and multiobjective settings;
- article-type guidance for algorithms, theory, benchmarks, surveys, and applications;
- optional voice profiles for EC paper genres.

## Compared with Anti-Defensive Writing

[Kiterlin/anti-defensive-writing](https://github.com/Kiterlin/anti-defensive-writing) provides the key distinction between necessary scope and unnecessary disclaimers.

EvoWrite uses the same broad principle but applies it to EC-specific claims:

- robustness requires a perturbation model;
- scalability requires a dimension and budget;
- efficiency requires a cost measure;
- significance requires a statistical protocol;
- Pareto claims require the correct space and reference setting.

## Compared with domain writing packs

Domain writing packs such as economics or Nature-style workflows often cover a whole publication pipeline. EvoWrite is deliberately narrower:

- one installable skill;
- focused on natural EC prose;
- evidence and terminology checks stay in the background;
- audit mode is available only when requested.

## When not to use EvoWrite

- You need a full literature review agent with citation retrieval.
- You need Word/LaTeX production automation.
- You need a generic non-academic humanizer.
- You want the tool to invent missing experiments, citations, or results.

EvoWrite is a writing and evidence-calibration skill, not a research-completion agent.
