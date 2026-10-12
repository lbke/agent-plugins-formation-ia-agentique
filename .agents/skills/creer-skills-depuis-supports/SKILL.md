---
name: creer-skills-depuis-supports
description: Transformer des supports de formation en skills opérationnelles publiées dans un plugin, en respectant les consignes éditoriales et techniques du dépôt.
---

# Transformer des supports de formation en skills

Utilise cette skill pour créer ou mettre à jour des skills destinées aux utilisateurs du plugin à partir des supports de formation stockés dans `data/`.

1. Lire les diapositives dans l'ordre et noter leur sujet et leurs dépendances.
2. Regrouper les diapositives qui servent un même objectif opérationnel. Créer un skill par cas d'usage autonome plutôt qu'un skill généraliste qui résume toute la formation.
3. Parcourir l'ensemble des diapositives avant de conclure : chaque section utile doit être reprise dans un skill ou identifiée comme simple titre, transition ou contenu sans procédure exploitable.
4. Rédiger les skills dans la langue du support et en suivant le format attendu par Claude (`SKILL.md` avec frontmatter `name` et `description`).
5. Donner des étapes concrètes, les prérequis, les vérifications et les erreurs fréquentes. Ne pas présenter des versions, offres gratuites, interfaces ou tarifs susceptibles d'évoluer comme des faits permanents : inviter à vérifier la documentation actuelle du fournisseur.
6. Corriger les erreurs techniques des supports plutôt que de les reproduire. Ne jamais inventer une exécution, une vérification ou une garantie.
7. Ignorer les éléments purement organisationnels du guide pratique : dates, planning, contact, règles internes, procédures administratives ou sections de logistique. Les skills ne doivent retenir que les éléments réutilisables comme des actions, diagnostics, validations ou mises à niveau à faire avant le cours.
8. Quand un guide pratique contient des sections de prérequis, les transformer en skills de mise en route plutôt qu'en un simple résumé. Par exemple, un guide qui recommande « mettre Python en place avant la formation » peut devenir des skills comme `demarrer-avec-python-pour-ia-agentique`, `valider-pre-requis-langchain` ou `preparer-environnement-developpement-langchain`.
9. Chaque skill doit toujours répondre à une question concrète : « quand utiliser ce skill ? », « quels sont les prérequis ? », « comment le vérifier ? », « quelles erreurs fréquentes éviter ? ».
10. Préférer des skills ciblés au niveau « mise en route » et « validation de niveau » plutôt que des synthèses trop larges. Un guide administratif ou de déroulé ne doit pas devenir un skill « tout-en-un » ; le contenu utile est souvent réparti entre plusieurs compétences indépendantes.

## Exemple de transformation depuis un guide pratique

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

## Règles techniques

- Utiliser en priorité LangChain dans les skills, sauf si l'utilisateur veut explicitement créer des applications LangGraph.
- Même pour LangChain, utiliser le CLI `langgraph-cli` pour créer une application complète avec un serveur web et la déployer.
- Consulter [les préférences LangChain et LangGraph](references/langchain.md) pour les précisions propres à la formation.
- Ajouter un petit script seulement lorsqu'il automatise une vérification directement liée au cas d'usage du skill. Le script doit avoir une interface documentée, fonctionner sans dépendances inutiles, signaler clairement les erreurs, ne jamais afficher de secrets et ne jamais modifier ou transmettre les identifiants de l'utilisateur.
- Les skills publiées résident sous `plugins/<nom-du-plugin>/skills/<nom-du-skill>/`. Les skills internes de développement résident sous `.agents/skills/` et ne doivent pas être copiées dans le plugin.
- Mettre à jour le README lorsqu'on ajoute ou retire des skills publiées ou des commandes utilisateur.
- Valider les chemins, le frontmatter et les scripts concernés après chaque changement.
