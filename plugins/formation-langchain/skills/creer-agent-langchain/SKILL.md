---
name: creer-agent-langchain
description: Aider à construire un agent conversationnel simple avec LangChain, un état typé et des outils qui lisent ou mettent à jour cet état. Utiliser pour prototyper un agent à boucle simple plutôt qu'un workflow LangGraph personnalisé.
---

# Créer un agent simple avec LangChain

Conduis l'utilisateur vers un agent minimal avec un objectif précis, une entrée/sortie explicite, des outils nécessaires et un test local. Préfère l'API de haut niveau LangChain pour ce cas d'usage ; si le besoin exige des transitions explicites, des interruptions ou une orchestration contrôlée, oriente vers le skill `concevoir-graphe-langgraph`.

## Concevoir l'état et les outils

1. Écris le cas d'usage en une phrase et précise ce que l'agent doit demander, décider et renvoyer.
2. Étends le schéma d'état agent fourni par la version de LangChain installée pour y placer les informations à conserver au-delà du seul appel courant. Utilise des champs typés (par exemple des préférences booléennes optionnelles), sans dupliquer le champ de conversation géré par le framework.
3. Ajoute uniquement des outils utiles. Un outil Python peut lire ou modifier l'état via le runtime prévu par l'API actuelle ; documente chaque outil par une docstring descriptive et valide ses entrées.
4. Pour des capacités externes, évalue un outil MCP adapté plutôt que d'accorder à l'agent un accès général au système.
5. Définis les permissions et les effets de bord. Exige confirmation humaine avant une action externe, financière, destructive ou difficile à annuler.

## Conversation et mémoire

- Explique que le thread identifie une conversation et permet au checkpointer de persister l'état d'un tour à l'autre ; ne confonds pas cette mémoire court-terme avec une mémoire longue durée.
- LangSmith Studio peut gérer le thread de l'interface. Dans le code client, passe le `thread_id` selon le format de configuration documenté pour la version installée.
- Choisis entre ne conserver que les derniers messages utiles et le schéma `MessagesState` / messages de conversation complet, selon le besoin et le coût. Ne conserve pas des données personnelles sans raison.

## Tester et faire évoluer

1. Teste un échange simple, la réutilisation du même thread et un nouvel échange sans thread précédent.
2. Teste chaque outil directement et vérifie les changements d'état ; ne suppose pas que le modèle appellera l'outil de façon déterministe.
3. Vérifie le chargement du modèle et sa clé avec `configurer-cles-api-langchain`.
4. Inspecte les erreurs réelles du framework installé. Les noms d'import, schémas d'état et signatures LangChain évoluent ; consulte la documentation correspondant à la version du projet au lieu de recopier une ancienne API.
