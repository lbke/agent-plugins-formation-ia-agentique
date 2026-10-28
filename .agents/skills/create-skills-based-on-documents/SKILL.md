---
name: create-skill-based-on-documents
description: Transform training materials into operational skills published in a plugin while following the repository's editorial and technical guidelines.
---

# Transform training support into skills

Use this skill to create or update skills intended for plugin users from the training materials stored in `data/`.

1. Read the slides in order and note their topic and dependencies.
2. Group slides that serve the same operational goal. Create one skill per autonomous use case rather than a general skill that summarises the whole training.
3. Review all slides before concluding: every useful section should either be turned into a skill or identified as a simple title, transition, or content without actionable procedures.
4. Write skills in the language of the support and follow the expected format for Claude (`SKILL.md` with frontmatter `name` and `description`).
5. Provide concrete steps, prerequisites, checks, and common mistakes. Do not present evolving versions, free offers, interfaces, or pricing as permanent facts: invite the user to verify the current provider documentation.
6. Correct technical errors in the support rather than reproducing them. Never invent an execution step, validation, or guarantee.
7. Ignore purely organisational content in the practice guide: dates, schedules, contacts, internal rules, administrative procedures, or logistics sections. Skills should retain only reusable elements such as actions, diagnostics, validations, or setup steps to complete before the course.
8. When a guide contains prerequisite sections, turn them into onboarding skills rather than a simple summary. For example, a guide recommending "set up Python before the training" can become skills such as `demarrer-avec-python-pour-ia-agentique`, `valider-prerequis-langchain`, `tester-environnement-python`, or `preparer-environnement-developpement-langchain`.
9. Each skill must answer a concrete question: "when should this skill be used?", "what are the prerequisites?", "how do we verify it?", and "what common mistakes should be avoided?".
10. Prefer targeted skills at the onboarding and readiness-validation level rather than overly broad summaries. An administrative or schedule guide should not become a generic "all-in-one" skill; the useful content is often distributed across several independent capabilities.

## Example of transformation from a practical guide

From a training guide, the following elements can be extracted:

- technical prerequisites to verify before the training;
- tools needed for the working environment;
- Python basics to master before entering the frameworks;
- minimum checks to decide whether the learner is ready.

In this repository, this becomes skills such as:

- `demarrer-avec-python-pour-ia-agentique`: help a learner install and validate Python before an agentic AI training;
- `valider-prerequis-langchain`: determine whether the learner meets the official prerequisites of the LangChain course (Python basics, HTTP, technical English, accounts to create), with the course page kept as a reference file;
- `tester-environnement-python`: diagnose whether Python, pip and uv are correctly installed, without installing anything;
- `preparer-environnement-developpement-langchain`: actually install and configure each missing tool, used together with the test skill.

This approach avoids copying the administrative structure of the guide and keeps the useful content in a form that can be used by an assistant or a learner.

## Technical rules

- Prefer LangChain in skills unless the user explicitly wants to build LangGraph applications.
- Even for LangChain, use the `langgraph-cli` CLI to create a complete application with a web server and deploy it.
- Consult [LangChain and LangGraph preferences](references/langchain.md) for training-specific details.
- Add a small script only when it automates a check directly tied to the skill's use case. The script should have a documented interface, work without unnecessary dependencies, clearly report errors, never display secrets, and never modify or transmit the user's credentials.
- Published skills live under `plugins/<plugin-name>/skills/<skill-name>/`. Internal development skills live under `.agents/skills/` and should not be copied into the plugin.
- Update the README when adding or removing published skills or user-facing commands.
- Validate the relevant paths, frontmatter, and scripts after each change.
