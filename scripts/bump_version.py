#!/usr/bin/env python3

import argparse
import json
import subprocess
import sys
from pathlib import Path


def bump_version(version: str, part: str) -> str:
    numbers = version.split(".")
    if len(numbers) != 3 or any(not n.isdigit() for n in numbers):
        raise ValueError(f"Invalid semantic version: {version!r}")

    major, minor, patch = (int(n) for n in numbers)

    if part == "major":
        return f"{major + 1}.0.0"
    if part == "minor":
        return f"{major}.{minor + 1}.0"
    if part == "patch":
        return f"{major}.{minor}.{patch + 1}"

    raise ValueError(
        f"Unsupported bump type: {part!r}. Use major, minor or patch.")


def update_version(path: Path, new_version: str) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    if "version" not in data:
        raise KeyError(f"Missing version field in {path}")
    data["version"] = new_version
    path.write_text(json.dumps(
        data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    argv = sys.argv[1:]
    parser = argparse.ArgumentParser(
        description="Bump the plugin version and create a matching git tag.")
    parser.add_argument("--plugin-path", type=Path, default=Path(
        "plugins/formation-ia-agentique"), help="Plugin directory to update.")
    parser.add_argument(
        "--part", choices=["major", "minor", "patch"], default="patch", help="Version bump type.")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview the updated version and tag without modifying files or Git tags.")
    args = parser.parse_args(argv)

    plugin_dir = args.plugin_path.resolve()
    metadata_path = plugin_dir / "plugin.json"
    claude_path = plugin_dir / ".claude-plugin" / "plugin.json"

    if not metadata_path.exists():
        raise FileNotFoundError(f"Plugin manifest not found: {metadata_path}")

    current_version = json.loads(
        metadata_path.read_text(encoding="utf-8"))["version"]
    new_version = bump_version(current_version, args.part)
    tag_name = f"v{new_version}"

    if args.dry_run:
        print(f"Current version: {current_version}")
        print(f"Next version:    {new_version}")
        print(f"Suggested Git tag: {tag_name}")
        return

    update_version(metadata_path, new_version)
    if claude_path.exists():
        update_version(claude_path, new_version)

    # Output the new version so callers (Makefile/justfile) can act on it.
    print(new_version)


if __name__ == "__main__":
    main()
