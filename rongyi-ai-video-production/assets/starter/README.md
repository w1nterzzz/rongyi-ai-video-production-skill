# {{PROJECT_NAME}}

A scalable AI production workspace for short-form commercial videos.

## Current phase

**{{DEVELOPMENT_PHASE}}**

For a new project, the first implementation goal is one verified path from human-recorded source media through FFmpeg and Remotion to a final MP4. The starter itself adds no Remotion components, FFmpeg commands, provider integrations, or runtime dependencies.

## Sources of truth

- Develop ideas and drafts in `01_Content/Creative_Script_Lab/<production-id>/`.
- Promote approved content to `01_Content/Scripts/<production-id>/script.md`. This file is the content source of truth.
- Store executable production configuration in `06_Automation/Jobs/<production-id>/job.json`. This file is the configuration source of truth.
- Keep production-specific visual direction and acceptance criteria in `01_Content/Creative_Briefs/<production-id>/brief.md`.

## Overall architecture

```text
Human recording -> FFmpeg normalization ---------+
                                                    +-> Remotion composition -> FFmpeg delivery -> final MP4
AI digital twin -> provider normalization --------+

Creative Script Lab -> approved script.md -> job.json
Creative Brief ------------------------------^---- human creative review
```

Human presenters and AI digital twins use different acquisition methods, then converge on the same normalized presenter contract and post-production pipeline. FFmpeg owns media processing and delivery conformance. Remotion owns programmable brand and timeline composition.

## Future roadmap

1. MVP human-presenter pipeline.
2. Automatic subtitles.
3. AI digital-twin integration.
4. Codex production automation.
5. Commercial production system.

See `00_Project_Management/ROADMAP.md` for phase goals and `09_Documentation/` for architecture, workflow, and setup boundaries.
