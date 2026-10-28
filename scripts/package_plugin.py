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
            # The glob already handle nested files, skip dirs
            if file_path.is_dir():
                continue
            # TODO: if this makes the script too slow we should remove this directory from the glob earlier
            # rather than skipping from the loop
            if "__pycache__" in file_path.parts or file_path.suffix == ".pyc":
                continue
            # TODO: we may need to skip "evals" too when we introduce them later on,
            # not sure if it makes sense to make them part of the plugin
            # We may even need to use a whitelist of files rather than a blacklist (removing __pycache__ etc.)
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
        help="Path to the plugin directory to zip.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Where to write the ZIP archive.",
    )
    args = parser.parse_args()

    output = package_plugin(args.plugin_path, args.output)
    print(f"Created archive: {output}")


if __name__ == "__main__":
    main()
