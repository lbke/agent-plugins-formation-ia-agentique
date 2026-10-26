# Formation IA agentique LBKE

Le dépôt propose deux plugins complémentaires : `formation-langchain`, centré sur l'apprentissage de LangChain et LangGraph, et `formation-ia-agentique`, un point d'entrée pour découvrir les concepts de l'IA agentique et choisir un parcours.

Le plugin `formation-langchain` accompagne l'utilisateur de la préparation de l'environnement Python à la création d'un agent ou d'un graphe LangGraph, puis au déploiement. Le plugin `formation-ia-agentique` aide à démarrer une formation et oriente vers le parcours technique LangChain si nécessaire. Les skills internes de création et de maintenance sont conservées dans `.agents/skills/`, séparément des skills distribuées avec les plugins.

Pour allez plus loin dans votre formation, découvrez le catalogue de [formations courtes à l'IA agentique de LBKE](https://www.lbke.fr/formations).

Le fichier `AGENTS.md` explique le fonctionnement de la base de code, pour les humains et pour l'IA.

## Installation du plugin


### Applications de bureau Claude, ChatGPT, Goose - installation via le fichier zip 

Le projet respecte le standard Agent Plugins, les skills sont donc installables dans [tous les clients compatibles](https://agent-plugins.org/compatible-clients).

Vous trouverez la dernière version zippée de l'application dans [l'onglet release du dépôt GitHub](https://github.com/lbke/agent-plugins-formation-ia-agentique/releases).

Téléchargez la version zippée du plugin et installez-la dans votre plateforme IA favorite.

### Claude Code via les sources

Clonez le dépôt.

Le dépôt fournit la marketplace Claude **Formations LBKE** dans `.claude-plugin/marketplace.json`. Ajoutez-la avec `claude plugin marketplace add .`

Puis installez le plugin avec `claude plugin install formation-langchain@lbke-formations` ou `claude plugin install formation-ia-agentique@lbke-formations`. Pour charger directement le plugin LangChain pendant son développement, utilisez `just launch-claude` (ou `claude --plugin-dir plugins/formation-langchain`). Pour lancer l'autre plugin, utilisez `just launch-claude formation-ia-agentique`.

### ChatGPT, VS Code, Mistral Vibe (Agent Plugins) via les sources

Les plugins `plugins/formation-langchain/` et `plugins/formation-ia-agentique/` contiennent chacun leurs manifestes Agent Plugins ainsi que leurs skills. Une marketplace locale est définie `.agents/plugins/marketplace.json`.


Ce plugin fournit des skills uniquement : il n'embarque pas de serveur MCP ni de connecteur. La marketplace locale permet de le tester ou de le distribuer dans un dépôt ; elle ne publie pas le plugin dans le répertoire public de ChatGPT.

Les deux marketplaces référencent le plugin sous `plugins/`, ce qui permet d'en ajouter d'autres sans modifier leur structure.

Dans l'application de bureau ChatGPT, ouvrez le dépôt comme projet local de confiance, puis redémarrez l'application pour faire apparaître la marketplace **Formations LBKE** dans le répertoire des plugins. Vous pourrez alors installer **Formation LangChain** et **Formation IA agentique**.

Pour les autres outils, notamment ceux en ligne de commandes, consultez la documentation appropriée (exemple avec [l'agent open source goose](https://goose-docs.ai/docs/guides/context-engineering/plugins) ou [Mistral Vibe](https://docs.mistral.ai/vibe/code/cli/plugins)).

### GitHub Copilot - en ligne de commande

GitHub Copilot ne propose pas de marketplace unifiée à ce jour, il faut donc d'abord configurer la marketplace `lbke-formations` via GitHub, puis installer chaque plugin proposé par LBKE. Quelques commandes suffisent.

```sh
# Installer la marketplace
copilot plugin marketplace add lbke/agent-plugins-formation-ia-agentique
copilot plugin marketplace browse lbke-formations
# Installer les plugins
copilot plugin install formation-langchain@lbke-formations
copilot plugin install ia-agentique@lbke-formations
# Etc. pour chaque plugin
```

[Documentation de l'installation de plugins pour GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-finding-installing) ([documentation équivalente pour VS Code via Copilot](https://code.visualstudio.com/docs/agent-customization/agent-plugins))

### Bonne pratique : menez un audit de sécurité

Installer des skills depuis un dépôt GitHub n'est pas toujours recommandé : vous pouvez procéder vous-mêmes à une analyse de sécurité avec l'outil [SkillSpector](https://github.com/NVIDIA/SkillSpector) de NVidia.

## Données

Le plugin ne contient aucun connecteur, n'envoie aucune donnée à un service externe et ne stocke pas de données. Les messages que vous adressez à Claude sont traités par Claude selon les conditions et paramètres de confidentialité applicables à votre compte.

## Commandes

Installez [just](https://github.com/casey/just), puis lancez `just` pour afficher les commandes courantes. Utilisez `just validate-claude` pour vérifier la marketplace et ses plugins Claude, `just launch-claude` pour charger le plugin LangChain dans Claude Code, `just zip-plugin formation-langchain` ou `just zip-plugin formation-ia-agentique` pour générer une archive ZIP installable, ou `just split-slides data/langchain-recap-5mn.md` pour extraire les diapositives numérotées. Le workflow de release génère les archives des deux plugins.

## Contributions

Dépôt GitHub : https://github.com/lbke/agent-plugins-formation-ia-agentique

Voir la skill "poser-une-question-a-un-formateur-ia" pour transmettre une question ou suggestion d'amélioration aux formateurs IA agentique de LBKE, via un ticket GitHub.

Ce dépôt constitue aussi un exemple de base de code pour développer des plugins IA multi-plateformes.

## Roadmap

### Projet

- Publier le dépôt sur les marketplaces MCP.

### Concepts

- MCP
- RAG
- Mastra (JavaScript)
- Fondamentaux de l'agentique

### Structuration sous forme de framework

- Schéma JSON avec les extensions Agent Plugin
- Gestion efficace multi-plugins : build global, build par plugin optionnel, définir une politique de versionnage (même version pour tous les plugins pour le moment)
- Templates jinja pour a réutilisation de blocs de prompts, étape de compilation, différenciation des skills internes (génération de skills à partir de support de formation) et publiées dans le plugin.

## Réferences

### Standards pour la structure des plugins et des skills

- [Agent Plugins](https://agent-plugins.org/) pour ChatGPT, VS Code, Cursor...
- [Agent Skills](https://agentskills.io/home)

## Documentation technique

- Claude : [documentation](https://code.claude.com/docs/en/plugins/overview), [reference plugin.json](https://code.claude.com/docs/en/plugins/manifest-reference)
- VSCode : [documentation Agent Plugin](https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference)
- GitHub Copilot: [installation et gestion des marketplace](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-finding-installing), [créer une marketplace et l'installer](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-marketplace) (format identique à Claude Code), [créer un plugin (format agent plugin)](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating) 
- Goose : [Agent skills](https://goose-docs.ai/docs/guides/context-engineering/using-skills/), [plugins](https://goose-docs.ai/docs/guides/context-engineering/plugins), [abandon du support d'un registre spécifique](https://github.com/aaif-goose/goose/discussions/10830), [making goose marketplace install easier](https://github.com/aaif-goose/goose/issues/13150)

## Interfaces de publication de plugins

- [Publication pour Claude](https://claude.ai/directory/manage)
- [Publication pour OpenAI](https://platform.openai.com/plugins) (bouton "upload") et [Documentation pour OpenAI](https://developers.openai.com/plugins/deploy/submission), [guidelines des plugins](https://developers.openai.com/plugins/plugin-guidelines)

## Marketplaces de plugins

- [Cursor marketplace](https://cursor.com/marketplace)
- [Registre officiel MCP](https://github.com/modelcontextprotocol/registry)
