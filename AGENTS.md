# Instructions for coding agents

## Internal skills

This repository keeps its internal, reusable development skills in `.agents/skills/`. Before working on plugin content or repository structure, read the relevant internal skill there; in particular, use `creer-skills-depuis-supports` when authoring user-facing skills and `maintenir-ce-depot` for repository conventions.

Internal skills under `.agents/skills/` guide development and are not part of a published plugin. Published skills live under `plugins/<plugin-name>/skills/` and are packaged for end users. Keep these two sets separate: only put learning experiences intended for plugin users in a plugin's `skills/` directory.

Note that `.agents/plugins/marketplace.json` is a published file; it documents the list of published plugins in this repository.

### References - support of local .agents/skills (for developing this codebase)

- [Cursor supports.agents/skills](https://cursor.com/docs/skills#skill-directories)
- [GitHub Copilot supports .agents/skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)

## Structure

This repository is a bundle of Claude and Agent Plugin packages, not a traditional application. Its main content consists of skills, manifests, training materials, and small helper scripts.

## Organisation

- `plugins/<plugin-name>/skills/<skill-name>/SKILL.md`: published skills distributed to users.
- `plugins/<plugin-name>/plugin.json`: Agent Plugins manifest.
- `plugins/<plugin-name>/.claude-plugin/plugin.json`: Claude manifest.
- `.claude-plugin/marketplace.json`: Claude Code marketplace.
- `.agents/plugins/marketplace.json`: Agent Plugins marketplace.
- `.agents/skills/`: internal skills that guide development agents. They are not part of a plugin and are not published.
- `data/`: source material and presentations used to produce and organize the training content.
- `scripts/`: small helper scripts directly related to the content.

Do not confuse internal skills with published ones: a skill for creating skills or maintenance instructions is internal and belongs in `.agents/skills/`. A learning skill intended for learners belongs in `plugins/<plugin-name>/skills/` and will be included in the plugin.

## Conventions

- Keep user-facing learning content in the plugin `skills/` folder.
- Keep development skills in `.agents/skills/`; general instructions for the repository root belong in `AGENTS.md`.
- Prefer targeted skills, each representing a concrete use case.
- For a published skill, follow the expected format: frontmatter `name` and `description` in `SKILL.md`, in the language of the training support.
- When a published skill is added or removed, update the README.
- Consult the current source documentation rather than reproducing outdated APIs or guarantees from older examples.
- Do not add generic server code or infrastructure unless the training content requires it.
- Keep helper scripts minimal, without hidden dependencies, and directly tied to the use case.

## Project management scripts

The repository uses `just` as its task runner. It does not have a JavaScript/TypeScript build pipeline or a dedicated test suite; validation mainly concerns the plugins, content, and relevant scripts.

- `just --list`: list available commands.

Internal skills must not be copied into archives or plugin skill folders.

`just` commands may call Python scripts in the `scripts/` directory.

Prefer orchestration in `just` (for example, running a loop across all plugins) and core Python functions for transformations (such as editing JSON).

Doc: https://github.com/casey/just
