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
- revised English text first;
- necessary scope kept once.

## 3. Draft from notes

```text
Use evo-write. Draft an introduction from these notes:
- Problem: expensive multiobjective optimization
- Method: Gaussian-process-assisted differential evolution
- Goal: reduce exact function evaluations
Do not invent baselines or numerical results.
```

If key information is missing, EvoWrite writes only what is supported and lists at most three missing details after the draft.

## 4. Voice matching

```text
Use evo-write. Match the rhythm and terminology of this author sample:
[paste 2–3 paragraphs]

Now rewrite this passage in the same voice:
[paste target text]
```

## 5. Audit

```text
Use evo-write in Audit mode. Check this paragraph for unsupported significance, robustness, scalability, efficiency, and optimality claims.
```

Audit returns a report because you explicitly asked for one. Normal rewriting returns only the text.
