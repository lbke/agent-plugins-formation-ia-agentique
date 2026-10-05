# Formation IA agentique LBKE

`formation-ia-agentique-lbke` est un plugin Claude conçu pour apprendre les bases et la pratique de l'IA agentique. Ses compétences accompagnent l'utilisateur avec des explications progressives, des exemples concrets et des exercices, tout en mettant l'accent sur les limites des agents et la validation humaine.

Les skills couvrent l'initialisation d'un projet LangGraph, la configuration de clés API, la création d'un agent LangChain simple, la conception d'un graphe LangGraph et le déploiement d'un agent. Les consignes de création et de maintenance du plugin sont conservées dans `authoring/`, séparément des skills distribuées.

## Utilisation

Chargez le plugin dans Claude Code avec `claude --plugin-dir .`. Demandez ensuite à Claude d'expliquer un concept d'IA agentique, de vous aider à concevoir un workflow, de démarrer un projet LangGraph ou de vous proposer un exercice adapté à votre niveau.

## Données

Le plugin ne contient aucun connecteur, n'envoie aucune donnée à un service externe et ne stocke pas de données. Les messages que vous adressez à Claude sont traités par Claude selon les conditions et paramètres de confidentialité applicables à votre compte.

## Commandes

Installez [just](https://github.com/casey/just), puis lancez `just` pour afficher les commandes courantes. Utilisez `just validate` pour vérifier le plugin, `just launch` pour le charger dans Claude Code ou `just split-slides` pour extraire les diapositives numérotées de `data/langchain-recap-5mn.md`.
