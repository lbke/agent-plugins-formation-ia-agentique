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

## Conventions for structuring skills files

- Keep user-facing learning content in the plugin `skills/` folder.
- Keep development skills in `.agents/skills/`; general instructions for the repository root belong in `AGENTS.md`.
- For a published skill, follow the expected format: frontmatter `name` and `description` in `SKILL.md`, in the language of the training support.
- Put references in the `references/` folder.
- When a published skill is added or removed, update the README.
- Keep helper scripts minimal, without hidden dependencies, and directly tied to the use case.

## Skill content conventions (for skills in the plugins)

- Write in French (important!)
- The user is designated as "l'apprenant" or "l'utilisateur" and never "l'étudiant".
- These plugins are about teaching and not automating programming of agentic AI apps: skills shoud include references to the doc, explanations, ouverture on how to keep progressing, examples, use case ideas.
- Prefer targeted skills, each representing a concrete use case. Favour using multiple small skills together rather than big skills.
- Keep every useful link (official documentation, LBKE guides and resources, templates) in a `references/` file inside the skill, and point to that file from `SKILL.md` rather than scattering URLs in the body.
- When a skill is modified (renamed, moved, or its content/scope changed), search the repository for its name to find every place it is referenced (README, other skills, manifests, `data/`, scripts) and check that each mention is still accurate after the change.
- Consult the current source documentation rather than reproducing outdated APIs or guarantees from older examples. Add current docs as reference if they are official : coming from LangChain docs, LangChain website, or LBKE.
- Do not add generic server code or infrastructure unless the training content requires it.

## Claude

Claude respects the Agent Skill format standard, but uses its own structure for "plugin.json". The Agent Plugins plugin.json is the source of truth for common fields, which are then replicated in Claude plugin.json through an helper script `sync_claude_plugin`.

## OpenAI

As of 2026/10, OpenAI doesn't accept skills-only plugins anymore.

"Use only letters, numbers, underscores, or hyphens, starting with a letter or number.": this is in regards to the plugin name, it can't be "fr.lbke.plugin-name" for OpenAI (though Agent Plugins standard accepts it) as dots are forbidden.

For an MCP server: the MCP server (so not this repo but the MCP codebase) should have a `public/.well-known/openai-apps-challenge` file (text file but without any extension) with a value provided in OpenAI interface.

To record the demo video: loads the plugin in ChatGPT interface, desktop app is needed for a plugin with MCP : https://chatgpt.com/plugins. Run each positive test case in the video. We hosted a quick demo in the MCP server directly, but using any kind of static file host should work (domain doesn't have to be the official company domain).

## GitHub Copilot

GitHub Copilot reuses the Claude Code marketplace location ([according to this doc](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-marketplace)).

## Goose

Does only support plugin install, not marketplace yet: https://goose-docs.ai/docs/guides/context-engineering/plugins

## Project management scripts

The repository uses `just` as its task runner. It does not have a JavaScript/TypeScript build pipeline or a dedicated test suite; validation mainly concerns the plugins, content, and relevant scripts.

- `just --list`: list available commands.

Internal skills must not be copied into archives or plugin skill folders.

`just` commands may call Python scripts in the `scripts/` directory.

Prefer orchestration in `just` (for example, running a loop across all plugins) and core Python functions for transformations (such as editing JSON).

Doc: https://github.com/casey/just

Use the scripts to audit the project : validate plugin file, run a security audit with SkillSpector...

## Skills over MCP

Skills served directly from the MCP server is an extension of the MCP protocol.

For now, we stick to defining skills as file structured in a plugin, and providing a separate MCP server.

The advantage is that the zip of skills can be exported easily without carrying a complete client/server architecture with MCP.

References:

- https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2640
- https://docs.skybridge.tech/guides/skills
