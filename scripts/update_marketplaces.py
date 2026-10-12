#!/usr/bin/env python3

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_DIR = ROOT / "plugins"


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"Expected a JSON object in {path}")
    return data


def plugin_manifests() -> list[tuple[str, dict[str, Any], dict[str, Any]]]:
    result = []
    for plugin_path in sorted(path for path in PLUGIN_DIR.iterdir() if path.is_dir()):
        agent_path = plugin_path / "plugin.json"
        if not agent_path.is_file():
            continue

        claude_path = plugin_path / ".claude-plugin" / "plugin.json"
        if not claude_path.is_file():
            raise FileNotFoundError(
                f"Claude plugin manifest not found for {plugin_path.name}: {claude_path}"
            )
        agent_manifest = load_json(agent_path)
        claude_manifest = load_json(claude_path)
        if not agent_manifest.get("name") or not claude_manifest.get("name"):
            raise ValueError(f"Both plugin manifests need a name: {plugin_path}")
        result.append((plugin_path.name, agent_manifest, claude_manifest))

    return result


def update_marketplace(path: Path, entries: list[dict[str, Any]]) -> None:
    marketplace = load_json(path)
    marketplace["plugins"] = entries
    updated_content = json.dumps(marketplace, indent=2, ensure_ascii=False) + "\n"
    if path.read_text(encoding="utf-8") == updated_content:
        print(f"Already up to date: {path.relative_to(ROOT)}")
        return

    path.write_text(updated_content, encoding="utf-8")
    print(f"Updated {path.relative_to(ROOT)}")


def main() -> int:
    plugins = plugin_manifests()
    agent_plugins = []
    claude_plugins = []

    for directory_name, agent_manifest, claude_manifest in plugins:
        relative_path = f"./plugins/{directory_name}"
        agent_plugins.append(
            {
                "name": agent_manifest["name"],
                "source": {"source": "local", "path": relative_path},
                "policy": {
                    "installation": "AVAILABLE",
                    "authentication": "ON_INSTALL",
                },
                "category": "Education",
            }
        )
        claude_plugins.append(
            {
                "name": claude_manifest["name"],
                "source": relative_path,
                "description": claude_manifest.get(
                    "description", agent_manifest.get("description", "")
                ),
            }
        )

    update_marketplace(ROOT / ".agents/plugins/marketplace.json", agent_plugins)
    update_marketplace(ROOT / ".claude-plugin/marketplace.json", claude_plugins)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
