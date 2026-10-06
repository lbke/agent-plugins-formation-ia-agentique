---
name: demarrer-projet-langgraph
description: Guider la création et le premier lancement d'un projet Python LangGraph. Utiliser pour choisir uv ou pip, initialiser le projet depuis un template ou le CLI, installer ses dépendances et démarrer le serveur local de développement.
---

# Démarrer un projet LangChain ou LangGraph avec le langgraph-cli

Accompagne l'utilisateur jusqu'à un projet local installé et démarré. Demande son système d'exploitation ou son gestionnaire Python préféré seulement si cela change les commandes. Préfère `uv` pour un nouveau projet et adapte les instructions si le projet existe déjà.

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

Le CLI peut s'installer séparément selon le projet et la documentation LangGraph courante :

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

Ne mélange pas silencieusement les installations `uv`, `pip` système et environnements virtuels. Explique quel interpréteur est utilisé et vérifie les commandes disponibles dans la version installée.

## Vérifier le premier lancement

- Confirme que le serveur local démarre et indique le port ou l'URL réellement affichés par le CLI.
- Le serveur de développement et LangSmith Studio sont des outils de développement ; ne les présente pas comme une configuration de production.
- Si le projet appelle un fournisseur LLM, suis le skill `configurer-cles-api-langchain` avant de diagnostiquer une erreur d'authentification.
- Si l'installation échoue, distingue un problème de version Python, de résolution de dépendances, de CLI absent ou de configuration du graphe avant de proposer un correctif.
