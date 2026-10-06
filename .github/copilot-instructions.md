# Copilot instructions for this repository

## Purpose and scope

This repository packages a Claude/Agent Plugins learning experience for “Formation IA agentique”. The project is not a traditional application with a package.json or test suite; it is a plugin bundle that exposes skills to Claude and other agent platforms.

The repository supports multiple plugins. The current plugin lives in `plugins/formation-ia-agentique/`. The key user-facing assets are:

- `plugins/<plugin-name>/skills/<skill-name>/SKILL.md`: individual learning experiences distributed to users.
- `plugins/<plugin-name>/plugin.json`: manifest used by the Agent Plugins standard.
- `plugins/<plugin-name>/.claude-plugin/plugin.json`: Claude-specific plugin manifest.
- `.claude-plugin/marketplace.json`: Claude Code marketplace catalog.
- `.agents/plugins/marketplace.json`: Agent Plugins marketplace catalog.
- `data/`: source material and slide decks used to produce/organize the training content.
- `authoring/`: internal documentation for maintainers; this content is not user-facing skill material.
- `scripts/`: small helper scripts tied to the learning content.

## Build, validation, and commands

This repository uses `just` as the main task runner.

- `just --list` — list available commands.
- `just validate-claude` — validate the plugin manifest and the Claude plugin layout.
- `claude plugin validate .` — validate the Claude marketplace and its listed plugins directly.
- `just launch-claude` — load the plugin in a Claude Code session.
- `just split-slides slidev_file` — split a slide deck into numbered Markdown snippets. Example: `just split-slides data/langchain-recap-5mn.md`.
- `python3 scripts/split_slides.py <file>` — direct execution of the same splitting helper.

There is no JavaScript/TypeScript build pipeline, no package manager manifest, and no dedicated unit/integration test suite in this repo. Validation is plugin-centric and content-centric rather than code-test-driven.

## High-level architecture

The repository is organized around a content-to-plugin pipeline:

1. Training materials live in `data/` and are transformed into reusable instructional units.
2. Each operational learning unit is authored as a standalone skill under `plugins/<plugin-name>/skills/<skill-name>/SKILL.md`.
3. Each plugin has manifests for both formats, and root marketplace manifests expose the plugin catalog to each target agent environment:
   - `.agents/plugins/marketplace.json` for the Agent Plugins / ChatGPT ecosystem.
   - `.claude-plugin/marketplace.json` for Claude Code.
4. Supporting guidance for maintainers remains in `authoring/` so it does not leak into the end-user skill bundle.
5. Small utilities in `scripts/` automate repetitive content tasks, such as splitting slide files into segment files.

The important design constraint is that the repo is authoring-heavy, not code-heavy: the “application” is the skill content plus manifests, not a runtime service or a web app.

## Key conventions

- Keep user-facing instructional material under each plugin's `skills/` directory only. Internal authoring material belongs in `authoring/`.
- Prefer focused skill files, not one giant catch-all skill. Each skill should represent a single operational use case.
- Preserve the expected SKILL format: frontmatter must include `name` and `description` and the file should be written in the language of the training material.
- When adding or removing skills, update the root README so the user-facing surface stays accurate.
- Validate the affected plugin paths and scripts after changes. This repo treats validation as part of authoring discipline, not as an optional later step.
- Use the source documentation rather than copying stale APIs or outdated platform assumptions. The repo explicitly warns against reproducing outdated declarations or “guarantees” from old examples.
- Do not place server-side runtime code or generic app infrastructure in this repo unless the training content specifically requires it. The project’s structure is intentionally lightweight and content-focused.
- Keep helper scripts minimal and directly tied to the skill/use case they support; avoid adding broad tooling or hidden dependencies.

## Documentation to consult when changing the repo

- `README.md` for user-facing overview and supported commands.
- `authoring/INSTRUCTIONS.md` for maintainer workflow and plugin-authoring rules.
- `authoring/langchain.md` for training-specific preferences and constraints around LangChain/LangGraph usage.
- An individual `plugins/<plugin-name>/skills/<name>/SKILL.md` file when modifying or creating a skill, because each skill is authored as a self-contained learning unit.

## Practical guidance for Copilot

When working in this repository:

- Treat changes as content and plugin metadata updates, not backend code changes.
- Prefer small, targeted edits that keep the manifest and skill structure consistent.
- Verify plugin validity with `just validate-claude` or `claude plugin validate .` after changing manifests or skill files.
- When creating new training modules, keep them self-contained and use the repository’s existing pattern of one purpose per skill folder.
- Reuse the naming and folder conventions already established by the current skills instead of inventing a new organizational pattern.
