# Instructions for coding agents

## Internal skills

This repository keeps its internal, reusable development skills in `.agents/skills/`. Before working on plugin content or repository structure, read the relevant internal skill there; in particular, use `creer-skills-depuis-supports` when authoring user-facing skills and `maintenir-ce-depot` for repository conventions.

Internal skills under `.agents/skills/` guide development and are not part of a published plugin. Published skills live under `plugins/<plugin-name>/skills/` and are packaged for end users. Keep these two sets separate: only put learning experiences intended for plugin users in a plugin's `skills/` directory.

Note that `.agets/plugins/marketplace.json` IS a published file, it documents the list of published plugins in this repo.

### References

- [Cursor supports.agents/skills](https://cursor.com/docs/skills#skill-directories)
- [GitHub Copilot supports .agents/skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)
