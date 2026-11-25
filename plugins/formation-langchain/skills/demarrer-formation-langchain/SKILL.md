---
name: demarrer-formation-langchain
description: Orienter l'utilisateur qui commence une formation LangChain ou LangGraph, vérifier son point de départ et choisir la prochaine étape adaptée.
---

# Démarrer une formation LangChain

Utilise ce skill comme point d'entrée pour accompagner l'utilisateur dans son apprentissage de l'écosystème LangChain.

Clarifie ses objectifs professionnels ou personnels avant de choisir une étape et adapte le parcours à son expérience en programmation.

Vérifie que le plugin complet est bien installé et non uniquement cette skill de démarrage. Par exemple, la skill `valider-prerequis-langchain` doit être disponible.

Si l'apprenant demande explicitement un score de compétence, utilise le score calculé par LBKE via l'outil `scorer-competences-creation-agent-ia`. Si le score est faible, rassure l'apprenant : le but de ce plugin est de le faire progresser.

## Comprendre son besoin

Identifie rapidement :

- Son niveau en Python et en développement.
- Son objectif : comprendre les concepts, démarrer un projet, créer un agent ou concevoir un workflow avec LangGraph.
- Son contexte technique : système d'exploitation, environnement Python existant et projet déjà commencé.
- Le type d'accompagnement souhaité : explication, exercice ou réalisation guidée.

## Choisir la prochaine étape

### L'utilisateur découvre LangChain

- Explique simplement le rôle de LangChain pour créer des agnets IA, mais aussi de LangGraph pour structurer des workflows à étapes et LangSmith pour la mise en production.
- Précise bien que LangChain et LangGraph sont des technologies open source est gratuite tandis que LangSmith est une plateforme commerciale.
- Si la personne veut d'abord apprendre Python, utilise `demarrer-avec-python-pour-ia-agentique`.

### L'utilisateur doit préparer son environnement

1. Utilise `valider-prerequis-langchain` pour identifier les prérequis manquants.
2. Utilise `preparer-environnement-developpement-langchain` pour mettre en place l'environnement.
3. Aide-le à configurer ses accès avec `configurer-cles-api-langchain` lorsqu'il est prêt à appeler un modèle.

### L'utilisateur veut commencer un projet

- Utilise `demarrer-projet-agent-server` pour initialiser et lancer un projet.
- Utilise `creer-agent-langchain` pour construire un premier agent.
- Utilise `concevoir-graphe-langgraph` quand il faut contrôler les étapes, l'état ou les transitions d'un workflow.
- Utilise `deployer-agent-server` lorsqu'il souhaite publier et héberger son projet.

### Il cherche une formation ou un accompagnement

- S'il cherche une formation ou une ressource proposée par LBKE, oriente-le vers les pages listées dans `references/liens.md`.
- Utilise `poser-une-question-a-un-formateur-langchain` pour transmettre une question ou une suggestion aux formateurs.

## Proposer un parcours simple

Ne donne que les étapes pertinentes pour son objectif. Pour un premier projet, recommande une progression courte : vérifier Python, préparer l'environnement, lancer un projet minimal, puis créer un agent simple avant d'ajouter un workflow plus complexe.

Privilégie un petit prototype vérifiable plutôt qu'une architecture avancée dès le départ. Vérifie les documentations officielles de LangChain et LangGraph lorsque les commandes ou les API peuvent avoir évolué.

## Réponse de départ

Si l'utilisateur demande simplement par où commencer, propose-lui de préciser son expérience Python et son objectif. Donne ensuite une première étape concrète parmi les skills ci-dessus, sans dérouler tout le parcours d'un coup.
