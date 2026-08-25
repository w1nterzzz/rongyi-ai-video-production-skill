---
name: rongyi-ai-video-production
description: Initialize or repair a maintainable AI commercial-video repository with a clear file tree, a writable Creative Script Lab, approved script and job boundaries, and one FFmpeg/Remotion post-production path for human presenters and AI digital twins. Use when starting an AI video studio or creating a production workspace; skip requests limited to editing one video in a SaaS editor.
---

# Rongyi AI Video Production

Build the workspace before the video. This Skill initializes project structure and content templates; it does not install dependencies, implement rendering, or connect provider APIs.

## Initialize the repository

Inspect the existing repository and preserve its files. For a directory audit, retrofit, or responsibility map, read [references/project-tree.md](references/project-tree.md).

Create only missing files:

```bash
python3 <skill-dir>/scripts/init_project.py <project> --name "Project Name"
```

Use `--dry-run` before applying it to an existing project. The initializer adapts status text for new versus existing repositories and never overwrites a file.

## Create one production workspace

Use one lowercase, hyphenated production ID everywhere:

```bash
python3 <skill-dir>/scripts/create_production.py <project> <production-id>
```

This creates writable idea, research, draft, scene-plan, and Creative Brief files. It leaves approved Script and Production Job directories empty until deliberate promotion and configuration.

## Preserve the boundaries

- `Creative_Script_Lab/<production-id>/` is writable development material and never an automatic render input.
- `Scripts/<production-id>/script.md` is the approved content source of truth.
- `Creative_Briefs/<production-id>/brief.md` stores visual direction and observable acceptance criteria.
- `Jobs/<production-id>/job.json` is the production configuration source of truth.
- FFmpeg owns media processing and delivery conformance. Remotion owns brand and timeline composition.
- Human recordings and AI digital twins use different acquisition adapters, then converge on one normalized presenter contract and shared post-production path.

Keep content data outside rendering logic, configuration outside implementation, and generated media outside Git. Regenerate outputs instead of editing them manually. After render-affecting pipeline changes, run automated checks and a representative render. Record major architecture changes in `DECISION_LOG.md`.

The initialization is complete when the requested tree exists, creative drafts and approved inputs have distinct homes, existing files are unchanged, and the scaffold tests pass.
