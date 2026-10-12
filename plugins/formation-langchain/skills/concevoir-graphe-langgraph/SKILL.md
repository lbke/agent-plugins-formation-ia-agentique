---
name: concevoir-graphe-langgraph
description: Concevoir ou déboguer un workflow agentique explicite avec LangGraph, en structurant état, nœuds, arêtes conditionnelles, mémoire de conversation, interruptions, appels d'outils et sorties structurées.
---

# Concevoir un graphe LangGraph

Utilise ce skill quand l'utilisateur a besoin de contrôler les étapes et transitions d'un agent. Commence par dessiner le flux en texte avant d'écrire du code : entrées, nœuds, décisions, sorties et chemins d'erreur.

## Définir l'état

- Décris les données d'entrée et de sortie et lesquelles doivent survivre entre les nœuds.
- Utilise des types explicites. Une `dataclass` avec `field(default_factory=...)`, `TypedDict` ou un schéma Pydantic peuvent convenir selon l'API du projet. Évite les objets mutables partagés comme valeur par défaut.
- Pour une conversation, utilise le schéma de messages recommandé par la version LangGraph actuelle si l'historique complet est requis ; sinon conserve seulement les éléments strictement utiles.
- Distingue l'état du graphe et le contexte d'exécution : ne place pas de secret dans l'état observable par le modèle.

## Modéliser nœuds et transitions

1. Implémente chaque nœud comme une fonction qui lit l'état et renvoie les mises à jour attendues par le schéma et ses reducers. Un nœud asynchrone doit attendre ses appels (`await`) avant de lire leur résultat.
2. Relie les étapes fixes par des arêtes directes ; utilise les arêtes conditionnelles pour choisir explicitement la suite selon l'état.
3. Définis le graphe avec `StateGraph`, un point d'entrée (`START`), des nœuds, des arêtes puis compile-le. Vérifie les noms de nœuds dans tous les branchements.
4. Pour un appel d'outil, relie l'appel de modèle à un nœud d'exécution des outils puis au modèle afin qu'il interprète le résultat. Utilise les primitives de routage/outils compatibles avec la version installée.
5. Ajoute un chemin d'erreur explicite et une sortie finie. Un échec, une erreur d'outil ou une réponse structurée invalide ne doit pas être traité comme un succès.

## Mémoire, interruptions et sorties structurées

- Un `thread_id` associé à un checkpointer permet de reprendre l'état entre les tours. Vérifie que le stockage/checkpointer choisi est adapté à l'environnement ; une mémoire en processus n'est pas une persistance de production.
- Utilise `interrupt` quand le workflow doit attendre une décision utilisateur puis reprendre au même thread. Décris comment le client renvoie la réponse. Pour une conversation simple, un nouvel input dans le state peut être plus simple qu'une interruption.
- Pour une sortie structurée, définis un schéma typé, vérifie que le modèle et son fournisseur prennent en charge la méthode choisie (`with_structured_output` ou équivalent) et valide le résultat avant de l'utiliser.

## Valider le flux

Teste au minimum le chemin heureux, chaque branche conditionnelle, une erreur de nœud ou d'outil, la reprise d'un même thread et la reprise après interruption si utilisée. Inspecte l'état intermédiaire dans Studio ou les logs sans exposer de secrets. Vérifie les imports et signatures dans la documentation de la version réellement installée : les extraits de cours peuvent contenir des erreurs ou employer une API ancienne.
