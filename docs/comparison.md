# Why not just use a generic humanizer?

Generic humanizers are useful, and many EC papers need more than they check.

## The short answer

Use a generic humanizer when the only problem is that the text sounds machine-generated.

Use EvoWrite when the text also has to respect EC evidence, terminology, and cost accounting.

## What generic humanizers usually miss

### 1. Cost claims

A generic editor may keep:

> The algorithm is highly efficient.

EvoWrite asks which cost measure supports the claim:

- exact function evaluations;
- generations;
- wall-clock runtime;
- surrogate model training time;
- memory;
- implementation complexity.

### 2. Multiobjective claims

A generic editor may keep:

> The algorithm improves both convergence and diversity.

EvoWrite checks whether the manuscript actually measures both, and whether it mixes up objective-space diversity with decision-space diversity.

### 3. Constraint claims

A generic editor may smooth a results paragraph without noticing that it reports objective values yet says nothing about feasibility or constraint violation.

### 4. Expensive optimization claims

A generic editor may treat surrogate-assisted optimization as ordinary EA writing. EvoWrite checks the real evaluation budget, the model-management strategy, and the modeling overhead.

### 5. Defensive academic framing

Generic AI-tell removal does not always tell a necessary scientific boundary from a defensive disclaimer. EvoWrite removes repeated disclaimers and keeps the validity-relevant scope once, in the section where it belongs.

## Compared with Humanizer

[blader/humanizer](https://github.com/blader/humanizer) is the strongest general-purpose reference point, with an excellent structural taxonomy of AI-sounding prose.

EvoWrite adapts that idea for EC papers and adds:

- EC-specific AI tells;
- rewriting of defensive academic framing;
- cost and evidence calibration;
- guidance for constrained, dynamic, expensive, large-scale, multimodal, and multiobjective settings;
- per-section guidance for algorithm, theory, benchmark, survey, and application papers;
- optional voice profiles for EC paper genres.

## Compared with Anti-Defensive Writing

[Kiterlin/anti-defensive-writing](https://github.com/Kiterlin/anti-defensive-writing) draws the line between necessary scope and unnecessary disclaimers.

EvoWrite follows the same principle and applies it to EC claims:

- `robustness` needs a perturbation model;
- `scalability` needs a dimension and a budget;
- efficiency needs a cost measure;
- significance needs a named statistical test;
- Pareto claims need the correct space and reference setting.

## Compared with domain writing packs

Domain writing packs, such as economics or Nature-style workflows, often try to cover the whole publication process. EvoWrite stays narrow on purpose:

- one installable skill;
- natural EC prose as the only goal;
- evidence and terminology checks run in the background;
- a report is written only when you ask for one.

## When not to use EvoWrite

- You need a full literature-review agent with citation retrieval.
- You need Word or LaTeX production automation.
- You need a generic non-academic humanizer.
- You want the tool to invent missing experiments, citations, or results.

EvoWrite rewrites and calibrates papers; it does not finish your research for you.
