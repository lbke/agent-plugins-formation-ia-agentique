# Formation IA agentique LBKE

`formation-ia-agentique` est un plugin Claude conçu pour apprendre les bases et la pratique de l'IA agentique. Ses compétences accompagnent l'utilisateur avec des explications progressives, des exemples concrets et des exercices, tout en mettant l'accent sur les limites des agents et la validation humaine.

Les skills couvrent l'initialisation d'un projet LangGraph, la configuration de clés API, la création d'un agent LangChain simple, la conception d'un graphe LangGraph et le déploiement d'un agent. Les consignes de création et de maintenance du plugin sont conservées dans `authoring/`, séparément des skills distribuées.

## Utilisation

### Claude Code

Le dépôt fournit la marketplace Claude **Formations LBKE** dans `.claude-plugin/marketplace.json`. Ajoutez-la et installez le plugin avec `claude plugin marketplace add .`, puis `claude plugin install formation-ia-agentique@lbke-formations`. Pour charger directement le plugin pendant son développement, utilisez `just launch-claude` (ou `claude --plugin-dir plugins/formation-ia-agentique`). Demandez ensuite à Claude d'expliquer un concept d'IA agentique, de vous aider à concevoir un workflow, de démarrer un projet LangGraph ou de vous proposer un exercice adapté à votre niveau.

### ChatGPT

Le plugin `plugins/formation-ia-agentique/` contient les manifestes Claude et Agent Plugins ainsi que ses skills. La marketplace locale Agent Plugins est définie dans `.agents/plugins/marketplace.json`. Dans l'application de bureau ChatGPT, ouvrez le dépôt comme projet local de confiance, puis redémarrez l'application pour faire apparaître la marketplace **Formations LBKE** dans le répertoire des plugins. Vous pourrez alors installer **Formation IA agentique**.

Ce plugin fournit des skills uniquement : il n'embarque pas de serveur MCP ni de connecteur. La marketplace locale permet de le tester ou de le distribuer dans un dépôt ; elle ne publie pas le plugin dans le répertoire public de ChatGPT.

Les deux marketplaces référencent le plugin sous `plugins/`, ce qui permet d'en ajouter d'autres sans modifier leur structure.

## Données

Le plugin ne contient aucun connecteur, n'envoie aucune donnée à un service externe et ne stocke pas de données. Les messages que vous adressez à Claude sont traités par Claude selon les conditions et paramètres de confidentialité applicables à votre compte.

## Commandes

Installez [just](https://github.com/casey/just), puis lancez `just` pour afficher les commandes courantes. Utilisez `just validate-claude` pour vérifier la marketplace et ses plugins Claude, `just launch-claude` pour charger le plugin dans Claude Code ou `just split-slides data/langchain-recap-5mn.md` pour extraire les diapositives numérotées.
