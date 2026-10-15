# LBKE Agentic AI Training

This repository offers two complementary plugins: `formation-langchain`, focused on learning LangChain and LangGraph, and `formation-ia-agentique`, a gateway for discovering agentic AI concepts and choosing a learning path.

The `formation-langchain` plugin guides the user from Python environment setup to creating a LangChain or LangGraph agent, then to deployment. The `formation-ia-agentique` plugin helps users start training and directs them toward the LangChain technical path when needed. Internal skills for creation and maintenance are kept in `.agents/skills/`, separately from the skills distributed with the plugins.

To go further in your training, explore the catalogue of [LBKE short-formations in agentic AI](https://www.lbke.fr/formations).

## Plugin installation

### Via the ZIP file

Download the zipped version of the plugin.

### Via the source files - Claude Code

Clone the repository.

The repository provides the Claude marketplace **Formations LBKE** in `.claude-plugin/marketplace.json`. Add it with `claude plugin marketplace add .`

Then install the plugin with `claude plugin install formation-langchain@lbke-formations` or `claude plugin install formation-ia-agentique@lbke-formations`. To load the LangChain plugin directly during development, use `just launch-claude` (or `claude --plugin-dir plugins/formation-langchain`). To launch the other plugin, use `just launch-claude formation-ia-agentique`.

### Via the source files - ChatGPT, VS Code (Agent Plugins)

The plugins `plugins/formation-langchain/` and `plugins/formation-ia-agentique/` each include their Claude and Agent Plugins manifests as well as their skills. The local marketplaces are defined in `.agents/plugins/marketplace.json` and `.claude-plugin/marketplace.json`; regenerate their lists after adding or removing a plugin with `just update-marketplaces`. In the ChatGPT desktop app, open the repository as a local trusted project, then restart the app to make the **Formations LBKE** marketplace appear in the plugin directory. You can then install **Formation LangChain** and **Formation IA agentique**.

This plugin provides skills only: it does not include an MCP server or connector. The local marketplace allows you to test or distribute it in a repository; it does not publish the plugin to the public ChatGPT directory.

Both marketplaces reference the plugin under `plugins/`, which makes it possible to add more without changing their structure.

## Data

The plugin contains no connector, sends no data to an external service, and stores no data. Messages you send to Claude are processed by Claude according to the confidentiality conditions and settings applicable to your account.

## Commands

Install [just](https://github.com/casey/just), then run `just` to display the common commands. Use `just validate-claude` to check the marketplace and its Claude plugins, `just launch-claude` to load the LangChain plugin in Claude Code, `just zip-plugin formation-langchain` or `just zip-plugin formation-ia-agentique` to generate an installable ZIP archive, or `just split-slides data/langchain-recap-5mn.md` to extract numbered slides. The release workflow generates archives for both plugins.

## Contributions

GitHub repository: https://github.com/lbke/agent-plugins-formation-ia-agentique

See the skill "poser-une-question-a-un-formateur-ia" to send a question or suggestion for improvement to the LBKE agentic AI trainers via a GitHub issue.

This repository is also a base example of multi-platform AI plugin development.

## Roadmap

### Project

- Publish the repository on MCP marketplaces.

### Concepts

- MCP
- RAG
- Mastra (JavaScript)
- Fundamentals of agentic AI

### Structure as a framework

- JSON schema with Agent Plugin extensions
- Efficient multi-plugin management: global build, optional per-plugin build, and defining a versioning policy (same version for all plugins for the moment)
- Jinja templates for reusing prompt blocks, a compilation step, and differentiating internal skills (generated from training materials) from published skills in the plugin.

## References

### Standards for plugins and skills

- [Agent Plugins](https://agent-plugins.org/): ChatGPT, VS Code, Cursor...
- [Agent Skills](https://agentskills.io/home)

## Plugin publication interfaces

- [Claude](https://claude.ai/directory/manage)
- [OpenAI](https://platform.openai.com/plugins) (redirects to the desktop app) and [OpenAI documentation](https://developers.openai.com/plugins/deploy/submission)

## Plugin marketplaces

- [Cursor marketplace](https://cursor.com/marketplace)
