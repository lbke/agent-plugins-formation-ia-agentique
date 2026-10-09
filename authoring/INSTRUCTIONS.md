# Consignes de création et de maintenance du plugin

Ce document est destiné aux agents IA qui font évoluer ce dépôt à partir des ressources de formations de LBKE. 

Il ne constitue pas un skill Claude et ne doit pas être placé sous `skills/` !

## Pour Claude

Documentation Claude pour la création de plugins : https://claude.com/docs/build/overview

Claude veut le nom du plugin en "kebab-case", sans source

Structure du fichier plugin.json: https://code.claude.com/docs/en/plugins/manifest-reference

## Pour ChatGPT

Documentation ChatGPT pour la création de plugins : https://developers.openai.com/plugins

ChatGPT respecte le standard "Agent Plugins" : https://agent-plugins.org/

Pour soumettre: 
https://developers.openai.com/plugins/deploy/submission

Champs spécifiques du schéma agent plugins (./plugin.json à la racine de chaque plugin, pas celui de Claude Code par contre) pour les Client Extensions : 

- Champs génériques : https://agent-plugins.org/plugin-authors/client-extensions

- Échantillon du schéma OpenAI : https://github.com/openai/plugins/blob/main/.agents/skills/plugin-creator/references/plugin-json-spec.md

- Schéma complet OpenAI : https://developers.openai.com/plugins/deploy/submission#agent-plugins-format

- Règles de validation : https://developers.openai.com/plugins/deploy/submission-errors



## Transformer des supports de formation en skills

1. Lire les diapositives dans l'ordre et noter leur sujet et leurs dépendances.
2. Regrouper les diapositives qui servent un même objectif opérationnel. Créer un skill par cas d'usage autonome plutôt qu'un skill généraliste qui résume toute la formation.
3. Parcourir l'ensemble des diapositives avant de conclure : chaque section utile doit être reprise dans un skill ou identifiée comme simple titre, transition ou contenu sans procédure exploitable.
4. Rédiger les skills dans la langue du support et en suivant le format attendu par Claude (`SKILL.md` avec frontmatter `name` et `description`).
5. Donner des étapes concrètes, les prérequis, les vérifications et les erreurs fréquentes. Ne pas présenter des versions, offres gratuites, interfaces ou tarifs susceptibles d'évoluer comme des faits permanents : inviter à vérifier la documentation actuelle du fournisseur.
6. Corriger les erreurs techniques des supports plutôt que de les reproduire. Ne jamais inventer une exécution, une vérification ou une garantie.
7. Ignorer les éléments purement organisationnels du guide pratique : dates, planning, contact, règles internes, procédures administratives ou sections de logistique. Les skills ne doivent retenir que les éléments réutilisables comme des actions, diagnostics, validations ou mises à niveau à faire avant le cours.
8. Quand un guide pratique contient des sections de prérequis, les transformer en skills de mise en route plutôt qu'en un simple résumé. Par exemple, un guide qui recommande “mettre Python en place avant la formation” peut devenir des skills comme `demarrer-avec-python-pour-ia-agentique`, `valider-pre-requis-langchain` ou `preparer-environnement-developpement-langchain`.
9. Chaque skill doit toujours répondre à une question concrète : “quand utiliser ce skill ?”, “quels sont les prérequis ?”, “comment le vérifier ?”, “quelles erreurs fréquentes éviter ?”.
10. Préférer des skills ciblés au niveau “mise en route” et “validation de niveau” plutôt que des synthèses trop larges. Un guide administratif ou de déroulé ne doit pas devenir un skill “tout-en-un” ; le contenu utile est souvent réparti entre plusieurs compétences indépendantes.

### Exemple de transformation depuis un guide pratique

À partir d'un guide de formation, on peut extraire les éléments suivants :

- les prérequis techniques à vérifier avant la formation ;
- les outils nécessaires à l'environnement de travail ;
- les bases Python à maîtriser avant d'entrer dans les frameworks ;
- les vérifications minimales pour décider si l'apprenant est prêt.

Dans ce dépôt, cela donne des skills de type :

- `demarrer-avec-python-pour-ia-agentique` : aider un apprenant à installer et valider Python avant une formation IA agentique ;
- `valider-pre-requis-langchain` : mesurer si les bases Python et l'environnement sont suffisants pour suivre un cours LangChain/LangGraph ;
- `preparer-environnement-developpement-langchain` : préparer un environnement de travail cohérent avant de lancer un projet.

Cette logique évite de recopier le cadre administratif du guide et garde le contenu utile sous une forme exploitable par un assistant ou un apprenant.

## Scripts d'aide

Ajouter un petit script seulement lorsqu'il automatise une vérification directement liée au cas d'usage du skill. Le script doit avoir une interface documentée, fonctionner sans dépendances inutiles, signaler clairement les erreurs, ne jamais afficher de secrets et ne jamais modifier ou transmettre les identifiants de l'utilisateur.

## Organisation et validation

- Les compétences livrées aux utilisateurs résident sous `plugins/<nom-du-plugin>/skills/<nom-du-skill>/`.
- Les consignes de contribution et les documents internes résident hors des dossiers de plugins, par exemple dans `authoring/`.
- Mettre à jour le README lorsqu'on ajoute ou retire des skills ou des commandes utilisateur.
- Valider les chemins, le frontmatter et les scripts concernés après chaque changement.

