#!/usr/bin/env python3

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from builder import iter_plugin_dirs


CLAUDE_MANIFEST_KEYS = {
    "name",
    "displayName",
    "version",
    "description",
    "author",
    "homepage",
    "repository",
    "license",
    "keywords",
    "icon",
    "supportUrl",
    "privacyPolicyUrl",
    "termsOfServiceUrl",
    "documentationUrl",
    "defaultEnabled",
    "dependencies",
    "settings",
    "userConfig",
    "channels",
    "skills",
    "commands",
    "agents",
    "hooks",
    "mcpServers",
    "lspServers",
    "outputStyles",
    "workflows",
    "experimental",
}


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Missing JSON file: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc


def get_openai_interface(agent_data: dict[str, Any]) -> dict[str, Any]:
    """
    Agent plugin "com.openai.interface" is the source of truth 
    for most fields you need to publish a plugin elsewhere
    icons, documentation URLs etc.

    """
    extensions = agent_data.get("extensions") or {}
    openai_extension = extensions.get("com.openai") or {}
    interface = openai_extension.get("interface") or {}
    return interface if isinstance(interface, dict) else {}


def build_sync_map(agent_data: dict[str, Any]) -> dict[str, Any]:
    sync_map: dict[str, Any] = {}
    openai_interface = get_openai_interface(agent_data)

    # Fields that can be defined in both agent plugin default fields and openai interface
    # #agent plugin has priority
    author = agent_data.get("author")
    if isinstance(author, dict) and author.get("name"):
        normalized_author: dict[str, Any] = {"name": author["name"]}
        if author.get("url"):
            normalized_author["url"] = author["url"]
        if author.get("email"):
            normalized_author["email"] = author["email"]
        sync_map["author"] = normalized_author
    homepage = agent_data.get("homepage")
    if homepage is not None:
        sync_map["homepage"] = homepage
    elif openai_interface["websiteURL"]:
        sync_map["homepage"] = openai_interface["websiteURL"]

    # Agent plugin keys
    for claude_key, agent_plugin_key in (
        ("license", "license"),
        ("repository", "repository"),
        ("keywords", "keywords"),
        ("version", "version"),
        ("description", "description")
    ):
        value = agent_data.get(agent_plugin_key)
        if value:
            sync_map[claude_key] = value

    # Open Ai interface keys
    for claude_key, openai_interface_key in (
        ("displayName", "displayName"),
        ("supportUrl", "supportURL"),
        ("privacyPolicyUrl", "privacyPolicyUURL"),
        ("termsOfServiceUrl", "termsOfServiceURL"),
        ("logo", "icon"),
    ):
        value = openai_interface.get(openai_interface_key)
        if value:
            sync_map[claude_key] = value

    return sync_map


def detect_extra_fields(claude_data: dict[str, Any]) -> list[str]:
    extra = []
    for key in claude_data:
        if key not in CLAUDE_MANIFEST_KEYS and key.lower() not in {k.lower() for k in CLAUDE_MANIFEST_KEYS}:
            extra.append(key)
    return extra


def merge_values(base: dict[str, Any], updates: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    changes: list[str] = []
    result = dict(base)

    for key, value in updates.items():
        if key == "author":
            current = result.get("author")
            if not isinstance(current, dict):
                result[key] = value
                changes.append(key)
                continue

            target_author = dict(current)
            if value.get("name") and target_author.get("name") != value.get("name"):
                target_author["name"] = value["name"]
                changes.append("author.name")
            if value.get("url") and target_author.get("url") != value["url"]:
                target_author["url"] = value["url"]
                changes.append("author.url")
            if value.get("email") and target_author.get("email") != value["email"]:
                target_author["email"] = value["email"]
                changes.append("author.email")
            result[key] = target_author
            continue

        if key not in result or result[key] != value:
            result[key] = value
            changes.append(key)

    return result, changes


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Synchronize Claude plugin metadata from the Agent Plugin manifest, using "
            "the com.openai interface as the source of truth for public metadata."
        )
    )
    parser.add_argument(
        "--plugin-path",
        type=Path,
        default=Path("plugins"),
        help="Plugin directory or plugins root to synchronize.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate whether the Claude manifests match the source and exit 1 if any would change.",
    )
    args = parser.parse_args()

    plugin_dirs = iter_plugin_dirs(args.plugin_path)
    failed = False

    for plugin_dir in plugin_dirs:
        agent_path = plugin_dir / "plugin.json"
        claude_path = plugin_dir / ".claude-plugin" / "plugin.json"

        if not agent_path.exists():
            raise FileNotFoundError(
                f"Agent plugin manifest not found: {agent_path}")

        agent_data = load_json(agent_path)
        expected_updates = build_sync_map(agent_data)

        if not claude_path.exists():
            if args.check:
                print(f"Claude manifest is missing: {claude_path}")
                failed = True
                continue
            claude_data: dict[str, Any] = {"name": plugin_dir.name}
        else:
            claude_data = load_json(claude_path)

        merged, changes = merge_values(claude_data, expected_updates)
        extra_fields = detect_extra_fields(claude_data)

        if args.check:
            mismatches = []
            for key, expected_value in expected_updates.items():
                current_value = claude_data.get(key)
                if current_value != expected_value:
                    mismatches.append(
                        f"{key}: expected {expected_value!r}, found {current_value!r}")

            if extra_fields:
                mismatches.extend(
                    f"extra-field: {field}" for field in extra_fields)

            if not mismatches:
                print(
                    f"Claude manifest is already synchronized for {plugin_dir.name}.")
                continue

            print(f"Claude manifest would be updated for {plugin_dir.name}:")
            for item in mismatches:
                print(f"  - {item}")
            failed = True
            continue

        if changes or extra_fields:
            claude_path.parent.mkdir(parents=True, exist_ok=True)
            claude_path.write_text(
                json.dumps(merged, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            print(f"Updated Claude manifest: {claude_path}")
            for change in changes:
                print(f"  - {change}")
            for field in extra_fields:
                print(f"  - extra-field: {field}")
        else:
            print(f"Claude manifest already in sync for {plugin_dir.name}.")

    return 1 if failed else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover - CLI safety net
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
