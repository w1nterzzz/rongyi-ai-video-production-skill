# Architecture

## Source-of-truth boundaries

| Concern | Authoritative location |
| --- | --- |
| Creative development | `01_Content/Creative_Script_Lab/<production-id>/` |
| Approved content | `01_Content/Scripts/<production-id>/script.md` |
| Creative direction | `01_Content/Creative_Briefs/<production-id>/brief.md` |
| Executable configuration | `06_Automation/Jobs/<production-id>/job.json` |
| Reusable source assets | `02_Assets/` |
| Rendering implementation | `03_Pipeline/` |
| Generated media and run-local work | `04_Render/` |

## Shared post-production path

```text
Human capture -> inspect/key/normalize ----------+
                                                   +-> normalized presenter -> Remotion -> FFmpeg -> output
Digital twin -> provider fetch/normalize --------+
```

Acquisition adapters may differ. Everything after the normalized presenter boundary is shared. A new provider must not introduce another composition or delivery pipeline.

## Tool ownership

- FFmpeg owns probing, chroma keying, media conversion, normalization, muxing, delivery conformance, and measurable media checks.
- Remotion owns programmable scene layout, brand elements, timeline composition, and visual templates.
- Codex owns repository maintenance, safe automation, tests, migrations, and documentation.

Runtime measurements and generated output are evidence, not configuration. Keep them outside `job.json` and do not edit them manually.
