---
name: tester-environnement-python
description: Vérifier pas à pas que Python, pip et uv sont correctement installés et utilisables depuis le terminal, avec la création d'un environnement virtuel de test, avant une formation ou un projet LangChain.
---

# Tester son environnement Python

Utilise ce skill quand un apprenant veut vérifier que son installation de Python est fonctionnelle, quand une autre skill a besoin de confirmer que Python, pip et uv sont disponibles, ou quand une commande Python échoue de façon inexpliquée.

Ce skill se limite au diagnostic : il n'installe rien. Il s'utilise avec `preparer-environnement-developpement-langchain`, qui aide effectivement l'utilisateur à installer chaque outil manquant, puis revient ici pour confirmer que tout fonctionne. Pour l'apprentissage du langage, oriente vers `demarrer-avec-python-pour-ia-agentique`.

## Objectif

Obtenir une réponse claire à trois questions : Python est-il installé et accessible ? pip fonctionne-t-il depuis le bon interpréteur ? uv est-il disponible ? Puis confirmer qu'un environnement virtuel peut être créé et activé.

`uv` est fortement conseillé : c'est l'outil utilisé pour l'installation locale pendant la formation LangChain et il simplifie la gestion des versions de Python et des dépendances. Il reste optionnel : si l'apprenant refuse de l'installer, poursuis avec `python -m venv` et `pip` sans bloquer.

## Étapes de vérification

Demande à l'apprenant d'exécuter chaque commande et de te coller la sortie complète, y compris les erreurs.

### 1. Python est installé et accessible

```bash
python --version
```

Selon le système, la commande peut être `python3` (Linux, macOS) ou `py` (Windows). Essaie les trois si la première échoue et note laquelle fonctionne : c'est celle à utiliser dans la suite.

Résultat attendu : une ligne du type `Python 3.x.y`.

Vérifie ensuite que la version est compatible avec LangChain : consulte la documentation LangChain actuelle pour connaître les versions supportées plutôt que de supposer qu'une version récente convient. Une version très récente de Python peut ne pas être encore prise en charge.

### 2. pip fonctionne depuis le bon interpréteur

```bash
python -m pip --version
```

Utilise toujours `python -m pip` plutôt que `pip` seul : cela garantit que pip correspond à l'interpréteur vérifié à l'étape 1.

Résultat attendu : une ligne du type `pip x.y from ... (python 3.x)`. La version Python indiquée entre parenthèses doit être celle de l'étape 1.

### 3. uv est disponible (optionnel mais fortement conseillé)

```bash
uv --version
```

Résultat attendu : une ligne du type `uv x.y.z`.

Si la commande échoue, propose l'installation via `preparer-environnement-developpement-langchain`. Après installation, il faut souvent rouvrir le terminal pour que `uv` soit trouvé.

Si l'apprenant ne souhaite pas installer `uv`, note-le et continue avec `python -m venv` et `pip` : ce n'est pas bloquant.

### 4. Créer et activer un environnement virtuel de test

Dans un dossier temporaire, pour ne pas polluer un projet existant.

Avec `uv` :

```bash
mkdir test-env-python && cd test-env-python
uv init
uv run python -c "print('environnement OK')"
```

Sans `uv` :

```bash
mkdir test-env-python && cd test-env-python
python -m venv .venv
```

Puis activer selon le système :

```bash
# Linux / macOS / WSL
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1

# Windows cmd
.venv\Scripts\activate.bat
```

Et vérifier :

```bash
python -c "print('environnement OK')"
python -m pip --version
```

Le chemin affiché par `pip --version` doit maintenant pointer dans `.venv`, pas dans l'installation globale.

### 5. Installer et importer une librairie

Toujours dans l'environnement de test, installe une petite librairie et importe-la.

Avec `uv` :

```bash
uv add requests
uv run python -c "import requests; print(requests.__version__)"
```

Sans `uv` :

```bash
python -m pip install requests
python -c "import requests; print(requests.__version__)"
```

Si l'import fonctionne, l'environnement est opérationnel. Le dossier de test peut ensuite être supprimé.

## Interprétation

- Les étapes 1, 2, 4 et 5 réussissent : l'environnement est prêt, avec ou sans `uv`.
- L'étape 1 échoue : Python n'est pas installé ou n'est pas sur le `PATH`. Oriente vers `preparer-environnement-developpement-langchain` pour l'installer.
- L'étape 2 échoue alors que l'étape 1 réussit : pip est absent de cette installation (`python -m ensurepip --upgrade` peut le réinstaller) ou l'apprenant a plusieurs Python et `pip` pointe sur un autre interpréteur.
- L'étape 4 échoue sous Windows PowerShell avec une erreur de politique d'exécution : l'activation des scripts est bloquée ; consulte la documentation officielle de Python sur les environnements virtuels pour la procédure adaptée.
- L'étape 5 échoue : vérifie que l'environnement est bien activé (le prompt du terminal affiche généralement `(.venv)`) et que l'accès réseau permet de télécharger des paquets.

## Erreurs fréquentes

- Plusieurs versions de Python coexistent et `python`, `python3`, `py` ne pointent pas vers la même : toujours vérifier avec `python -m pip --version` que pip et Python correspondent.
- `pip install` est lancé sans environnement activé et installe les paquets globalement.
- L'environnement virtuel est créé mais jamais activé.
- `uv` vient d'être installé mais le terminal n'a pas été rouvert.
- Le terminal de l'éditeur (VS Code) n'utilise pas le même interpréteur que le terminal système.

## À la suite de ce skill

- Pour installer ce qui manque (Python, pip, uv, Git, éditeur) : `preparer-environnement-developpement-langchain`.
- Pour apprendre les bases du langage Python : `demarrer-avec-python-pour-ia-agentique`.
- Pour vérifier les autres prérequis de la formation : `valider-prerequis-langchain`.
