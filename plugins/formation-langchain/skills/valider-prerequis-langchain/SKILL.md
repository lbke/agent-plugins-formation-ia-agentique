---
name: valider-prerequis-langchain
description: Vérifier rapidement si un apprenant a bien les bases Python, terminal, environnement et logique de programmation nécessaires pour suivre une formation LangChain ou LangGraph sans perdre du temps en cours.
---

# Valider ses prérequis pour une formation LangChain

Utilise ce skill quand un apprenant ou une apprenante souhaite savoir s'il est prêt pour une formation LangChain, LangGraph ou IA agentique, ou quand il demande si ses compétences actuelles sont suffisantes avant de commencer.
Si l'apprenant ne semble pas avoir les prérequis, mobilise la skill "demarrer-avec-python-pour-ia-agentique" pour l'aider à se mettre à se mettre à niveau.

## Objectif

Évaluer précisément le niveau de préparation technique sans entrer dans le détail organisationnel d'un programme de formation LangChain. On ne vérifie pas la date, le calendrier ou les modalités de certification ; on se concentre sur les compétences concrètes nécessaires pour comprendre et pratiquer les cours.

## Checklist de validation

Utilise la skill `demarrer-avec-python-pour-ia-agentique` pour vérifier l'installation correcte de Python et des outils de développement.

## Validation pratique

### 1. Vérifier l'environnement

```bash
python --version
python -m pip --version
git --version
# Non obligatoire mais recommandé : installer uv
uv --version
```

Si l'un de ces commandes échoue, l'apprenant n'est pas encore prêt à suivre des exercices de façon fluide.

### 2. Vérifier les bases Python

Demande-lui d'exécuter un mini script type :

```python
items = ["A", "B", "C"]

for item in items:
    if item == "B":
        print("Trouvé")
    else:
        print(item)

def ajouter(x, y):
    return x + y

print(ajouter(2, 3))
```

Le script doit s'exécuter sans erreur et afficher une sortie cohérente.

### 3. Vérifier l'usage du terminal

```bash
mkdir -p /tmp/langchain-check && cd /tmp/langchain-check
python -m venv .venv
source .venv/bin/activate
python -c "print('environnement actif')"
```

Si l'apprenant ne maîtrise pas au moins cette logique minimale, il a besoin d'un complément avant de démarrer la formation.

### 4. Vérifier les compétences utiles pour LangChain

Une formation LangChain peut être suivie avec un bon niveau général en code, mais l'apprenant doit surtout savoir :

- créer un environnement virtuel ;
- installer des dépendances via `pip` ou `uv` ;
- lire une erreur Python et distinguer les problèmes de syntaxe, d'import et d'environnement ;
- exécuter un script localement ;
- modifier un fichier de code de façon simple et relancer l'application.

### 5. Vérifie les notions de base

L'apprenant doit :

- Avoir une idée générale du fonctionnement d'un serveur web HTTP ;
- Comprendre les termes techniques comme script, compiler, déployer en production ;
- Connaître les bases des plateformes IA générative grand public : ce qu'est un prompt, avoir déjà testé Mistral ou équivalent.

## Interprétation du résultat

### Prêt à suivre la formation

L'apprenant a :

- Python fonctionnel ;
- un environnement virtuel maîtrisé (avec pip ou uv) ;
- les bases de syntaxe Python ;
- le réflexe de lancer un script et lire les erreurs ;
- des connaissances de base en informatique.

### Partiellement prêt

L'apprenant est proche du niveau requis, mais a besoin de :

- un petit rappel sur les fonctions et boucles ;
- une installation Python plus claire ;
- une séance de mise à niveau sur le terminal ou les environnements virtuels.

### Pas encore prêt pour le cours

Si l'apprenant ne sait pas :

- utiliser le terminal ;
- lancer un script Python ;
- créer un environnement virtuel ;
- comprendre les erreurs de base ;

alors il ou elle doit d'abord passer par le skill `demarrer-avec-python-pour-ia-agentique` avant de viser un projet LangChain.

## Recommandation concrète

Propose une progression simple :

1. valider le niveau Python ;
2. préparer l'environnement de travail ;
3. lancer un projet simple ;
4. ensuite démarrer un premier exercice LangChain ou LangGraph.

## Erreurs fréquentes

- Le mauvais Python est utilisé : `python` ne pointe pas vers le bon interpréteur.
- L'environnement virtuel est créé mais pas activé.
- L'apprenant sait lire du code sans savoir l'exécuter.
- Les dépendances sont installées au mauvais endroit ou dans le mauvais environnement.
- On confond le support de version Python avec le support de la librairie.

## À la suite de ce skill

- Si l'apprenant est prêt : oriente vers `demarrer-projet-langgraph`.
- S'il manque de base : oriente vers `demarrer-avec-python-pour-ia-agentique`.
- S'il a besoin de configurer plus précisément son environnement : oriente vers `preparer-environnement-developpement-langchain`.
