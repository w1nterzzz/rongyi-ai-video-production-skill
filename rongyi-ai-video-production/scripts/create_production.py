#!/usr/bin/env python3
"""Create one production's writable content workspace without overwriting files."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


PRODUCTION_ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SKILL_ROOT = Path(__file__).resolve().parents[1]
SCAFFOLD_MANIFEST = SKILL_ROOT / "assets/scaffold.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a production workspace from the project templates."
    )
    parser.add_argument("project", help="Initialized AI video project directory")
    parser.add_argument("production_id", help="Lowercase hyphenated production ID")
    parser.add_argument(
        "--dry-run", action="store_true", help="Print planned changes without writing"
    )
    return parser.parse_args()


def repository_path(project: Path, relative: str) -> Path:
    absolute = (project / relative).resolve()
    if not absolute.is_relative_to(project):
        raise SystemExit(f"Workspace manifest path escapes the project: {relative}")
    return absolute


def create_if_missing(
    target: Path,
    relative: str,
    content: str,
    dry_run: bool,
    created: list[str],
    preserved: list[str],
) -> None:
    if target.exists():
        preserved.append(relative)
        return
    created.append(relative)
    if not dry_run:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")


def main() -> int:
    args = parse_args()
    if not PRODUCTION_ID_PATTERN.fullmatch(args.production_id):
        raise SystemExit(
            "production_id must use lowercase letters, digits, and single hyphens."
        )

    project = Path(args.project).expanduser().resolve()
    if project == Path(project.anchor) or project == Path.home().resolve():
        raise SystemExit("Refusing to use a filesystem root or home directory.")
    if not project.is_dir():
        raise SystemExit(f"Project directory does not exist: {project}")
    if not SCAFFOLD_MANIFEST.is_file():
        raise SystemExit(f"Skill scaffold manifest is missing: {SCAFFOLD_MANIFEST}")

    manifest = json.loads(SCAFFOLD_MANIFEST.read_text(encoding="utf-8"))
    planned_files: list[tuple[Path, str, str]] = []
    missing_templates: list[str] = []
    for template in manifest["productionTemplates"]:
        source_relative = template["source"]
        target_relative = template["target"].format(
            production_id=args.production_id
        )
        source = repository_path(project, source_relative)
        if not source.is_file():
            missing_templates.append(source_relative)
            continue
        content = source.read_text(encoding="utf-8")
        if target_relative.endswith("/brief.md"):
            content = content.replace(
                "## Production ID\n\n",
                f"## Production ID\n\n{args.production_id}\n\n",
                1,
            )
        planned_files.append(
            (
                repository_path(project, target_relative),
                target_relative,
                content,
            )
        )

    if missing_templates:
        raise SystemExit(
            "Missing project templates; no files were created: "
            + ", ".join(missing_templates)
            + ". Run init_project.py to restore them."
        )

    for directory_pattern in manifest["productionEmptyDirectories"]:
        directory_relative = directory_pattern.format(
            production_id=args.production_id
        )
        placeholder_relative = directory_relative + "/.gitkeep"
        planned_files.append(
            (
                repository_path(project, placeholder_relative),
                placeholder_relative,
                "# Preserve this directory in Git.\n",
            )
        )

    created: list[str] = []
    preserved: list[str] = []
    for target, relative, content in planned_files:
        create_if_missing(
            target,
            relative,
            content,
            args.dry_run,
            created,
            preserved,
        )

    print(f"Production: {args.production_id}")
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
