---
name: demarrer-avec-python-pour-ia-agentique
description: Aider un apprenant à installer, vérifier et utiliser Python pour une formation IA agentique, avec les bases de syntaxe et l'environnement de travail nécessaires avant de démarrer un projet LangChain ou LangGraph.
---

# Démarrer avec Python pour une formation IA agentique

Utilise ce skill quand l'utilisateur veut commencer une formation IA agentique, n'a pas encore installé Python, ou veut vérifier s'il est prêt au niveau technique pour suivre un cours LangChain ou LangGraph.

## Objectif

Accompagner l'utilisateur jusqu'à un environnement Python fonctionnel, sans supposer qu'il maîtrise déjà les outils de développement. L'idée est de se concentrer sur les compétences minimales utiles pour une formation IA agentique : exécuter Python, créer un environnement virtuel, installer des dépendances, écrire de petites fonctions et vérifier le bon fonctionnement d'un script.

## Vérifier les prérequis techniques

Avant de proposer un cours ou un projet, confirme au moins ces éléments :

- Python est installé et accessible depuis le terminal.
- La version est compatible avec le type de projet souhaité ; pour LangChain, vérifie toujours la version supportée dans la documentation actuelle avant de conclure qu'une version est acceptable.
- Un environnement virtuel peut être créé et activé.
- L'utilisateur sait lancer un script simple depuis le terminal.
- L'utilisateur connaît les bases de syntaxe Python : variables, fonctions, conditions, boucles, classes simples.

## Étapes recommandées

1. Vérifier l'installation de Python.

```bash
python --version
python3 --version
python -m pip --version
```

Si l'un des appels échoue, installe Python avant de continuer. Sur Windows, la commande `py` peut remplacer `python` selon la configuration locale.

2. Choisir une version adaptée et éviter les pièges.

- Python 3.10+ est généralement une bonne base pour les projets Python modernes.
- Si le projet vise LangChain, vérifie la compatibilité de la version Python avant de déclarer qu'une version est valide.
- Évite de recommander une version non supportée par la documentation en vigueur.

3. Créer un environnement virtuel.

```bash
python -m venv .venv
```

Puis activer l'environnement selon le système :

```bash
# Linux / macOS / WSL
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

4. Mettre à jour l'installateur et installer les dépendances minimales.

```bash
python -m pip install --upgrade pip
```

Si le contexte le nécessite, ajoute ensuite le package de travail ou les dépendances du projet, par exemple :

```bash
python -m pip install -r requirements.txt
```

ou les dépendances du projet Python choisi.

5. Vérifier les bases de syntaxe Python.

Demande à l'utilisateur d'exécuter un script minimal comme celui-ci :

```python
message = "Bonjour"

def dire_bonjour(nom: str) -> str:
    return f"Bonjour {nom}"

for i in range(3):
    print(dire_bonjour(message))
```

Le script doit s'exécuter sans erreur et afficher le message attendu.

6. Vérifier l'éditeur et le terminal.

- VS Code est un bon choix pour les projets Python.
- Assure-toi que le terminal utilisé est bien celui de l'environnement virtuel actif.
- Vérifie que Git est disponible si le projet doit être cloné ou versionné.

## Vérifications utiles

- `python --version` renvoie bien une version exploitable.
- `python -m pip --version` fonctionne depuis le bon environnement.
- `python -c "print('ok')"` affiche `ok` sans erreur.
- Un petit script avec fonction et boucle s'exécute sans problème.
- L'utilisateur sait où sont installés ses paquets et comment activer son environnement.

## Erreurs fréquentes

- Python n'est pas installé ou n'est pas sur le `PATH`.
- L'utilisateur exécute `pip` dans le mauvais environnement.
- Il utilise une version Python non compatible avec le projet visé.
- Il a du mal à exécuter des scripts depuis le terminal.
- Il sait écrire du code dans un éditeur mais n'a pas validé le lancement local.

## À la suite de ce skill

Quand l'environnement est validé, oriente l'utilisateur vers le skill `demarrer-projet-langgraph` pour lancer un projet LangGraph ou LangChain, ou vers `valider-pre-requis-langchain` pour vérifier s'il est prêt à suivre une formation donnée.
