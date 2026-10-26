---
name: demarrer-projet-agent-server
description: Guider la création et le premier lancement d'un projet Python LangChain ou LangGraph exposé par un Agent Server. Utiliser pour choisir uv ou pip, initialiser le projet depuis un template ou le CLI langgraph, installer ses dépendances et démarrer le serveur local de développement.
---

# Démarrer un projet LangChain ou LangGraph avec un Agent Server

Accompagne l'utilisateur jusqu'à un projet local installé et démarré. Demande son système d'exploitation ou son gestionnaire Python préféré seulement si cela change les commandes. Préfère `uv` pour un nouveau projet et adapte les instructions si le projet existe déjà.

Ce skill fonctionne aussi bien pour un projet LangChain que pour un projet LangGraph : dans les deux cas, on utilise le même outil `langgraph-cli` et la même structure de projet (`langgraph.json`, graphe ou agent exposé). Un agent créé avec LangChain (`create_agent`) est lui-même un graphe LangGraph, et se sert exactement de la même façon.

Les liens utiles (documentation du CLI, de l'Agent Server, projet agent-service-toolkit) sont rassemblés dans `references/liens.md`.

## Qu'est-ce qu'un Agent Server ?

L'Agent Server est un serveur web construit autour d'un agent ou d'un graphe LangChain/LangGraph : il expose une API (assistants, threads, runs, streaming, persistance) et il est compatible avec LangSmith Studio, l'interface de développement qui permet de visualiser et tester le graphe. C'est ce que `langgraph dev` lance en local.

Point important à expliquer à l'utilisateur : l'Agent Server fait partie de l'offre LangSmith Deployment de LangChain Inc. ; ce n'est pas la partie open source de LangChain. Le mode développement (`langgraph dev`) est gratuit, mais le déploiement d'un Agent Server en production passe par une offre commerciale. Les bibliothèques LangChain et LangGraph, elles, sont open source et peuvent être intégrées dans n'importe quelle autre application web.

Deux voies sont donc possibles :

- **Agent Server** : pratique pour la formation et le développement, grâce à LangSmith Studio ; c'est la voie suivie par défaut dans ce skill.
- **Intégration full open source** : intégrer LangChain/LangGraph dans sa propre application web (FastAPI, Flask, Django, etc.). Propose à l'utilisateur d'étudier `agent-service-toolkit`, un projet non officiel mais complet qui montre comment déployer soi-même une application LangGraph avec sa partie web (service FastAPI, client, interface Streamlit, Docker Compose), sans Agent Server. Vérifie l'état du projet et sa documentation avant de le recommander comme base.

## Démarrage avec un template

1. Crée ou choisis le répertoire du projet et explique le template retenu. Un template LangGraph existant ou la commande `langgraph new` peuvent servir de point de départ. Vérifie le dépôt exact et sa documentation avant de recommander un template tiers.
2. Si l'utilisateur clone un template, rappelle que le clone apporte son propre historique Git. Vérifie ses remotes avant de proposer de publier le projet ; si la remote du template est appelée `origin`, on peut la renommer `upstream` avant d'ajouter son propre dépôt `origin`.
3. Inspecte `pyproject.toml` et les fichiers de configuration présents avant d'ajouter ou remplacer des dépendances.

## Installer les dépendances

Avec `uv` :

```sh
uv sync
uv run langgraph dev
```

Le CLI peut s'installer séparément selon le projet et la documentation courante :

```sh
uv tool install 'langgraph-cli[inmem]'
```

Alternative avec pip, de préférence dans un environnement virtuel :

```sh
python -m venv .venv
# Active l'environnement avec la commande adaptée au shell.
python -m pip install -e .
python -m pip install 'langgraph-cli[inmem]'
langgraph dev
```

Ne mélange pas silencieusement les installations `uv`, `pip` système et environnements virtuels. Explique quel interpréteur est utilisé et vérifie les commandes disponibles dans la version installée. Si l'environnement Python pose problème, mobilise `tester-environnement-python`.

## Vérifier le premier lancement

- Confirme que l'Agent Server local démarre et indique le port ou l'URL réellement affichés par le CLI ; LangSmith Studio s'ouvre normalement dans le navigateur.
- Le serveur de développement et LangSmith Studio sont des outils de développement ; ne les présente pas comme une configuration de production.
- Si le projet appelle un fournisseur LLM, suis le skill `configurer-cles-api-langchain` avant de diagnostiquer une erreur d'authentification.
- Si l'installation échoue, distingue un problème de version Python, de résolution de dépendances, de CLI absent ou de configuration du graphe avant de proposer un correctif.

## À la suite de ce skill

- Pour écrire l'agent lui-même : `creer-agent-langchain` ou `concevoir-graphe-langgraph`.
- Pour publier et héberger le projet : `deployer-agent-server`.
