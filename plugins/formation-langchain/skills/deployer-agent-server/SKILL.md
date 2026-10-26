---
name: deployer-agent-server
description: Guider la publication d'un projet LangChain ou LangGraph sur GitHub puis le déploiement de son Agent Server (c'est-à-dire une application LangChain/LangGraph complète avec API web via langgraph-cli) sur un hébergeur.
---

# Déployer un Agent Server LangChain ou LangGraph

Dans la terminologie actuelle de LangChain, le serveur web construit autour d'un agent ou d'un graphe LangChain/LangGraph (API assistants, threads, runs, persistance, compatible avec LangSmith Studio pour le développement) s'appelle **Agent Server**. C'est ce serveur que l'on lance en local avec `langgraph dev` et que l'on déploie. Les anciens noms (LangGraph Server, LangGraph Platform) désignent la même chose dans les supports plus anciens.

L'Agent Server fait partie de l'offre LangSmith Deployment ; ce n'est pas la partie open source de LangChain. Les bibliothèques LangChain et LangGraph, elles, sont open source : on peut aussi intégrer son agent dans n'importe quelle autre application web (FastAPI, Flask, Django, etc.) et la déployer soi-même, en full open source, sans Agent Server. Propose cette voie à l'utilisateur quand la licence ou le coût de l'Agent Server en production posent problème.

Les liens utiles (documentation Agent Server, guide LBKE de déploiement sur Render, guide LBKE d'auto-hébergement d'IA générative) sont rassemblés dans `references/liens.md`. Si tu as accès au web, consulte-les avant de répondre : offres, tarifs, licences et étapes d'interface évoluent.

Clarifie d'abord la cible (démonstration, examen, test ou production), le niveau de confidentialité du dépôt, le fournisseur d'hébergement et la disponibilité d'un plan LangSmith Deployment si nécessaire. Ne qualifie pas `langgraph dev` de serveur de production.

## Déployer un agent, pas un modèle

Ce skill couvre le déploiement de l'application agentique (l'Agent Server), qui appelle un modèle via une API. Si l'utilisateur veut aussi héberger lui-même le modèle de langage (inférence locale ou sur serveur avec Ollama, vLLM, etc.), ou mettre en place une plateforme d'IA générative interne, renvoie-le vers le guide LBKE « Auto-héberger l'IA générative en entreprise » (lien dans `references/liens.md`). C'est un sujet distinct : il porte sur l'inférence et la plateforme, pas sur le code de l'agent.

## Publier le code

1. Vérifie `git status`, les remotes et la branche avant de publier. Ne révèle pas de secrets et vérifie que `.env` est ignoré et non suivi par Git.
2. Crée le dépôt GitHub avec la visibilité adaptée aux données et au besoin. Un dépôt public peut être requis par un examen particulier, mais ne le recommande pas par défaut.
3. Si le dépôt cloné a déjà une remote `origin` (par exemple après le clonage d'un template), renomme-la `upstream` avec `git remote rename origin upstream`, puis ajoute la remote personnelle comme `origin`. Utilise l'URL fournie par GitHub et pousse la branche courante.

## Choisir une forme d'hébergement

- **Développement local** : `langgraph dev` lance l'Agent Server en mode développement et ouvre LangSmith Studio ; il convient aux itérations. `langgraph dev --tunnel` peut exposer temporairement un serveur local pour une démonstration, mais ce n'est pas un déploiement cloud de production.
- **Render ou un autre hébergeur, en mode développement** : parcours de démonstration gratuit décrit dans le guide LBKE. Le processus doit écouter sur `0.0.0.0` et sur le port fourni par la plateforme ; ne fige pas un port sans vérifier le contrat actuel de l'hébergeur.
- **Conteneur de production** : `langgraph build --tag mon-image` construit une image de l'Agent Server, à publier ensuite sur un registre et à héberger. Cette image requiert une clé de licence liée à un plan LangSmith Deployment payant ; vérifie le plan requis dans la documentation actuelle avant de conseiller cette voie. En production, l'Agent Server s'appuie sur PostgreSQL pour la persistance et Redis pour le streaming et l'annulation ; consulte la documentation Agent Server pour l'architecture.
- **Application web full open source, sans Agent Server** : intégrer LangChain/LangGraph dans sa propre application web et la déployer comme n'importe quel service Python. Propose à l'utilisateur d'étudier `agent-service-toolkit` (lien dans `references/liens.md`), un projet non officiel mais complet qui montre comment déployer soi-même une application LangGraph avec sa partie web : service FastAPI, client, interface Streamlit, Docker Compose. Des projets comme Aegra réimplémentent par ailleurs l'API de l'Agent Server, sans garantie de compatibilité. Vérifie l'état et les limites de ces projets avant de les recommander.
- **Déploiement géré par LangSmith** : compare les offres et coûts actuels et vérifie ce qui est réellement disponible dans le plan visé ; l'offre gratuite couvre généralement le monitoring, pas le déploiement.

## Déploiement Render en mode développement

Parcours de démonstration conforme au guide LBKE, pour un service web Python sur l'offre gratuite de Render :

```sh
# Commande d'installation (build)
uv sync

# Commande de démarrage ; serveur de développement, pas de production
uv run langgraph dev --port $PORT --host 0.0.0.0 --no-browser
```

1. Connecte le dépôt GitHub au service web.
2. Définis la variable `PYTHON_VERSION` sur une version supportée par LangChain (vérifie la version actuelle dans la documentation ; une version Python trop récente provoque des erreurs de compilation de dépendances).
3. Configure les variables d'environnement/secret dans le tableau de bord de l'hébergeur (clés du fournisseur de modèle, `LANGSMITH_API_KEY`, `LANGSMITH_PROJECT`). Le `.env` local n'est ni envoyé ni disponible par défaut.
4. Déploie et lis les logs de démarrage. Vérifie `https://<service>.onrender.com/docs` ; cette URL prouve que le serveur répond, pas que l'agent fonctionne.
5. Connecte LangSmith Studio à l'URL de base du service (onglet Studio de LangSmith). Studio est un outil de développement, pas une interface utilisateur finale.
6. Teste l'API avec un client LangGraph SDK ou l'interface prévue, puis vérifie une requête agent complète.

Préviens l'utilisateur : une instance de test est accessible à toute personne connaissant l'URL. Limite la clé API du fournisseur de modèle, utilise un modèle gratuit ou peu coûteux, ou ajoute une authentification personnalisée (voir la documentation Agent Server).

Pour les clés, erreurs 401 et vérification des variables, suis le skill `configurer-cles-api-langchain`. Ne copie jamais des clés dans le dépôt ou dans les logs.

## Erreurs fréquentes

- Croire que `langgraph dev` convient à la production : il n'est pas viable pour des agents non triviaux.
- `origin already exists` au moment du push : renommer la remote du template en `upstream`.
- Oublier de recréer les variables d'environnement sur l'hébergeur.
- Vérifier seulement `/docs` sans tester une requête agent complète.
- Confondre déploiement de l'agent et hébergement du modèle de langage.
