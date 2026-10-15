# Instructions for coding agents

## Internal skills

This repository keeps its internal, reusable development skills in `.agents/skills/`. Before working on plugin content or repository structure, read the relevant internal skill there; in particular, use `creer-skills-depuis-supports` when authoring user-facing skills and `maintenir-ce-depot` for repository conventions.

Internal skills under `.agents/skills/` guide development and are not part of a published plugin. Published skills live under `plugins/<plugin-name>/skills/` and are packaged for end users. Keep these two sets separate: only put learning experiences intended for plugin users in a plugin's `skills/` directory.

Note that `.agets/plugins/marketplace.json` IS a published file, it documents the list of published plugins in this repo.

### References - support of local .agents/skills (for developing this codebase)

- [Cursor supports.agents/skills](https://cursor.com/docs/skills#skill-directories)
- [GitHub Copilot supports .agents/skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)

## Structure

Le dépôt est un bundle de plugins Claude et Agent Plugins, pas une application traditionnelle. Son contenu principal est constitué des skills, des manifestes, des supports de formation et de petits scripts auxiliaires.

## Organisation

- `plugins/<plugin-name>/skills/<skill-name>/SKILL.md` : skills publiées, distribuées aux utilisateurs.
- `plugins/<plugin-name>/plugin.json` : manifeste Agent Plugins.
- `plugins/<plugin-name>/.claude-plugin/plugin.json` : manifeste Claude.
- `.claude-plugin/marketplace.json` : catalogue Claude Code.
- `.agents/plugins/marketplace.json` : catalogue Agent Plugins.
- `.agents/skills/` : skills internes qui guident les agents de développement. Elles ne font pas partie d'un plugin et ne sont pas publiées.
- `data/` : supports sources et présentations utilisés pour produire ou organiser le contenu de formation.
- `scripts/` : petits scripts d'aide directement liés au contenu.

Ne pas confondre skills internes et skills publiées : une skill de création de skills ou une consigne de maintenance est interne et appartient à `.agents/skills/`. Une skill pédagogique destinée aux apprenants appartient à `plugins/<plugin-name>/skills/` et sera incluse dans le plugin.

## Conventions

- Garder les contenus pédagogiques destinés aux utilisateurs dans le dossier `skills/` du plugin.
- Garder les compétences de développement dans `.agents/skills/` ; les instructions générales à la racine du dépôt appartiennent à `AGENTS.md`.
- Préférer des skills ciblées, chacune représentant un cas d'usage opérationnel.
- Pour une skill publiée, respecter le format attendu : frontmatter `name` et `description` dans `SKILL.md`, dans la langue du support de formation.
- Lorsqu'une skill publiée est ajoutée ou retirée, mettre à jour le README.
- Consulter la documentation source actuelle plutôt que de reproduire des API obsolètes ou des garanties issues d'exemples anciens.
- Ne pas ajouter de code serveur ou d'infrastructure générique, sauf si le contenu de formation l'exige.
- Garder les scripts d'aide minimaux, sans dépendances cachées et directement liés au cas d'usage.

## Validation et commandes

Le dépôt utilise `just` comme lanceur de tâches. Il n'a pas de chaîne de build JavaScript/TypeScript ni de suite de tests dédiée ; la validation porte principalement sur les plugins, les contenus et les scripts concernés.

- `just --list` : lister les commandes disponibles.
- `just validate-claude` : valider le manifeste et la structure des plugins Claude.
- `claude plugin validate .` : valider la marketplace Claude et les plugins qu'elle référence.
- `just launch-claude` : charger le plugin dans une session Claude Code.
- `just split-slides slidev_file` : séparer un support Slidev en extraits Markdown numérotés.
- `python3 scripts/split_slides.py <file>` : exécuter directement le même outil.

Valider les chemins, les manifestes, le frontmatter et les scripts concernés après chaque changement. Les skills internes ne doivent pas être copiées dans les archives ou les dossiers de skills des plugins.

## Ressources à consulter

- `README.md` pour la présentation publique et les commandes disponibles.
- `AGENTS.md` pour l'orientation vers les skills internes.
- `.agents/skills/creer-skills-depuis-supports/SKILL.md` pour transformer les supports en skills publiées.
- La skill publiée concernée sous `plugins/<plugin-name>/skills/` avant de la modifier, car chaque unité pédagogique est autonome.


## Réferences


- [Agent Plugins](https://agent-plugins.org/) : ChatGPT, VS Code, Cursor...
- [Agent Skills](https://agentskills.io/home)
- [Cursor markertlace](https://cursor.com/marketplace)