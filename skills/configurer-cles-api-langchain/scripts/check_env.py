#!/usr/bin/env python3
"""Check required keys in a dotenv-style file without printing secret values."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

KEY_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
ASSIGNMENT_RE = re.compile(
    r"^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*?)\s*$"
)
PLACEHOLDER_RE = re.compile(
    r"^(?:x{3,}|changeme|change_me|your[_ -].*|replace[_ -].*|<.*>)$",
    re.IGNORECASE,
)


def strip_inline_comment(value: str) -> str:
    quote: str | None = None
    escaped = False
    for index, char in enumerate(value):
        if escaped:
            escaped = False
        elif char == "\\" and quote == '"':
            escaped = True
        elif quote:
            if char == quote:
                quote = None
        elif char in {"'", '"'}:
            quote = char
        elif char == "#" and (index == 0 or value[index - 1].isspace()):
            return value[:index].rstrip()
    return value.strip()


def parse_env(path: Path) -> tuple[dict[str, str], list[str]]:
    values: dict[str, str] = {}
    errors: list[str] = []

    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        return values, [f"Impossible de lire {path}: {exc}"]

    for line_number, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        match = ASSIGNMENT_RE.fullmatch(line)
        if not match:
            errors.append(f"Ligne {line_number}: format attendu NOM=valeur.")
            continue

        key, value = match.groups()
        if not KEY_RE.fullmatch(key):
            errors.append(f"Ligne {line_number}: nom de variable invalide.")
            continue
        if key in values:
            errors.append(f"Ligne {line_number}: variable {key} définie plusieurs fois.")
            continue

        value = strip_inline_comment(value)
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        elif value.startswith(("'", '"')) or value.endswith(("'", '"')):
            errors.append(f"Ligne {line_number}: guillemets non appariés pour {key}.")
            continue

        values[key] = value

    return values, errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Vérifie la présence de clés dans un fichier .env sans afficher les valeurs."
    )
    parser.add_argument("--env-file", type=Path, default=Path(".env"))
    parser.add_argument(
        "--required",
        action="append",
        default=[],
        metavar="NOM",
        help="Variable requise (répétable). Par défaut : OPENROUTER_API_KEY.",
    )
    args = parser.parse_args()
    required = args.required or ["OPENROUTER_API_KEY"]

    invalid_required_names = [name for name in required if not KEY_RE.fullmatch(name)]
    if invalid_required_names:
        parser.error("nom de variable requis invalide")

    values, errors = parse_env(args.env_file)
    for error in errors:
        print(f"ERREUR: {error}", file=sys.stderr)

    failed = bool(errors)
    for name in required:
        if name not in values:
            print(f"ERREUR: {name} est absente de {args.env_file}.", file=sys.stderr)
            failed = True
            continue
        value = values[name].strip()
        if not value:
            print(f"ERREUR: {name} est vide.", file=sys.stderr)
            failed = True
        elif PLACEHOLDER_RE.fullmatch(value):
            print(f"ERREUR: {name} contient vraisemblablement un placeholder.", file=sys.stderr)
            failed = True
        else:
            print(f"OK: {name} est définie (valeur masquée).")

    if failed:
        return 1
    print(f"Configuration vérifiée dans {args.env_file}. La validité des clés n'a pas été testée.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
