#!/usr/bin/env python3
"""Check that marketplace plugin names match their plugin manifests."""

import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent
MARKETPLACES = [
    ROOT / ".claude-plugin/marketplace.json",
    ROOT / ".agents/plugins/marketplace.json",
]


def get_marketplace_kind(marketplace_path: Path) -> str:
    path_text = str(marketplace_path)
    if ".claude-plugin" in path_text:
        return "claude"
    if ".agents" in path_text:
        return "agent"
    return "generic"


def get_manifest_path(plugin_root: Path, marketplace_kind: str) -> Path:
    if marketplace_kind == "claude":
        return plugin_root / ".claude-plugin/plugin.json"
    return plugin_root / "plugin.json"


def main() -> int:
    errors = []
    for marketplace_path in MARKETPLACES:
        with marketplace_path.open(encoding="utf-8") as file:
            marketplace = json.load(file)

        marketplace_kind = get_marketplace_kind(marketplace_path)

        for entry in marketplace["plugins"]:
            plugin_path = entry.get("source")
            if isinstance(plugin_path, dict):
                plugin_path = plugin_path.get("path")
            if not plugin_path:
                continue

            plugin_root = (ROOT / plugin_path).resolve()
            manifest_path = get_manifest_path(plugin_root, marketplace_kind)
            if not manifest_path.is_file():
                errors.append(
                    f"{marketplace_path}: plugin manifest not found for {entry['name']}")
                continue

            with manifest_path.open(encoding="utf-8") as file:
                manifest = json.load(file)

            expected_name = manifest.get("name")
            if marketplace_kind == "claude":
                if entry["name"] != expected_name:
                    errors.append(
                        f"{marketplace_path}: marketplace name {entry['name']!r} "
                        f"does not match Claude config {manifest_path}: {expected_name!r}"
                    )
            else:
                if entry["name"] != expected_name:
                    errors.append(
                        f"{marketplace_path}: marketplace name {entry['name']!r} "
                        f"does not match Agent Plugin config {manifest_path}: {expected_name!r}"
                    )

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print("Marketplace and plugin names match per ecosystem.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
