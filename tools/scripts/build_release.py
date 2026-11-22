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

try:
    from .check_prose import check_text
except ImportError:
    from check_prose import check_text

ROOT = Path(__file__).resolve().parents[2]
EXCLUDED_DIRS = {".git", "build", "dist", "__pycache__", ".pytest_cache"}
EXCLUDED_FILES = {".DS_Store", "Thumbs.db"}
SECRET_NAMES = {".env", ".env.local", "id_rsa", "id_ed25519"}


def iter_public_files(root: Path) -> list[Path]:
    manifest_path = root / "install-manifest.txt"
    if not manifest_path.is_file():
        raise SystemExit("install-manifest.txt is missing.")
    files = []
    seen = set()
    for raw_line in manifest_path.read_text(encoding="utf-8").splitlines():
        entry = raw_line.strip()
        if not entry:
            continue
        rel = Path(entry)
        if rel.is_absolute() or ".." in rel.parts:
            raise SystemExit(f"Manifest paths must stay inside the release root: {entry}")
        if entry in seen:
            raise SystemExit(f"Duplicate manifest entry: {entry}")
        seen.add(entry)
        path = root / rel
        if any(part in EXCLUDED_DIRS for part in rel.parts):
            raise SystemExit(f"Excluded directory listed in manifest: {entry}")
        if path.name in EXCLUDED_FILES or path.suffix == ".pyc":
            raise SystemExit(f"Excluded file listed in manifest: {entry}")
        if path.name in SECRET_NAMES:
            raise SystemExit(f"Refusing to package possible secret file: {entry}")
        if not path.is_file():
            raise SystemExit(f"Manifest file is missing: {entry}")
        files.append(path)
    return files


def after_example_blocks(root: Path) -> list[tuple[Path, str]]:
    blocks = []
    for path in sorted((root / "skill" / "examples").glob("*.md")):
        collecting = False
        current = []
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip() in {"## After", "### After"}:
                if current:
                    blocks.append((path, " ".join(current)))
                current = []
                collecting = True
            elif line.startswith("#"):
                if current:
                    blocks.append((path, " ".join(current)))
                current = []
                collecting = False
            elif collecting and line.startswith("> "):
                current.append(line[2:])
        if current:
            blocks.append((path, " ".join(current)))
    return blocks


def validate_prose_gate(root: Path) -> dict[str, int]:
    lexicon_path = root / "skill" / "data" / "prose-gate.json"
    fixtures_path = root / "tools" / "evals" / "prose-gate-fixtures.json"
    try:
        rules = json.loads(lexicon_path.read_text(encoding="utf-8"))
        fixtures = json.loads(fixtures_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"Cannot load prose-gate validation data: {error}") from error
    for fixture in fixtures["clean"]:
        findings = check_text(fixture["text"], rules)
        if findings:
            raise SystemExit(f"Clean prose-gate fixture {fixture['id']} failed: {findings[:2]}")
    for fixture in fixtures["blocked"]:
        actual = {item["rule"] for item in check_text(fixture["text"], rules)}
        missing = set(fixture["rules"]) - actual
        if missing:
            raise SystemExit(f"Blocked prose-gate fixture {fixture['id']} missed rules: {sorted(missing)}")
    examples = after_example_blocks(root)
    if not examples:
        raise SystemExit("No After examples found for prose-gate validation.")
    for path, text in examples:
        findings = check_text(text, rules)
        if findings:
            raise SystemExit(f"Recommended After example in {path.name} failed: {findings[:2]}")
    return {
        "clean_fixtures": len(fixtures["clean"]),
        "blocked_fixtures": len(fixtures["blocked"]),
        "after_examples": len(examples),
    }


def validate(root: Path, files: list[Path]) -> dict[str, object]:
    skill = root / "SKILL.md"
    if not skill.is_file():
        raise SystemExit("SKILL.md is missing.")
    text = skill.read_text(encoding="utf-8")
    if not re.search(r"^name:\s*evo-write\s*$", text, flags=re.MULTILINE):
        raise SystemExit("SKILL.md must declare name: evo-write.")
    if "description:" not in text.split("---", 2)[1]:
        raise SystemExit("SKILL.md frontmatter must contain a description.")
    required = [
        root / "README.md",
        root / "LICENSE",
        root / "LICENSE-CC-BY-4.0",
        root / "skill" / "data" / "prose-gate.json",
        root / "skill" / "references" / "style" / "plain-ec-english.md",
        root / "skill" / "references" / "style" / "revision-gate.md",
        root / "tools" / "scripts" / "check_prose.py",
        root / "tools" / "evals" / "prose-gate-fixtures.json",
    ]
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
        "prose_gate": validate_prose_gate(root),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--version", default="v0.5.0")
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
