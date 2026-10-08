#!/usr/bin/env python3

import argparse
import zipfile
from pathlib import Path


def package_plugin(plugin_path: Path, output_path: Path) -> Path:
    plugin_path = plugin_path.resolve()
    if not plugin_path.exists():
        raise FileNotFoundError(f"Plugin directory not found: {plugin_path}")
    if not plugin_path.is_dir():
        raise NotADirectoryError(
            f"Plugin path is not a directory: {plugin_path}")

    output_path = output_path.resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for file_path in sorted(plugin_path.rglob("*")):
            if file_path.is_dir():
                continue
            archive.write(file_path, arcname=str(
                file_path.relative_to(plugin_path.parent)))

    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Package a plugin directory into a ZIP archive for direct download or GitHub release publishing."
    )
    parser.add_argument(
        "--plugin-path",
        type=Path,
        default=Path("plugins/formation-ia-agentique"),
        help="Path to the plugin directory to zip.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("dist/formation-ia-agentique.zip"),
        help="Where to write the ZIP archive.",
    )
    args = parser.parse_args()

    output = package_plugin(args.plugin_path, args.output)
    print(f"Created archive: {output}")


if __name__ == "__main__":
    main()
