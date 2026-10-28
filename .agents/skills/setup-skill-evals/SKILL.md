---
name: setup-skill-evals
description: Use this skill to setup an evaluation (evals) for a skill
---

Create at list one example of relevant use case for a skill.
If the skill is connected to other skill, test that:

- the right skill is picked when the difference is subtle (example: testing the user's development environment versus setting up said environment might be different skills)
- related skills are picked together (for instance, evaluate the user's prerequesites and also checking if their environment is properly setup)

**For now, we use Claude as the eval init and eval runner.** This is not a final choice, but keeping the evals compatible with Claude approach makes evaluation easier.

```sh
claude plugin eval init
```

However our skills are not specific to Claude Code, so some part of the proposed Yaml structure do not make sense here (for instance tool activation is not evaluated, we only evaluate the skill).

Stick to the common usages of evals: testing if the skill is triggered by Claude.

## Do not use skill creator format

NOTE: claude skill creator uses another `evals.json` file which is totally different from the `claude plugin eval` format. Since we create a plugin with multiple skills, stick to the plugin approach.

## References

- Claude Plugin Evals (what we use): https://code.claude.com/docs/fr/plugin-evals
- Claude Skill Evals (not used yet but inspiring): https://code.claude.com/docs/fr/skills#run-evals-with-skill-creator

## On GitHub Actions for CI

An action can be setup to run evals automatically, currently **for skills** (NOT PLUGINS) : https://github.com/marketplace/actions/skill-eval
