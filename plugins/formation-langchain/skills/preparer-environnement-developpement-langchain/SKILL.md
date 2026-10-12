---
name: preparer-environnement-developpement-langchain
description: Préparer un environnement de développement fonctionnel pour un projet LangChain ou LangGraph en vérifiant Python, gestionnaire de versions, terminal, éditeur et outils de base du workflow de développement.
---

# Préparer l'environnement de développement LangChain

Utilise ce skill quand l'utilisateur veut se préparer avant la formation ou avant un projet personnel, et qu'il a besoin d'un environnement de développement local fonctionnel : terminal, Python, éditeur, gestionnaire de dépendances et outils de base.

## Objectif

Créer une base technique fiable pour travailler avec Python et les bibliothèques de LangChain/LangGraph sans mélange d'environnements ni de versions.

## Points de préparation

### 1. Python

Vérifie qu'un interpréteur Python est installé et que la commande disponible est cohérente avec le projet.

```bash
python --version
python -m pip --version
```

Si nécessaire, propose un gestionnaire de versions si la machine en a plusieurs :

- `uv` ;
- `pyenv` ;
- `pymanager` / `py` sur Windows ;
- autres gestionnaires selon le système.

### 2. Environnement virtuel

Crée un environnement dédié pour éviter d'installer des paquets au mauvais endroit.

```bash
python -m venv .venv
source .venv/bin/activate
```

Sur Windows PowerShell :

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Gestion des dépendances

Selon la préférence du projet :

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

ou :

```bash
uv sync
```

La règle de base est la suivante : ne mélange pas `pip` système, `pip` de l'environnement virtuel et `uv` sans l'expliquer clairement.

### 4. Outils de développeur

Pour une bonne expérience de travail, vérifie :

- Git installé pour cloner et versionner le projet ;
- un éditeur de code (VS Code recommandé) ;
- un terminal fonctionnel ;
- un navigateur pour vérifier les logs ou la documentation ;
- un accès Internet pour consulter la documentation et les dépendances.

### 5. Vérification finale

Le bon environnement est celui qui permet de lancer un script local et de relancer rapidement un projet simple.

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

- Utiliser `pip` sans environnement actif.
- Installer des libs globalement au lieu d'un projet dédié.
- Confondre version Python locale et version du projet.
- Oublier de changer de dossier avant de lancer le projet.
- Croire que le terminal est toujours le bon sans le vérifier.

## À la suite de ce skill

Quand l'environnement est prêt, passe au skill `demarrer-projet-langgraph` ou à `valider-pre-requis-langchain` selon le besoin : préparation technique ou validation de niveau.
