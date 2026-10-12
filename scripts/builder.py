#!/usr/bin/env python3

from pathlib import Path


def iter_plugin_dirs(plugin_path: Path) -> list[Path]:
    plugin_root = plugin_path.resolve()
    if not plugin_root.exists():
        raise FileNotFoundError(f"Plugin path not found: {plugin_root}")

    if (plugin_root / "plugin.json").exists():
        return [plugin_root]

    plugin_dirs = sorted(
        child for child in plugin_root.iterdir()
        if child.is_dir() and (child / "plugin.json").exists()
    )
    if not plugin_dirs:
        raise FileNotFoundError(
            f"No plugin manifests found under {plugin_root}."
        )
    return plugin_dirs
