# Repository Instructions

## Project overview

This repository is a long-lived AI commercial-video production system. Human recordings and AI digital twins use different acquisition paths, then share one FFmpeg and Remotion post-production pipeline.

## Directory responsibilities

- `00_Project_Management/` owns roadmap, tasks, version, and architecture decisions.
- `01_Content/Creative_Script_Lab/` is the writable idea, research, draft, and scene-planning area.
- `01_Content/Scripts/` owns approved `script.md` files; rendering consumes no Lab draft directly.
- `01_Content/Creative_Briefs/` owns visual direction and observable acceptance criteria.
- `02_Assets/` owns reusable, rights-tracked source assets.
- `03_Pipeline/` owns FFmpeg, Remotion, subtitle, component, and media-contract implementation.
- `04_Render/` owns raw, intermediate, and final generated media.
- `05_AI_Avatar/` owns provider-specific acquisition boundaries and prompts.
- `06_Automation/Jobs/` owns production `job.json` configuration; other automation directories own orchestration, tests, and logs.
- `07_Platform/`, `08_Analytics/`, and `09_Documentation/` own delivery, measurement, and durable documentation respectively.

## Coding and production rules

- Treat `01_Content/Scripts/<production-id>/script.md` as the approved content source of truth.
- Treat `06_Automation/Jobs/<production-id>/job.json` as the production configuration source of truth.
- Do not mix content data or Creative Brief requirements with rendering logic.
- Keep configuration and versioned contracts separate from implementation.
- Normalize human and AI presenters to one versioned media contract before composition.
- FFmpeg owns media processing; Remotion owns brand and timeline composition.
- Do not manually modify generated media, intermediate outputs, or finalized run evidence. Change their sources or generators and create a new run.
- Keep generated media, logs, credentials, and environment files out of Git.
- After modifying pipeline code or render-affecting configuration, run automated checks and render a representative video before declaring completion.
- Record major architecture decisions and migrations in `00_Project_Management/DECISION_LOG.md`.
- Preserve unrelated user changes and never overwrite existing content during scaffolding.
