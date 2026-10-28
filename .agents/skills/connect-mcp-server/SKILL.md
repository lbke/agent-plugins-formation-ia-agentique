---
name: connect-mcp-server
description: "Connect an MCP server to a plugin"
---

## Find and deploy the MCP server

**The MCP server lives in a separate project**, this skills only indicates the architecture, so you may need to require the developer's assistance to actually run the commands.

Currently this project reuses the same MCP server for all plugins: https://github.com/lbke/agent-plugins-mcp-server

Alpic is the official platform behind the Skybridge MCP framework it uses, but domain configuration is not free.

So instead we use Vercel:
https://docs.skybridge.tech/ship/deploy#vercel

```sh
pnpm run build
pnpx vercel deploy --prebuilt
```

## MCP json in this repo

In this repo, the `mcp.json` handles the connection to the deployed MCP server.

## Reference

https://agent-plugins.org/client-implementers/mcp-runtime
https://agent-plugins.org/plugin-authors/mcp-servers
