#!/usr/bin/env python3
"""Build and sanity-check the public skill release archive."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRS = {".git", "build", "dist", "__pycache__", ".pytest_cache"}
EXCLUDED_FILES = {".DS_Store", "Thumbs.db"}
SECRET_NAMES = {".env", ".env.local", "id_rsa", "id_ed25519"}


def iter_public_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if path.is_dir():
            continue
        if any(part in EXCLUDED_DIRS for part in rel.parts):
            continue
        if path.name in EXCLUDED_FILES or path.suffix == ".pyc":
            continue
        if path.name in SECRET_NAMES:
            raise SystemExit(f"Refusing to package possible secret file: {rel}")
        files.append(path)
    return files


def validate(root: Path, files: list[Path]) -> dict[str, object]:
    skill = root / "SKILL.md"
    if not skill.is_file():
        raise SystemExit("SKILL.md is missing.")
    text = skill.read_text(encoding="utf-8")
    if not re.search(r"^name:\s*evo-write\s*$", text, flags=re.MULTILINE):
        raise SystemExit("SKILL.md must declare name: evo-write.")
    if "description:" not in text.split("---", 2)[1]:
        raise SystemExit("SKILL.md frontmatter must contain a description.")
    required = [root / "README.md", root / "LICENSE", root / "LICENSE-CC-BY-4.0"]
    missing = [str(p.relative_to(root)) for p in required if not p.is_file()]
    if missing:
        raise SystemExit(f"Missing release files: {', '.join(missing)}")
    forbidden_year_dirs = [str(p.relative_to(root)) for p in files if p.relative_to(root).parts and re.fullmatch(r"20(?:24|25|26)", p.relative_to(root).parts[0])]
    if forbidden_year_dirs:
        raise SystemExit(f"Post-cutoff corpus directories must not be packaged: {forbidden_year_dirs[:3]}")
    oversized = [(str(p.relative_to(root)), p.stat().st_size) for p in files if p.stat().st_size > 10 * 1024 * 1024]
    if oversized:
        raise SystemExit(f"Oversized public files require review: {oversized}")
    return {
        "files": len(files),
        "bytes": sum(p.stat().st_size for p in files),
        "largest_files": sorted(((str(p.relative_to(root)), p.stat().st_size) for p in files), key=lambda x: x[1], reverse=True)[:10],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--version", default="v0.3.1")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    files = iter_public_files(root)
    report = validate(root, files)
    dist = root / "dist"
    dist.mkdir(exist_ok=True)
    archive = dist / f"evo-writing-skill-{args.version}.zip"
    if archive.exists():
        archive.unlink()
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in files:
            rel = path.relative_to(root).as_posix()
            zf.write(path, f"evo-write/{rel}")
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    manifest = {
        "version": args.version,
        "archive": archive.name,
        "sha256": digest,
        **report,
    }
    (dist / "release-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
