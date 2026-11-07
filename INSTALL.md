# Install EvoWrite

## Recommended

```bash
npx skills add Wenhua-Li/evo-writing-skill
```

## Shell installer

```bash
curl -fsSL https://raw.githubusercontent.com/Wenhua-Li/evo-writing-skill/main/install.sh | bash
```

Options:

```bash
--agent claude|codex|kimi|generic
--dest /path/to/skills
--ref v0.3.3
--force
--dry-run
--doctor
```

## Windows PowerShell

```powershell
iwr https://raw.githubusercontent.com/Wenhua-Li/evo-writing-skill/main/install.ps1 | iex
```

Options:

```powershell
-Agent claude
-Agent codex
-Agent kimi
-Dest "$HOME\.agents\skills"
-Ref v0.3.3
-Force
-DryRun
-Doctor
```

## Default destinations

| Agent | Destination |
|---|---|
| Claude Code | `~/.claude/skills/evo-write` |
| Codex / Kimi Code / generic | `~/.agents/skills/evo-write` |

## Manual installation

```bash
git clone https://github.com/Wenhua-Li/evo-writing-skill.git
```

Copy the repository directory into your agent's skills directory as `evo-write/`. The directory must contain `SKILL.md` directly.

## Verify

Shell:

```bash
./install.sh --doctor --dest ~/.agents/skills
```

PowerShell:

```powershell
.\install.ps1 -Doctor -Dest "$HOME\.agents\skills"
```

Then ask your agent:

```text
Use evo-write. Rewrite this paragraph to remove AI tells and return only the revised English.
```

## Updating

Pin a release for stability:

```bash
./install.sh --ref v0.3.3 --force
```

Or install the latest `main`:

```bash
./install.sh --force
```

The installer backs up an existing `evo-write` directory before replacing it.
