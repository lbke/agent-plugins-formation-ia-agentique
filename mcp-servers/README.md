# Serveurs MCP des plugins

Chaque plugin de `plugins/` peut avoir son propre serveur MCP, dans `mcp-servers/<nom-du-plugin>/`. Les serveurs sont écrits en Python avec [FastMCP](https://gofastmcp.com) et déployés sur Vercel, **un projet Vercel par serveur**.

| Serveur | Plugin | Outils |
| --- | --- | --- |
| `formation-ia-agentique/` | `plugins/formation-ia-agentique` | `lister-criteres-competences-creation-agent-ia`, `scorer-competences-creation-agent-ia`, `recommander-parcours-ia-agentique` |

## Conventions

Chaque dossier de serveur est **autonome** : Vercel ne déploie que le dossier défini comme « Root Directory », donc un serveur n'importe rien d'un autre dossier du dépôt (ni d'un autre serveur, ni de `plugins/`). Une petite duplication entre serveurs est acceptée.

```
mcp-servers/<nom-du-plugin>/
├── pyproject.toml     # dépendances (uv), [tool.vercel] entrypoint = "app:app"
├── uv.lock
├── .python-version    # 3.12 (version par défaut de Vercel)
├── .vercelignore
├── app.py             # point d'entrée ASGI : app = mcp.http_app(stateless_http=True, ...)
├── server.py          # instance FastMCP : outils, ressources, routes HTTP
├── <domaine>.py       # données et logique métier, sans dépendance à MCP
└── tests/
```

- Noms d'outils en kebab-case français, identiques aux `tools_triggered` des cas de test de `plugin.json`.
- Tous les outils déclarent leurs annotations (`read_only_hint`, `destructive_hint`, `open_world_hint`), exigées par OpenAI.
- Les entrées et sorties sont typées avec Pydantic : FastMCP en déduit `inputSchema`, `outputSchema` et `structuredContent`.
- Mode HTTP sans état (`stateless_http=True`, `json_response=True`) : chaque invocation serverless est indépendante.
- Le fichier `/.well-known/openai-apps-challenge` est servi par une route FastMCP à partir de la variable d'environnement `OPENAI_APPS_CHALLENGE` (pas de dossier `public/`, donc pas de problème de chemin ou de type de contenu).
- Quand un contenu de skill est repris dans un serveur (par exemple les technologies recommandées), le module Python indique le fichier source à garder synchronisé.

## Commandes

```sh
just mcp-test                              # tests de tous les serveurs
just mcp-dev formation-ia-agentique        # serveur local sur http://localhost:8000/mcp
just mcp-inspect formation-ia-agentique    # MCP Inspector sur le serveur local
just mcp-deploy formation-ia-agentique     # déploiement Vercel en production
```

## Déployer sur Vercel

Pour chaque serveur, créez un projet Vercel dont le **Root Directory** est `mcp-servers/<nom-du-plugin>` (interface Vercel, ou `vercel link` lancé depuis ce dossier). Vercel détecte `app.py` et la variable `app` ([runtime Python](https://vercel.com/docs/functions/runtimes/python)).

1. `cd mcp-servers/<nom-du-plugin> && vercel link` (une seule fois).
2. Ajoutez la variable d'environnement `OPENAI_APPS_CHALLENGE` si le plugin est soumis à OpenAI.
3. `just mcp-deploy <nom-du-plugin>`, puis associez un domaine (par exemple `mcp-<nom-du-plugin>.lbke.fr`).
4. Mettez à jour l'URL dans `plugins/<nom-du-plugin>/mcp.json` (`https://<domaine>/mcp`).

## Ajouter un serveur

1. Copiez `formation-ia-agentique/` vers `mcp-servers/<nom-du-plugin>/`, supprimez `.venv/`, renommez le projet dans `pyproject.toml` et le nom du serveur dans `server.py`.
2. Remplacez les modules métier et les outils, puis les tests.
3. Mettez à jour `plugins/<nom-du-plugin>/mcp.json`, les cas de test de `plugin.json` et le tableau ci-dessus.

## Références

- [FastMCP : déploiement HTTP](https://gofastmcp.com/deployment/http)
- [FastMCP : outils](https://gofastmcp.com/servers/tools)
- [Vercel : runtime Python](https://vercel.com/docs/functions/runtimes/python)
- [Exigences MCP d'OpenAI](https://developers.openai.com/plugins/plugin-guidelines#mcp-requirements)
