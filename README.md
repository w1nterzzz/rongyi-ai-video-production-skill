# Rongyi AI Video Production Skill

One Codex Skill for initializing a maintainable AI commercial-video repository.

Its core function is intentionally small:

1. Generate a clear project tree without overwriting existing files.
2. Provide a writable Creative Script Lab.
3. Keep approved `script.md`, production `job.json`, assets, rendering code, and generated media separate.
4. Make human presenters and AI digital twins converge on one FFmpeg and Remotion post-production path.

It does not install dependencies, generate video code, connect APIs, or include media and credentials.

## Install

### One-command install

If Node.js and npm are available, install the Skill for Codex with the open-source [Skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/w1nterzzz/rongyi-ai-video-production-skill/tree/main/rongyi-ai-video-production -g -a codex -y
```

- `-g` installs at user level, so the Skill is available across projects.
- `-a codex` targets Codex.
- `-y` accepts the installation prompts automatically.

### Install with Codex

You can also ask Codex to use its built-in Skill installer:

```text
Use $skill-installer to install:
https://github.com/w1nterzzz/rongyi-ai-video-production-skill/tree/main/rongyi-ai-video-production
```

### Manual install

Codex discovers user-level Skills in `$HOME/.agents/skills`. To install without an installer:

```bash
mkdir -p "$HOME/.agents/skills"
git clone --depth 1 https://github.com/w1nterzzz/rongyi-ai-video-production-skill.git
cp -R rongyi-ai-video-production-skill/rongyi-ai-video-production "$HOME/.agents/skills/"
```

Open Codex and run `/skills` to verify that `rongyi-ai-video-production` appears. If it does not appear, restart Codex once. See the [official OpenAI Skills documentation](https://developers.openai.com/codex/skills) for discovery locations and usage.

## Use

Invoke the installed Skill with:

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
