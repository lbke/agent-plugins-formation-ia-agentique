---
name: enregistrer-video-chatgpt
description: Automatiser l'enregistrement de la vidéo de démonstration d'un plugin dans ChatGPT desktop (Windows), en rejouant les cas de test positifs et négatifs de plugin.json et en montrant les appels d'outils MCP. Utiliser pour préparer ou refaire la vidéo exigée par la soumission OpenAI (review.demo_recording_url).
---

# Enregistrer la vidéo de démonstration dans ChatGPT desktop

> Statut : **conception, non testée**. Commencer par la phase exploratoire (étape 0) sous Windows avant d'écrire le code, puis mettre à jour cette skill avec ce qui a été observé.

## Contexte

La soumission OpenAI d'un plugin avec serveur MCP demande une vidéo de démonstration (`extensions.com.openai.review.demo_recording_url` dans `plugins/<plugin>/plugin.json`). On y joue les cas de test de `review.test_cases` dans l'app ChatGPT desktop, la seule à gérer les plugins avec MCP (voir la section OpenAI de `AGENTS.md`). Il faut refaire la vidéo à chaque changement des cas de test ou des outils du serveur (`mcp-servers/<plugin>/`).

**Faisabilité** : oui, en semi-automatique, sur une machine **Windows** (ChatGPT desktop n'existe pas sous Linux).

- Automatisable : enchaîner les cas, saisir les prompts, attendre les réponses, déplier l'appel d'outil, filmer l'écran.
- Manuel, une seule fois : se connecter à ChatGPT, installer le plugin en mode développeur, connecter le serveur MCP, autoriser les outils (« toujours autoriser » si l'option existe), fixer la taille et la position de la fenêtre.
- Fragile : les sélecteurs de l'interface ChatGPT changent sans préavis. On isole donc toute la partie interface dans un seul module.
- Conditions d'utilisation : on pilote l'interface pour enregistrer quelques prompts sur son propre compte. L'outil doit rester un enregistreur lancé à la main, jamais un client automatisé utilisé en continu.

## Principe : une vidéo qui fait humaine, sans montage

À notre connaissance, OpenAI ne demande ni montage, ni titres, ni sous-titres : seulement une démonstration réelle des cas de test. Vérifier la [documentation de soumission](https://developers.openai.com/plugins/deploy/submission) avant d'ajouter quoi que ce soit. La vidéo est donc **une seule prise brute**, sans post-traitement. Pour qu'elle ait l'air naturelle :

- Taper le prompt caractère par caractère, avec un délai aléatoire entre les touches (environ 30 à 90 ms) et de petites pauses après la ponctuation. Ne pas coller depuis le presse-papiers.
- Déplacer la souris de façon visible et progressive vers les éléments sur lesquels on clique (zone de saisie, appel d'outil), plutôt que des clics instantanés.
- Laisser le temps de lire : une pause de 1 à 2 s avant d'envoyer, puis 3 à 5 s après la fin de la réponse. Faire défiler doucement si la réponse dépasse l'écran.
- Déplier l'appel d'outil des cas positifs pour montrer la requête et le résultat, comme le ferait un humain qui vérifie.
- Ouvrir une nouvelle conversation pour chaque cas, pour qu'un cas ne dépende pas du précédent.
- Les cas négatifs se jouent de la même façon : on voit simplement qu'aucun outil n'est appelé.

## Architecture proposée

### 1. Scénario : `scripts/demo_scenario.py` (Python standard, sans dépendance)

- Lit `plugins/<plugin>/plugin.json` → `extensions.com.openai.review.test_cases`, avec le même accès JSON que `scripts/validate_agent_plugin_extensions.py`.
- Écrit `dist/demo/<plugin>/scenario.json` : les positifs d'abord, puis les négatifs. Chaque cas contient `id`, `type`, `description`, `prompt` et `tools_triggered` (vide pour un négatif).
- Recette : `just demo-scenario <plugin>`. Exécutable sous Linux.

### 2. Enregistreur Windows : `tools/demo-recorder/` (projet uv autonome)

- Dépendances explicites dans `pyproject.toml` :
  - `pywinauto` (UI Automation, saisie Unicode via `send_keys`, mouvements de souris) ;
  - `mss` + `numpy` (captures pour détecter la fin des réponses) ;
  - `opencv-python-headless` (repérage par images de référence si l'arbre UIA ne suffit pas).
  - La capture vidéo se fait avec `ffmpeg` (gdigrab).
- `chatgpt_driver.py` est **le seul module qui connaît l'interface ChatGPT**. Il expose `focus()`, `nouvelle_conversation()`, `taper(prompt)`, `envoyer()`, `attendre_fin_reponse()`, `deplier_appel_outil()` et `confirmer_outil_si_demande()`.
  - Saisie : `send_keys` caractère par caractère, avec délais aléatoires. Vérifier que les accents et les guillemets français (« ») passent ; sinon, utiliser une saisie Unicode `SendInput`.
  - Fin de réponse : attendre un changement de l'écran, puis qu'il reste stable pendant N secondes, avec un délai maximal. Vérifier aussi, si l'arbre UIA le permet, que le bouton « Arrêter » a disparu.
  - Appel d'outil et confirmation : chercher l'élément UIA par son nom. À défaut, le repérer par correspondance avec une image de référence de `tools/demo-recorder/templates/`, capturée pendant la phase exploratoire.
- `record.py` lit `scenario.json`, démarre `ffmpeg -f gdigrab -framerate 30 -i title="ChatGPT" dist/demo/<plugin>/demo.mp4`, puis joue chaque cas. Il écrit les horodatages dans `dist/demo/<plugin>/timeline.json`, qui servent seulement au diagnostic (pas au montage). Options : `--only <id>` et `--dry-run` (sans ffmpeg).
- Lancement sous Windows : `uv run --project tools/demo-recorder record.py --scenario dist/demo/<plugin>/scenario.json`. Pour `just demo-record <plugin>`, ajouter `set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]` au `justfile`.

### 3. Publication sur Cloudflare R2

- `just demo-upload <plugin>` : `wrangler r2 object put <bucket>/<plugin>/demo.mp4 --file dist/demo/<plugin>/demo.mp4`, dans un [bucket public](https://developers.cloudflare.com/r2/buckets/public-buckets/).
- Une petite fonction Python met à jour `review.demo_recording_url` dans `plugins/<plugin>/plugin.json` (même approche que `scripts/sync_claude_plugin.py` et `scripts/bump_version.py`), puis on lance `just sync-claude` et `just validate-openai-interface`.

### Optionnel : prouver que les bons outils ont été appelés

- Dans `mcp-servers/<plugin>/server.py`, un middleware FastMCP (`on_call_tool`) écrit une ligne de log JSON par appel : nom de l'outil et horodatage, sans les arguments.
- `scripts/demo_report.py` croise les logs Vercel (`vercel logs`) avec `timeline.json` et `tools_triggered`. Il affiche OK/KO par cas, pour savoir s'il faut refaire la prise avant de la soumettre.

## Étapes

0. **Phase exploratoire sous Windows (½ journée).** Relever le raccourci de nouvelle conversation, l'arbre UIA de ChatGPT (`app.window().print_control_identifiers()`), l'aspect d'un appel d'outil MCP et de sa boîte de confirmation. Capturer les images de référence. Si l'arbre UIA n'expose rien d'utile, garder uniquement le repérage par images. Noter les résultats dans cette skill.
1. Préparation manuelle : connexion, plugin installé, serveur MCP connecté, outils autorisés, fenêtre à taille fixe (par exemple 1280×800), notifications Windows désactivées.
2. `just demo-scenario <plugin>`, puis `record.py --only 1 --dry-run`, puis l'enregistrement complet.
3. Regarder la vidéo en entier. Refaire la prise si un cas positif n'a pas appelé son outil ou si un cas négatif en a appelé un.
4. `just demo-upload <plugin>`.

## Vérification

- `demo_scenario.py` : test sur `plugins/formation-langchain/plugin.json`, qui doit donner 5 positifs puis 3 négatifs.
- Enregistreur : une prise d'un seul cas, puis la prise complète. Chaque appel d'outil doit être visible et déplié, et la saisie doit paraître naturelle.
- Publication : l'URL R2 se lit dans un navigateur et `just validate-openai-interface` passe.

## Références

- [Soumission d'un plugin OpenAI (review, test cases, vidéo)](https://developers.openai.com/plugins/deploy/submission)
- [Plugins dans ChatGPT](https://chatgpt.com/plugins)
- [pywinauto](https://pywinauto.readthedocs.io/)
- [ffmpeg gdigrab](https://ffmpeg.org/ffmpeg-devices.html#gdigrab)
- [Cloudflare R2 : buckets publics](https://developers.cloudflare.com/r2/buckets/public-buckets/)
- Skill liée : `connect-mcp-server`
