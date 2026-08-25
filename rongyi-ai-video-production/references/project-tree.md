# Project Tree

Read this reference when initializing, reorganizing, or auditing an AI video production repository.

## Structure

```text
ai-video-studio/
├── AGENTS.md
├── README.md
├── CHANGELOG.md
├── .gitignore
├── package.json
├── 00_Project_Management/
│   ├── ROADMAP.md
│   ├── TODO.md
│   ├── DECISION_LOG.md
│   └── VERSION.md
├── 01_Content/
│   ├── Creative_Script_Lab/
│   │   ├── _template/
│   │   └── <production-id>/
│   ├── Scripts/
│   │   ├── _template/script.md
│   │   └── <production-id>/script.md
│   ├── Creative_Briefs/
│   ├── Topics/
│   ├── Research/
│   └── Published/
├── 02_Assets/
│   ├── Registry/
│   ├── Brand/
│   ├── Avatar/{Human,Providers}/
│   ├── Background/
│   ├── Music/
│   ├── Fonts/
│   └── Templates/
├── 03_Pipeline/{Contracts,FFmpeg,Remotion,Subtitle,Components}/
├── 04_Render/{Raw,Processing,Output}/
├── 05_AI_Avatar/{Providers,API,Prompts}/
├── 06_Automation/{Production,Scripts,Jobs,Tests,Logs}/
├── 07_Platform/
├── 08_Analytics/{Metrics,Reports,Experiments}/
├── 09_Documentation/{Architecture.md,Workflow.md,Setup.md}
└── 10_Backup/
```

Numeric prefixes keep lifecycle areas stable. Add provider- or platform-specific children only when they have real configuration or implementation. The scaffold manifest stores empty-directory paths once; the initializer generates `.gitkeep` files in the target project.

## Responsibilities

- `01_Content` contains creative development, approved words, and briefs; it contains no renderer implementation.
- `02_Assets` contains reusable source assets and rights records; it contains no run-local intermediates.
- `03_Pipeline` contains media contracts and reusable FFmpeg/Remotion implementation.
- `04_Render` contains acquired source, generated processing files, and final output; these files stay outside Git.
- `05_AI_Avatar` contains provider-specific acquisition only. Shared composition remains in `03_Pipeline`.
- `06_Automation/Jobs` contains desired production configuration. Logs and runtime evidence stay separate.
- `07_Platform` adapts an approved master for destinations without becoming the content source.
- `08_Analytics` records outcomes without changing historical production files.

## Creative promotion

Develop `idea.md`, `research-notes.md`, `script-draft.md`, and `scene-plan.md` under one production ID. When the content owner approves the draft:

1. Create `01_Content/Scripts/<production-id>/script.md` from the approved words.
2. Complete the matching Creative Brief with visual and presenter acceptance criteria.
3. Create or update `06_Automation/Jobs/<production-id>/job.json` against its versioned schema.
4. Keep prior drafts as development history; rendering reads only the approved Script.

## Existing repositories

Inventory current files before moving anything. Add missing paths first, then update references and tests before moving source-of-truth files. Preserve existing work and keep the migration separate from unrelated changes.

The tree is unambiguous when one production ID resolves to one writable Lab folder, one approved Script, one Creative Brief, and one Production Job.
