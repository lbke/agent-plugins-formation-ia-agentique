---
name: configurer-cles-api-langchain
description: Configurer et vérifier des clés API de fournisseur LLM pour un projet LangChain ou LangGraph, notamment avec un fichier .env chargé par le CLI LangGraph. Utiliser pour résoudre les erreurs de clé absente/invalide et éviter d'exposer ou de publier les secrets.
---

# Configurer les clés API

Aide l'utilisateur à charger une clé nécessaire à son projet sans lui demander de la coller dans la conversation, le code ou un dépôt. Demande quel fournisseur et quel modèle sont utilisés ; le nom de variable et l'URL de base doivent correspondre à l'intégration réelle.

## Configurer le fournisseur

1. Consulte la configuration actuelle du projet : dépendance LangChain du fournisseur, appel `init_chat_model`, nom de modèle, `model_provider`, URL de base éventuelle et variable référencée dans le code.
2. Vérifie la documentation actuelle du fournisseur pour créer ou révoquer une clé. Les liens et offres gratuits montrés dans les supports peuvent avoir changé.
3. Pour OpenRouter, un exemple de configuration peut être :

```dotenv
OPENROUTER_API_KEY=remplacer_par_la_cle
```

Pour un autre fournisseur, utilise exactement le nom de variable attendu par le code. Ne stocke pas la valeur réelle dans les fichiers suivis par Git.

## Charger et contrôler `.env`

Le CLI LangGraph peut charger automatiquement un `.env` selon sa configuration et son répertoire de lancement. Vérifie le fichier `.env` et `langgraph.json` si l'application ne voit pas la variable. Avec un script Python autonome, `python-dotenv` ou une injection par l'environnement peut être nécessaire ; ne présume pas qu'un `.env` est chargé par Python tout seul.

1. Vérifie que `.env` est ignoré par Git et qu'il n'a jamais été publié. L'ignorer maintenant ne retire pas une clé déjà suivie ou divulguée.
2. Ajoute la clé dans le tableau de bord de l'hébergeur séparément : un fichier local non versionné n'est généralement pas présent en production.
3. Lance le contrôle non destructif fourni avec ce skill depuis le répertoire du projet :

```sh
python /chemin/vers/ce-skill/scripts/check_env.py --env-file .env
```

Le script vérifie par défaut `OPENROUTER_API_KEY`. Pour un autre fournisseur, passe le nom attendu :

```sh
python /chemin/vers/ce-skill/scripts/check_env.py --env-file .env --required OPENAI_API_KEY
```

Il signale les clés manquantes ou vides, les placeholders, les doublons et les lignes mal formées sans jamais afficher la valeur d'une clé. Il ne prouve pas que la clé est valide ; ne l'envoie pas à un service externe pour la tester.

## Diagnostiquer sans révéler le secret

- `KeyError` / variable manquante : comparer le nom lu dans le code et celui du `.env`, puis vérifier le répertoire de lancement et le chargement de dotenv.
- HTTP 401 : vérifier localement que la clé correspond au fournisseur et au compte, qu'elle n'est ni expirée ni révoquée, et que le modèle / endpoint est correct. Ne pas demander à l'utilisateur de révéler la clé.
- En production : configurer le secret dans les variables d'environnement du fournisseur d'hébergement, redémarrer le service si nécessaire, puis consulter des logs qui ne divulguent pas les en-têtes ou valeurs secrets.
- Si la clé a été commitée ou partagée, la révoquer et en créer une nouvelle ; supprimer le fichier du dépôt ne suffit pas à invalider l'ancienne clé.

Les clés LangSmith (par exemple `LANGSMITH_API_KEY`) sont distinctes des clés du fournisseur LLM et ne sont nécessaires que si le projet utilise ces services.
