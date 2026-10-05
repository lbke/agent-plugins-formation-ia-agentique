---
name: deployer-agent-langgraph
description: Guider la publication d'un projet LangGraph sur GitHub puis son exécution sur un hébergeur, notamment Render, ou aider à choisir entre développement local, conteneur et service géré. Utiliser pour préparer, configurer ou dépanner un déploiement.
---

# Déployer un agent LangGraph

Clarifie d'abord la cible (démonstration, examen, test ou production), le niveau de confidentialité du dépôt, le fournisseur d'hébergement et la disponibilité d'une licence LangGraph Deployment si nécessaire. Les offres gratuites, tarifs, étapes d'interface et conditions des services évoluent : vérifie leur documentation actuelle. Ne qualifie pas `langgraph dev` de serveur de production.

## Publier le code

1. Vérifie `git status`, les remotes et la branche avant de publier. Ne révèle pas de secrets et vérifie que `.env` est ignoré et non suivi par Git.
2. Crée le dépôt GitHub avec la visibilité adaptée aux données et au besoin. Un dépôt public peut être requis par un examen particulier, mais ne le recommande pas par défaut.
3. Si le dépôt cloné a déjà une remote `origin`, examine-la avant de la renommer `upstream`, puis ajoute la remote personnelle comme `origin`. Utilise l'URL fournie par GitHub et pousse la branche courante.

## Choisir une forme d'hébergement

- **Développement local** : `langgraph dev` convient aux itérations et outils de développement ; un tunnel peut exposer temporairement un serveur local, mais ce n'est pas un déploiement cloud de production.
- **Render ou un autre hébergeur** : vérifie si l'hébergeur supporte l'exécution du CLI LangGraph et sous quelles conditions/licences. Pour un service web, le processus doit écouter sur l'hôte public attendu et le port fourni par la plateforme ; ne fige pas un port sans vérifier le contrat actuel de l'hébergeur.
- **Conteneur** : une image construite avec les outils LangGraph peut demander une licence commerciale. Vérifie les licences et conditions avant de conseiller `langgraph build` ou l'hébergement de l'image.
- **Serveur alternatif open source** : des projets tiers comme Agent Service Toolkit ou Aegra peuvent remplacer certaines fonctions du CLI, sans garantie de compatibilité fonctionnelle. Vérifie leur état et leurs limites.
- **Service LangGraph géré** : compare les offres et coûts actuels et vérifie ce qui est réellement disponible dans le plan visé.

## Déploiement Render (ou plateforme à commandes configurables)

Quand le fournisseur accepte les commandes de construction et de démarrage personnalisées, configure celles-ci conformément à son guide :

```sh
# Construction avec uv
uv sync

# Exemple de démarrage de serveur de développement ; ne pas supposer que cela convient à la production
uv run langgraph dev --port "$PORT" --host 0.0.0.0 --no-browser
```

L'exemple reflète un parcours de démonstration des slides ; vérifie que le CLI, la licence, le port et l'usage du mode `dev` sont compatibles avec l'offre et l'environnement actuels avant de l'appliquer. Pour un déploiement production, choisis un serveur et un modèle de licence pris en charge.

1. Connecte le dépôt GitHub au service.
2. Configure les variables d'environnement/secret dans le tableau de bord de l'hébergeur. Le `.env` local n'est ni envoyé ni disponible par défaut.
3. Déploie et lis les logs de démarrage. Vérifie le point de santé ou `/docs` si ce serveur l'expose ; cette URL ne prouve pas à elle seule que l'agent fonctionne.
4. Connecte LangSmith Studio à l'URL de base du service si cette utilisation est supportée et appropriée. Studio est un outil de développement, pas une interface utilisateur finale.
5. Teste l'API avec un client LangGraph SDK ou l'interface prévue, puis vérifie une requête agent complète. Si Studio est indisponible, le SDK peut servir de solution de diagnostic selon les méthodes documentées pour sa version.

Pour les clés, erreurs 401 et vérification des variables, suis le skill `configurer-cles-api-langchain`. Ne copie jamais des clés dans le dépôt ou dans les logs.
