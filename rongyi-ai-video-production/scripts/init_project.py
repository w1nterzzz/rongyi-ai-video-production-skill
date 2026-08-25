#!/usr/bin/env python3
"""Copy the additive Rongyi AI video production starter tree."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
STARTER_ROOT = SKILL_ROOT / "assets/starter"
SCAFFOLD_MANIFEST = SKILL_ROOT / "assets/scaffold.json"


def package_name(project_name: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "-", project_name.lower()).strip("-")
    return normalized or "ai-video-studio"


def has_existing_user_files(target: Path) -> bool:
    if not target.is_dir():
        return False
    for path in target.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(target)
        if relative.parts[0] == ".git":
            continue
        return True
    return False


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Add a sustainable AI video production tree without overwriting files."
    )
    parser.add_argument("target", help="Project directory to create or complete")
    parser.add_argument("--name", help="Human-facing project name")
    parser.add_argument(
        "--dry-run", action="store_true", help="Print planned changes without writing"
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target = Path(args.target).expanduser().resolve()
    if target == Path(target.anchor) or target == Path.home().resolve():
        raise SystemExit("Refusing to initialize a filesystem root or home directory.")
    if target.exists() and not target.is_dir():
        raise SystemExit(f"Target exists and is not a directory: {target}")
    if not STARTER_ROOT.is_dir():
        raise SystemExit(f"Skill starter assets are missing: {STARTER_ROOT}")
    if not SCAFFOLD_MANIFEST.is_file():
        raise SystemExit(f"Skill scaffold manifest is missing: {SCAFFOLD_MANIFEST}")

    project_name = args.name or target.name
    is_new_project = not has_existing_user_files(target)
    substitutions = {
        "{{PROJECT_NAME}}": project_name,
        "{{PACKAGE_NAME}}": package_name(project_name),
        "{{DEVELOPMENT_PHASE}}": (
            "Phase 1: MVP pipeline — project initialized; implementation not started."
            if is_new_project
            else (
                "Reconcile the existing implementation with this starter roadmap "
                "before recording the current phase."
            )
        ),
        "{{INITIALIZATION_STATE}}": (
            "This new project was initialized with structure and documentation only."
            if is_new_project
            else (
                "This scaffold added only missing structure and documentation. "
                "Review any existing implementation, dependencies, integrations, "
                "and history before changing them."
            )
        ),
        "{{DECISION_STATUS}}": (
            "Accepted as part of new-project initialization."
            if is_new_project
            else (
                "Proposed starter default; confirm against the existing architecture "
                "before implementation."
            )
        ),
    }
    sources = sorted(path for path in STARTER_ROOT.rglob("*") if path.is_file())
    if not sources:
        raise SystemExit(f"Skill starter assets are empty: {STARTER_ROOT}")
    manifest = json.loads(SCAFFOLD_MANIFEST.read_text(encoding="utf-8"))

    created: list[str] = []
    preserved: list[str] = []
    for source in sources:
        relative = source.relative_to(STARTER_ROOT)
        destination = target / relative
        display_path = relative.as_posix()
        if destination.exists():
            preserved.append(display_path)
            continue
        content = source.read_text(encoding="utf-8")
        for marker, value in substitutions.items():
            content = content.replace(marker, value)
        created.append(display_path)
        if not args.dry_run:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(content, encoding="utf-8")

    for directory in manifest["emptyDirectories"]:
        relative = Path(directory) / ".gitkeep"
        destination = target / relative
        display_path = relative.as_posix()
        if destination.exists():
            preserved.append(display_path)
            continue
        created.append(display_path)
        if not args.dry_run:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(
                "# Preserve this directory in Git.\n",
                encoding="utf-8",
            )

    print(f"Target: {target}")
    print(f"Created: {len(created)}")
    for relative in created:
        print(f"  + {relative}")
    print(f"Preserved existing files: {len(preserved)}")
    for relative in preserved:
        print(f"  = {relative}")
    if args.dry_run:
        print("Dry run only; no files were written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
