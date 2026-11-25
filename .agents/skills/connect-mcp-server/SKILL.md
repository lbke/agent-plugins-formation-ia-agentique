---
name: connect-mcp-server
description: "Connect an MCP server to a plugin"
---

## Find and deploy the MCP server

**The MCP servers live in `mcp-servers/<plugin-name>/`**, one self-contained FastMCP (Python) project per plugin. Read `mcp-servers/README.md` for the architecture and conventions.

Each server is deployed as its own Vercel project (Root Directory = `mcp-servers/<plugin-name>`):

```sh
just mcp-test
just mcp-dev <plugin-name>      # http://localhost:8000/mcp
just mcp-deploy <plugin-name>   # requires `vercel link` once in the server folder
```

Deploying and linking Vercel projects needs the developer's account: ask them to run these commands if needed.

Legacy: the plugins first used a shared Skybridge (TypeScript) server, https://github.com/lbke/agent-plugins-mcp-server, deployed at `https://agent-plugins-mcp-server.lbke.fr/mcp`. Point `mcp.json` to the new server only once it is deployed.

## Keep tools and plugin.json in sync

Tool names in `server.py` must match the `tools_triggered` values of the review test cases in `plugins/<plugin-name>/plugin.json`.

## Plugin.json in this repo

Must contain review + demo_url

https://developers.openai.com/plugins/deploy/submission?utm_source=chatgpt.com#configure-onboarding-review-and-publication

## MCP json in this repo

In this repo, the `mcp.json` handles the connection to the deployed MCP server.

https://agent-plugins.org/client-implementers/mcp-runtime
https://agent-plugins.org/plugin-authors/mcp-servers

## MCP requirements for OpenAI

https://developers.openai.com/plugins/plugin-guidelines#mcp-requirements

The domain verification file `/.well-known/openai-apps-challenge` is served by each FastMCP server from the `OPENAI_APPS_CHALLENGE` environment variable of its Vercel project.
