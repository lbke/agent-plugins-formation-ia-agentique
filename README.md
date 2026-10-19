# Formation IA agentique LBKE

Le dépôt propose deux plugins complémentaires : `formation-langchain`, centré sur l'apprentissage de LangChain et LangGraph, et `formation-ia-agentique`, un point d'entrée pour découvrir les concepts de l'IA agentique et choisir un parcours.

Le plugin `formation-langchain` accompagne l'utilisateur de la préparation de l'environnement Python à la création d'un agent ou d'un graphe LangGraph, puis au déploiement. Le plugin `formation-ia-agentique` aide à démarrer une formation et oriente vers le parcours technique LangChain si nécessaire. Les skills internes de création et de maintenance sont conservées dans `.agents/skills/`, séparément des skills distribuées avec les plugins.

Pour allez plus loin dans votre formation, découvrez le catalogue de [formations courtes à l'IA agentique de LBKE](https://www.lbke.fr/formations).

## Installation du plugin

### Via le fichier zip

Téléchargez la version zippée du plugin.

### Via les sources - Claude Code

Clonez le dépôt.

Le dépôt fournit la marketplace Claude **Formations LBKE** dans `.claude-plugin/marketplace.json`. Ajoutez-la avec `claude plugin marketplace add .`

Puis installez le plugin avec `claude plugin install formation-langchain@lbke-formations` ou `claude plugin install formation-ia-agentique@lbke-formations`. Pour charger directement le plugin LangChain pendant son développement, utilisez `just launch-claude` (ou `claude --plugin-dir plugins/formation-langchain`). Pour lancer l'autre plugin, utilisez `just launch-claude formation-ia-agentique`.

### Via les sources - ChatGPT, VS Code (Agent Plugins)

Les plugins `plugins/formation-langchain/` et `plugins/formation-ia-agentique/` contiennent chacun leurs manifestes Claude et Agent Plugins ainsi que leurs skills. Les marketplaces locales sont définies dans `.agents/plugins/marketplace.json` et `.claude-plugin/marketplace.json` ; régénérez leurs listes après l'ajout ou le retrait d'un plugin avec `just update-marketplaces`. Dans l'application de bureau ChatGPT, ouvrez le dépôt comme projet local de confiance, puis redémarrez l'application pour faire apparaître la marketplace **Formations LBKE** dans le répertoire des plugins. Vous pourrez alors installer **Formation LangChain** et **Formation IA agentique**.

Ce plugin fournit des skills uniquement : il n'embarque pas de serveur MCP ni de connecteur. La marketplace locale permet de le tester ou de le distribuer dans un dépôt ; elle ne publie pas le plugin dans le répertoire public de ChatGPT.

Les deux marketplaces référencent le plugin sous `plugins/`, ce qui permet d'en ajouter d'autres sans modifier leur structure.

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

- [Agent Plugins](https://agent-plugins.org/) pour ChatGPT, VS Code, Cursor...
- [Agent Skills](https://agentskills.io/home)
- Cursor :  [marketplace](https://cursor.com/marketplace)
- Claude : [documentation](https://code.claude.com/docs/en/plugins/overview),