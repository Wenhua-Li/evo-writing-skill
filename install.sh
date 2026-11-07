#!/usr/bin/env bash
set -euo pipefail

REPO="Wenhua-Li/evo-writing-skill"
SKILL_NAME="evo-write"
AGENT="generic"
DEST=""
REF="v0.4.0"
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
  --ref REF        Git ref or release tag to install (default: v0.3.2)
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

download_with_retries() {
  curl -fL --retry 5 --retry-all-errors --retry-delay 2 --connect-timeout 20 "$@"
}

download_from_manifest() {
  local tmp="$1"
  local base_url="https://raw.githubusercontent.com/$REPO/$REF"
  local src="$tmp/repo"
  mkdir -p "$src"
  echo "Downloading EvoWrite file manifest from $base_url..." >&2
  download_with_retries -o "$tmp/manifest.txt" "$base_url/install-manifest.txt"
  while IFS= read -r rel; do
    [ -z "$rel" ] && continue
    mkdir -p "$src/$(dirname "$rel")"
    download_with_retries -o "$src/$rel" "$base_url/$rel"
  done < "$tmp/manifest.txt"
  printf '%s' "$src"
}

download_remote_source() {
  local tmp="$1"
  if [ "$REF" != "main" ]; then
    local zip_url="https://github.com/$REPO/releases/download/$REF/evo-writing-skill-$REF.zip"
    local archive="$tmp/evo-write.zip"
    echo "Downloading EvoWrite release archive..." >&2
    if download_with_retries -o "$archive" "$zip_url"; then
      mkdir -p "$tmp/extract"
      if command -v unzip >/dev/null 2>&1; then
        unzip -q "$archive" -d "$tmp/extract"
      else
        python -m zipfile -e "$archive" "$tmp/extract"
      fi
      if [ -f "$tmp/extract/evo-write/SKILL.md" ]; then
        printf '%s' "$tmp/extract/evo-write"
        return 0
      fi
    fi
    echo "Release archive unavailable; falling back to manifest download." >&2
  fi
  download_from_manifest "$tmp"
}

SOURCE_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" 2>/dev/null && pwd || true)"
if [ -n "$SOURCE_DIR" ] && [ -f "$SOURCE_DIR/SKILL.md" ]; then
  SRC="$SOURCE_DIR"
else
  TMP="$(mktemp -d)"
  trap 'rm -rf "$TMP"' EXIT
  SRC="$(download_remote_source "$TMP")"
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
