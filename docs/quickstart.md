# Quick start

## 1. Install

Recommended:

```bash
npx skills add Wenhua-Li/evo-writing-skill
```

Installer:

```bash
curl -fsSL https://raw.githubusercontent.com/Wenhua-Li/evo-writing-skill/main/install.sh | bash
```

Windows PowerShell:

```powershell
iwr https://raw.githubusercontent.com/Wenhua-Li/evo-writing-skill/main/install.ps1 | iex
```

Manual:

```text
git clone https://github.com/Wenhua-Li/evo-writing-skill.git
```

Copy the repository directory into your agent's skills directory as `evo-write/`.

## 2. First rewrite

```text
Use evo-write. Rewrite this abstract to remove AI tells and defensive writing.
Return only the revised English.
```

Expected behavior:

- no long diagnostic report;
- no invented evidence;
- no unapproved blocked wording or stock contrast patterns;
- substantial paragraph rebuilding when light editing is insufficient;
- necessary scope kept once.

## 3. Hard language gate

EvoWrite reads `skill/references/style/plain-ec-english.md`, `skill/references/style/revision-gate.md`, and `skill/data/prose-gate.json` for every writing task. A blocked expression requires another rewrite before delivery.

To run the deterministic checker yourself, pass the complete candidate text through standard input:

```bash
python tools/scripts/check_prose.py -
```

Use `--json` for structured findings. The process returns 0 for accepted text and 1 when any rule is violated. Narrow technical exceptions, such as the DE term `trial vector`, are defined in the JSON file.

## 4. Draft from notes

```text
Use evo-write. Draft an introduction from these notes:
- Problem: expensive multiobjective optimization
- Method: Gaussian-process-assisted differential evolution
- Goal: reduce exact function evaluations
Do not invent baselines or numerical results.
```

If key information is missing, EvoWrite writes only what is supported and lists at most three missing details after the draft.

## 5. Voice matching

```text
Use evo-write. Match the rhythm and terminology of this author sample:
[paste 2–3 paragraphs]

Now rewrite this passage in the same voice:
[paste target text]
```

Voice matching cannot reintroduce wording blocked by the language gate.

## 6. Audit

```text
Use evo-write in Audit mode. Check this paragraph for unsupported significance, robustness, scalability, efficiency, and optimality claims.
```

Audit returns a report because you explicitly asked for one. Normal rewriting returns only the text. The Revised text in an Audit report must also pass the language gate.
