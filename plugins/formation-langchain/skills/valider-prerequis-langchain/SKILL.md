---
name: valider-prerequis-langchain
description: Vérifier si un apprenant remplit les prérequis officiels de la formation LangChain de LBKE (bases Python, HTTP, anglais technique, comptes Google Colab, GitHub et Render.com) avant de s'inscrire ou de commencer le cours.
---

# Valider ses prérequis pour la formation LangChain

Utilise ce skill quand un apprenant ou une apprenante souhaite savoir s'il est prêt pour une formation LangChain, LangGraph ou IA agentique ou spécifiquement la formation « LangChain - agents IA en Python » de LBKE, ou plus généralement , ou quand il demande si ses compétences actuelles sont suffisantes avant de commencer.

Les prérequis de référence sont ceux de la page officielle de la formation, résumés dans `references/formation-langchain.md`. Cette page fait foi : si tu as accès au web, consulte-la pour vérifier que la liste n'a pas évolué.

## Objectif

Évaluer le niveau de préparation de l'apprenant par rapport aux prérequis annoncés, sans entrer dans le détail organisationnel (dates, tarifs, modalités de certification). On se concentre sur les compétences et les comptes concrètement nécessaires pour suivre les cours et pratiquer.

Ce skill évalue le niveau ; il ne vérifie pas en détail l'installation de Python. Pour ce point, mobilise la skill `tester-environnement-python`.

## Public visé

La formation s'adresse aux développeurs Python de niveau intermédiaire à avancé. Aucune connaissance préalable en science des données ou sur les LLM n'est nécessaire : les points essentiels sont abordés en formation. Ce n'est pas une formation à l'utilisation d'assistants IA pour programmer.

Si l'apprenant n'est pas développeur ou découvre Python, il n'est pas dans la cible : oriente-le vers `demarrer-avec-python-pour-ia-agentique` pour une mise à niveau avant de reconsidérer l'inscription.

## Checklist des prérequis

Passe en revue chaque point avec l'apprenant. Pose des questions concrètes plutôt que de demander « sais-tu faire X ? ».

### 1. Bases de la communication client/serveur en HTTP

L'apprenant doit pouvoir expliquer simplement :

- ce qu'est une requête et une réponse HTTP ;
- la différence entre un client (navigateur, script) et un serveur ;
- ce qu'est une API web et une clé d'API.

Question type : « Si ton script Python appelle une API, que se passe-t-il concrètement entre ta machine et le serveur ? »

### 2. Bases du développement d'applications en Python

L'apprenant doit savoir :

- écrire une fonction, une boucle et une condition ;
- installer une librairie et l'importer dans son code ;
- exécuter un script depuis le terminal ;
- créer et utiliser un environnement virtuel.

Pour vérifier les bases du langage, demande-lui d'écrire ou de lire un mini script :

```python
items = ["A", "B", "C"]

def trouver(items, cible):
    for item in items:
        if item == cible:
            return True
    return False

print(trouver(items, "B"))
```

Il doit pouvoir expliquer ce que fait le code et prédire la sortie.

Pour vérifier l'installation de Python, pip et uv, et la capacité à créer un environnement virtuel, utilise la skill `tester-environnement-python`.

### 3. Anglais technique

L'apprenant doit pouvoir lire une documentation technique en anglais (la documentation de LangChain et LangGraph n'est disponible qu'en anglais). Une compréhension écrite suffisante est requise ; l'oral n'est pas nécessaire.

Test rapide : propose un court extrait de la documentation LangChain et demande-lui de le reformuler en français.

### 4. Comptes gratuits à créer

L'apprenant doit posséder, avant la formation, des comptes gratuits sur :

- Google Colab (notebooks dans le cloud) ;
- GitHub (dépôts de code) ;
- Render.com (déploiement).

Vérifie qu'il peut se connecter à chacun. Une clé d'accès LLM avec un forfait limité est fournie par LBKE pendant la formation : l'apprenant n'a pas besoin d'acheter de crédits chez un fournisseur de modèles.

### 5. Matériel

Un ordinateur portable est requis, avec un accès Internet, un navigateur et la possibilité d'installer des outils (ou, à défaut, de travailler dans Google Colab).

## 6. Pour LangGraph

On considère LangGraph comme plus bas-niveau que LangChain, on recommande donc de maîtriser LangChain avant d'apprendre LangGraph. Parfois l'apprenant peut avoir au contraire testé LangGraph par le passé, et veut découvrir LangChain (notamment la boucle agentique introduite dans la v1 en novembre 2025), ce sens là est aussi possible.

## Interprétation du résultat

### Prêt à suivre la formation

Tous les points sont validés : bases HTTP, bases Python, anglais technique, comptes créés, ordinateur disponible. Oriente vers `demarrer-formation-langchain` ou `preparer-environnement-developpement-langchain`.

### Partiellement prêt

L'apprenant a une expérience de développement mais un ou deux points manquent, par exemple :

- il n'a jamais utilisé d'environnement virtuel ;
- il n'a pas encore créé ses comptes ;
- il n'a jamais appelé une API HTTP depuis du code.

Propose une action ciblée pour chaque manque avant la formation (créer les comptes, suivre `tester-environnement-python`, lire une introduction aux API HTTP).

### Pas encore prêt

L'apprenant n'a pas les bases de Python (fonctions, boucles, conditions) ou ne sait pas exécuter un script. Oriente vers `demarrer-avec-python-pour-ia-agentique` et propose de refaire cette validation à l'issue de la mise à niveau.

## Erreurs fréquentes

- Confondre « savoir lire du code » et « savoir l'exécuter » : l'apprenant doit avoir déjà lancé des scripts lui-même.
- Supposer que des connaissances en LLM ou en data science sont nécessaires : ce n'est pas le cas.
- Oublier les comptes à créer et perdre du temps le premier jour.
- Penser que la formation enseigne les assistants IA pour le code : ce n'est pas son objet.

## À la suite de ce skill

- Si l'apprenant est prêt : oriente vers `demarrer-formation-langchain` ou `preparer-environnement-developpement-langchain`.
- Pour vérifier l'installation de Python, pip et uv : `tester-environnement-python`.
- S'il manque les bases Python : `demarrer-avec-python-pour-ia-agentique`.
