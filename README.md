# Rongyi AI Video Production Skill

One Codex Skill for initializing a maintainable AI commercial-video repository.

Its core function is intentionally small:

1. Generate a clear project tree without overwriting existing files.
2. Provide a writable Creative Script Lab.
3. Keep approved `script.md`, production `job.json`, assets, rendering code, and generated media separate.
4. Make human presenters and AI digital twins converge on one FFmpeg and Remotion post-production path.

It does not install dependencies, generate video code, connect APIs, or include media and credentials.

## Use

Install the `rongyi-ai-video-production/` folder as a Codex Skill, then invoke it with:

```text
Use $rongyi-ai-video-production to initialize my AI video studio.
```

The deterministic helpers can also run directly:

```bash
python3 rongyi-ai-video-production/scripts/init_project.py ./My-Studio --name "My Studio"
python3 rongyi-ai-video-production/scripts/create_production.py ./My-Studio first-video
```

Both commands support additive, non-overwriting operation. Use `--dry-run` before modifying an existing project.

## Why the repository stays small

The Skill stores only real output templates. Empty project directories are listed once in `assets/scaffold.json`; the initializer creates their `.gitkeep` files when needed. The repository therefore does not carry dozens of duplicate placeholder files.

```text
rongyi-ai-video-production/
├── SKILL.md
├── assets/
│   ├── scaffold.json
│   └── starter/          # actual project documents and creative templates
├── scripts/
│   ├── init_project.py
│   └── create_production.py
└── references/
    └── project-tree.md
```

Run validation with:

```bash
python3 -m unittest discover -s tests -v
```

## License

MIT
