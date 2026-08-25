from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
INITIALIZER = (
    REPOSITORY_ROOT / "rongyi-ai-video-production/scripts/init_project.py"
)
PRODUCTION_CREATOR = (
    REPOSITORY_ROOT / "rongyi-ai-video-production/scripts/create_production.py"
)
STARTER_ASSETS = REPOSITORY_ROOT / "rongyi-ai-video-production/assets/starter"


def run_script(script: Path, *arguments: str, check: bool = True):
    return subprocess.run(
        [sys.executable, str(script), *arguments],
        check=check,
        capture_output=True,
        text=True,
    )


class ProjectInitializerTests(unittest.TestCase):
    def test_creates_trackable_tree_and_complete_creative_templates(self):
        with tempfile.TemporaryDirectory() as temporary:
            self.assertEqual(list(STARTER_ASSETS.rglob(".gitkeep")), [])
            project = Path(temporary) / "studio"
            run_script(INITIALIZER, str(project), "--name", "Test Studio")

            expected = [
                "01_Content/Creative_Script_Lab/_template/idea.md",
                "01_Content/Creative_Script_Lab/_template/research-notes.md",
                "01_Content/Creative_Script_Lab/_template/script-draft.md",
                "01_Content/Creative_Script_Lab/_template/scene-plan.md",
                "01_Content/Scripts/_template/script.md",
                "02_Assets/Brand/.gitkeep",
                "03_Pipeline/Contracts/.gitkeep",
                "04_Render/Raw/.gitkeep",
                "06_Automation/Jobs/.gitkeep",
            ]
            for relative in expected:
                self.assertTrue((project / relative).is_file(), relative)

            readme = (project / "README.md").read_text(encoding="utf-8")
            self.assertIn("# Test Studio", readme)
            package = json.loads(
                (project / "package.json").read_text(encoding="utf-8")
            )
            self.assertEqual(package["name"], "test-studio")
            for path in project.rglob("*"):
                if path.is_file():
                    self.assertNotIn(
                        "{{",
                        path.read_text(encoding="utf-8"),
                        str(path.relative_to(project)),
                    )

            subprocess.run(
                ["git", "init", "-q"], cwd=project, check=True, capture_output=True
            )
            subprocess.run(
                ["git", "add", "."], cwd=project, check=True, capture_output=True
            )
            tracked = subprocess.run(
                ["git", "ls-files"],
                cwd=project,
                check=True,
                capture_output=True,
                text=True,
            ).stdout.splitlines()
            self.assertIn("02_Assets/Brand/.gitkeep", tracked)
            self.assertIn("04_Render/Raw/.gitkeep", tracked)

    def test_is_idempotent_and_preserves_existing_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "studio"
            run_script(INITIALIZER, str(project))
            custom_readme = "# Keep this content\n"
            (project / "README.md").write_text(custom_readme, encoding="utf-8")

            result = run_script(INITIALIZER, str(project))

            self.assertIn("Created: 0", result.stdout)
            self.assertEqual(
                (project / "README.md").read_text(encoding="utf-8"),
                custom_readme,
            )

    def test_adapts_status_records_for_an_existing_project(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            new_project = root / "new-studio"
            existing_project = root / "existing-studio"
            existing_project.mkdir()
            existing_marker = existing_project / "existing.txt"
            existing_marker.write_text("keep\n", encoding="utf-8")

            run_script(INITIALIZER, str(new_project))
            run_script(INITIALIZER, str(existing_project))

            self.assertEqual(
                existing_marker.read_text(encoding="utf-8"),
                "keep\n",
            )
            for relative in [
                "README.md",
                "00_Project_Management/DECISION_LOG.md",
                "09_Documentation/Setup.md",
            ]:
                new_content = (new_project / relative).read_text(encoding="utf-8")
                existing_content = (existing_project / relative).read_text(
                    encoding="utf-8"
                )
                self.assertNotEqual(new_content, existing_content, relative)


class ProductionCreatorTests(unittest.TestCase):
    def test_creates_one_consistent_production_workspace(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "studio"
            run_script(INITIALIZER, str(project))
            run_script(PRODUCTION_CREATOR, str(project), "rongyi-intro")

            expected = [
                "01_Content/Creative_Script_Lab/rongyi-intro/idea.md",
                "01_Content/Creative_Script_Lab/rongyi-intro/research-notes.md",
                "01_Content/Creative_Script_Lab/rongyi-intro/script-draft.md",
                "01_Content/Creative_Script_Lab/rongyi-intro/scene-plan.md",
                "01_Content/Creative_Briefs/rongyi-intro/brief.md",
                "01_Content/Scripts/rongyi-intro/.gitkeep",
                "06_Automation/Jobs/rongyi-intro/.gitkeep",
            ]
            for relative in expected:
                self.assertTrue((project / relative).is_file(), relative)
            brief = (
                project / "01_Content/Creative_Briefs/rongyi-intro/brief.md"
            ).read_text(encoding="utf-8")
            self.assertIn("## Production ID\n\nrongyi-intro", brief)

    def test_preserves_drafts_and_rejects_invalid_production_ids(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "studio"
            run_script(INITIALIZER, str(project))
            run_script(PRODUCTION_CREATOR, str(project), "rongyi-intro")
            draft = (
                project
                / "01_Content/Creative_Script_Lab/rongyi-intro/script-draft.md"
            )
            custom_draft = "# User draft\n"
            draft.write_text(custom_draft, encoding="utf-8")

            result = run_script(PRODUCTION_CREATOR, str(project), "rongyi-intro")
            invalid = run_script(
                PRODUCTION_CREATOR,
                str(project),
                "Invalid ID",
                check=False,
            )

            self.assertIn("Created: 0", result.stdout)
            self.assertEqual(draft.read_text(encoding="utf-8"), custom_draft)
            self.assertNotEqual(invalid.returncode, 0)
            self.assertIn("production_id must use", invalid.stderr)

    def test_preflights_all_templates_before_creating_any_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "studio"
            run_script(INITIALIZER, str(project))
            missing_template = (
                project / "01_Content/Creative_Briefs/_template/brief.md"
            )
            missing_template.unlink()

            result = run_script(
                PRODUCTION_CREATOR,
                str(project),
                "rongyi-intro",
                check=False,
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("no files were created", result.stderr)
            production_paths = [
                "01_Content/Creative_Script_Lab/rongyi-intro",
                "01_Content/Creative_Briefs/rongyi-intro",
                "01_Content/Scripts/rongyi-intro",
                "06_Automation/Jobs/rongyi-intro",
            ]
            for relative in production_paths:
                self.assertFalse((project / relative).exists(), relative)


if __name__ == "__main__":
    unittest.main()
