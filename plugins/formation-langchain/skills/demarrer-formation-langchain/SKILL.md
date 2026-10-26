---
name: demarrer-formation-langchain
description: Orienter l'utilisateur qui commence une formation LangChain ou LangGraph, vérifier son point de départ et choisir la prochaine étape adaptée.
---

# Démarrer une formation LangChain

Utilise ce skill comme point d'entrée pour accompagner l'utilisateur dans son apprentissage de LangChain et LangGraph. Clarifie son objectif avant de choisir une étape et adapte le parcours à son expérience en programmation.

## Comprendre son besoin

Identifie rapidement :

- Son niveau en Python et en développement.
- Son objectif : comprendre les concepts, démarrer un projet, créer un agent ou concevoir un workflow avec LangGraph.
- Son contexte technique : système d'exploitation, environnement Python existant et projet déjà commencé.
- Le type d'accompagnement souhaité : explication, exercice ou réalisation guidée.

## Choisir la prochaine étape

### Il découvre LangChain ou LangGraph

- Explique simplement le rôle de LangChain et la place de LangGraph pour structurer des workflows à étapes.
- Si la personne veut d'abord apprendre Python, utilise `demarrer-avec-python-pour-ia-agentique`.
- Pour consolider les concepts d'IA agentique, utilise `enseigner-ia-agentique`.

### Il doit préparer son environnement

1. Utilise `valider-pre-requis-langchain` pour identifier les prérequis manquants.
2. Utilise `preparer-environnement-developpement-langchain` pour mettre en place l'environnement.
3. Aide-le à configurer ses accès avec `configurer-cles-api-langchain` lorsqu'il est prêt à appeler un modèle.

### Il veut commencer un projet

- Utilise `demarrer-projet-agent-server` pour initialiser et lancer un projet.
- Utilise `creer-agent-langchain` pour construire un premier agent.
- Utilise `concevoir-graphe-langgraph` quand il faut contrôler les étapes, l'état ou les transitions d'un workflow.
- Utilise `deployer-agent-server` lorsqu'il souhaite publier et héberger son projet.

### Il cherche une formation ou un accompagnement

- Utilise `rechercher-formation-ia-agentique` s'il cherche une formation ou une ressource proposée par LBKE.
- Utilise `poser-une-question-a-un-formateur-ia` pour transmettre une question ou une suggestion aux formateurs.

## Proposer un parcours simple

Ne donne que les étapes pertinentes pour son objectif. Pour un premier projet, recommande une progression courte : vérifier Python, préparer l'environnement, lancer un projet minimal, puis créer un agent simple avant d'ajouter un workflow plus complexe.

Privilégie un petit prototype vérifiable plutôt qu'une architecture avancée dès le départ. Vérifie les documentations officielles de LangChain et LangGraph lorsque les commandes ou les API peuvent avoir évolué.

## Réponse de départ

Si l'utilisateur demande simplement par où commencer, propose-lui de préciser son expérience Python et son objectif. Donne ensuite une première étape concrète parmi les skills ci-dessus, sans dérouler tout le parcours d'un coup.
