---
name: preparer-environnement-developpement-langchain
description: Installer et configurer un environnement de développement fonctionnel pour un projet LangChain ou LangGraph, outil par outil (Python, pip, uv, environnement virtuel, Git, éditeur), en s'appuyant sur le diagnostic de la skill tester-environnement-python.
---

# Préparer l'environnement de développement LangChain

Utilise ce skill quand l'utilisateur veut se préparer avant la formation ou avant un projet personnel, et qu'il a besoin d'un environnement de développement local fonctionnel : terminal, Python, éditeur, gestionnaire de dépendances et outils de base.

Ce skill s'utilise avec `tester-environnement-python` : le test se limite au diagnostic, la préparation consiste à aider effectivement l'utilisateur à installer et configurer chaque outil manquant. Le déroulé est donc : tester, installer ce qui manque, retester.

Les liens d'installation officiels (Python, `uv`, Git, VS Code, `venv`) sont rassemblés dans `references/liens.md`.

## Objectif

Créer une base technique fiable pour travailler avec Python et les bibliothèques de LangChain/LangGraph sans mélange d'environnements ni de versions.

## Déroulé

### 1. Diagnostiquer avec `tester-environnement-python`

Commence toujours par la skill `tester-environnement-python` pour savoir où en est l'utilisateur : Python, pip, uv, création d'un environnement virtuel, installation d'une librairie. Note les étapes qui échouent ; ce sont les seules à traiter ci-dessous. Ne réinstalle pas ce qui fonctionne déjà.

### 2. Installer Python

Si Python est absent ou dans une version non compatible avec LangChain, aide l'utilisateur à l'installer. Vérifie la version supportée dans la documentation LangChain actuelle avant de choisir.

Deux approches :

- avec `uv` (recommandé) : `uv python install` installe une version gérée par `uv`, sans toucher au Python système ;
- avec l'installateur officiel de python.org (lien dans `references/liens.md`). Sur Windows, coche l'option d'ajout de Python au `PATH` pendant l'installation ; sinon la commande `py` reste disponible.

Si la machine a déjà plusieurs versions de Python, propose un gestionnaire de versions (`uv`, `pyenv`, `py` sur Windows) et fais choisir explicitement l'interpréteur à utiliser.

### 3. Installer `uv`

Fortement recommandé : c'est l'outil utilisé pour l'installation locale pendant la formation. Suis la documentation officielle d'installation (lien dans `references/liens.md`). Fais rouvrir le terminal après l'installation.

Si l'utilisateur refuse `uv`, respecte ce choix et poursuis avec `python -m venv` et `pip` ; ce n'est pas bloquant.

### 4. Créer l'environnement virtuel du projet

Dans le dossier du projet, pour éviter d'installer des paquets au mauvais endroit.

Avec `uv` :

```bash
uv init
```

Sans `uv` :

```bash
python -m venv .venv
source .venv/bin/activate
```

Sur Windows PowerShell :

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Installer les dépendances

Avec `uv` :

```bash
uv add langchain
uv sync
```

Sans `uv` :

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

La règle de base est la suivante : ne mélange pas `pip` système, `pip` de l'environnement virtuel et `uv` sans l'expliquer clairement.

### 6. Installer les outils de développeur

Pour une bonne expérience de travail, vérifie et installe si besoin :

- Git, pour cloner et versionner le projet ;
- un éditeur de code, VS Code recommandé, avec son extension Python ;
- un terminal fonctionnel, de préférence celui intégré à l'éditeur, configuré pour utiliser l'environnement virtuel du projet ;
- un navigateur pour consulter la documentation et les logs ;
- un accès Internet pour télécharger les dépendances.

### 7. Retester

Relance la skill `tester-environnement-python` pour confirmer que toutes les étapes passent, puis vérifie dans le projet :

```bash
python -c "print('environnement OK')"
```

## Vérifications à faire avant de commencer un projet

- La commande `python` correspond bien à l'interpréteur attendu.
- Le terminal est bien dans le bon dossier de travail.
- L'environnement virtuel est activé.
- Les dépendances du projet sont installées dans ce même environnement.
- Le script le plus simple du projet s'exécute sans erreur.

## Erreurs fréquentes

- Installer sans avoir diagnostiqué : on réinstalle Python alors que seul pip manquait.
- Utiliser `pip` sans environnement actif.
- Installer des libs globalement au lieu d'un projet dédié.
- Confondre version Python locale et version du projet.
- Oublier de changer de dossier avant de lancer le projet.
- Croire que le terminal est toujours le bon sans le vérifier.
- Oublier de rouvrir le terminal après l'installation d'un outil.

## À la suite de ce skill

- Pour diagnostiquer ou confirmer l'installation : `tester-environnement-python`.
- Pour apprendre les bases du langage Python : `demarrer-avec-python-pour-ia-agentique`.
- Pour vérifier les autres prérequis de la formation : `valider-prerequis-langchain`.
- Quand l'environnement est prêt : `demarrer-projet-agent-server` ou `creer-agent-langchain`.
