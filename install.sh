#!/usr/bin/env bash
set -euo pipefail

REPO="Wenhua-Li/evo-writing-skill"
SKILL_NAME="evo-write"
AGENT="generic"
DEST=""
REF="main"
FORCE=0
DRY_RUN=0
DOCTOR=0

usage() {
  cat <<'USAGE'
Install EvoWrite for an Agent Skills environment.

Usage: install.sh [options]

Options:
  --agent NAME     claude | codex | kimi | generic (default: generic)
  --dest DIR       Skills directory (overrides --agent)
  --ref REF        Git ref to install (default: main)
  --force          Replace an existing evo-write installation after backup
  --dry-run        Show what would happen without changing files
  --doctor         Validate an existing installation
  -h, --help       Show this help
USAGE
}

while [ $# -gt 0 ]; do
  case "$1" in
    --agent) AGENT="${2:?}"; shift 2 ;;
    --dest) DEST="${2:?}"; shift 2 ;;
    --ref) REF="${2:?}"; shift 2 ;;
    --force) FORCE=1; shift ;;
    --dry-run) DRY_RUN=1; shift ;;
    --doctor) DOCTOR=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage >&2; exit 2 ;;
  esac
done

if [ -z "$DEST" ]; then
  case "$AGENT" in
    claude) DEST="$HOME/.claude/skills" ;;
    codex|kimi|generic) DEST="$HOME/.agents/skills" ;;
    *) echo "Unsupported agent: $AGENT" >&2; exit 2 ;;
  esac
fi

TARGET="$DEST/$SKILL_NAME"

if [ "$DOCTOR" -eq 1 ]; then
  if [ ! -f "$TARGET/SKILL.md" ]; then
    echo "EvoWrite is not installed at $TARGET" >&2
    exit 1
  fi
  grep -q '^name: evo-write$' "$TARGET/SKILL.md"
  echo "EvoWrite installation looks valid: $TARGET"
  exit 0
fi

SOURCE_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" 2>/dev/null && pwd || true)"
if [ -n "$SOURCE_DIR" ] && [ -f "$SOURCE_DIR/SKILL.md" ]; then
  SRC="$SOURCE_DIR"
else
  TMP="$(mktemp -d)"
  trap 'rm -rf "$TMP"' EXIT
  echo "Downloading $REPO@$REF..."
  curl -fsSL "https://github.com/$REPO/archive/$REF.tar.gz" -o "$TMP/repo.tar.gz"
  tar -xzf "$TMP/repo.tar.gz" -C "$TMP"
  SRC="$(find "$TMP" -mindepth 1 -maxdepth 1 -type d | head -n 1)"
fi

if [ ! -f "$SRC/SKILL.md" ]; then
  echo "Could not find SKILL.md in the source." >&2
  exit 1
fi
if ! grep -q '^name: evo-write$' "$SRC/SKILL.md"; then
  echo "SKILL.md does not declare name: evo-write" >&2
  exit 1
fi

if [ "$DRY_RUN" -eq 1 ]; then
  echo "Would install from: $SRC"
  echo "Would install to:   $TARGET"
  [ -e "$TARGET" ] && echo "Existing installation would be backed up." || true
  exit 0
fi

mkdir -p "$DEST"
if [ -e "$TARGET" ]; then
  if [ "$FORCE" -ne 1 ]; then
    echo "$TARGET already exists. Re-run with --force to replace it." >&2
    exit 1
  fi
  BACKUP="$TARGET.backup.$(date +%Y%m%d%H%M%S)"
  mv "$TARGET" "$BACKUP"
  echo "Existing installation backed up to $BACKUP"
fi

mkdir -p "$TARGET"
if command -v rsync >/dev/null 2>&1; then
  rsync -a --exclude '.git' --exclude 'build' --exclude 'dist' --exclude '__pycache__' "$SRC/" "$TARGET/"
else
  (cd "$SRC" && tar --exclude='./.git' --exclude='./build' --exclude='./dist' --exclude='./__pycache__' -cf - .) | (cd "$TARGET" && tar -xf -)
fi

grep -q '^name: evo-write$' "$TARGET/SKILL.md"
echo "EvoWrite installed to $TARGET"
echo "Try: Use evo-write. Rewrite this paragraph to remove AI tells and return only the revised English."
