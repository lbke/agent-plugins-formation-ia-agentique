# Consignes de création et de maintenance du plugin

Ce document est destiné aux agents IA qui font évoluer ce dépôt à partir des ressources de formations de LBKE. 

Il ne constitue pas un skill Claude et ne doit pas être placé sous `skills/` !

## Pour Claude

Documentation Claude pour la création de plugins : https://claude.com/docs/build/overview

## Pour ChatGPT

Documentation ChatGPT pour la création de plugins : https://developers.openai.com/plugins

ChatGPT respecte le standard "Agent Plugins" : https://agent-plugins.org/

Pour soumettre: 
https://developers.openai.com/plugins/deploy/submission

## Transformer des supports de formation en skills

1. Lire les diapositives dans l'ordre et noter leur sujet et leurs dépendances.
2. Regrouper les diapositives qui servent un même objectif opérationnel. Créer un skill par cas d'usage autonome plutôt qu'un skill généraliste qui résume toute la formation.
3. Parcourir l'ensemble des diapositives avant de conclure : chaque section utile doit être reprise dans un skill ou identifiée comme simple titre, transition ou contenu sans procédure exploitable.
4. Rédiger les skills dans la langue du support et en suivant le format attendu par Claude (`SKILL.md` avec frontmatter `name` et `description`).
5. Donner des étapes concrètes, les prérequis, les vérifications et les erreurs fréquentes. Ne pas présenter des versions, offres gratuites, interfaces ou tarifs susceptibles d'évoluer comme des faits permanents : inviter à vérifier la documentation actuelle du fournisseur.
6. Corriger les erreurs techniques des supports plutôt que de les reproduire. Ne jamais inventer une exécution, une vérification ou une garantie.

## Scripts d'aide

Ajouter un petit script seulement lorsqu'il automatise une vérification directement liée au cas d'usage du skill. Le script doit avoir une interface documentée, fonctionner sans dépendances inutiles, signaler clairement les erreurs, ne jamais afficher de secrets et ne jamais modifier ou transmettre les identifiants de l'utilisateur.

## Organisation et validation

- Les compétences livrées aux utilisateurs résident sous `skills/<nom-du-skill>/`.
- Les consignes de contribution et les documents internes résident hors de `skills/`, par exemple dans `authoring/`.
- Mettre à jour le README lorsqu'on ajoute ou retire des skills ou des commandes utilisateur.
- Valider les chemins, le frontmatter et les scripts concernés après chaque changement.

