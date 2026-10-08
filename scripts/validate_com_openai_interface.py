#!/usr/bin/env python3

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


def load_json(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(f"Missing JSON file: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc


def get_interface_from_plugin(plugin_data: dict[str, Any]) -> dict[str, Any]:
    extensions = plugin_data.get("extensions") or {}
    openai = extensions.get("com.openai") or {}
    interface = openai.get("interface") or {}
    if not isinstance(interface, dict):
        return {}
    return interface


def validate_string_constraints(value: Any, schema: dict[str, Any], path: str) -> list[str]:
    errors: list[str] = []
    if not isinstance(value, str):
        return [f"{path} must be a string"]

    if "minLength" in schema and len(value) < schema["minLength"]:
        errors.append(
            f"{path} is shorter than {schema['minLength']} characters")
    if "maxLength" in schema and len(value) > schema["maxLength"]:
        errors.append(f"{path} exceeds {schema['maxLength']} characters")
    if "pattern" in schema and re.match(schema["pattern"], value) is None:
        errors.append(f"{path} does not match the expected pattern")
    if schema.get("format") == "uri":
        parsed = urlparse(value)
        if parsed.scheme != "https" or not parsed.netloc:
            errors.append(f"{path} must be a valid HTTPS URL")
    return errors


def validate_schema(data: Any, schema: dict[str, Any], path: str = "$") -> list[str]:
    errors: list[str] = []

    if "$ref" in schema:
        return errors

    if "type" in schema and schema["type"] == "object":
        if not isinstance(data, dict):
            return [f"{path} must be an object"]

        required = schema.get("required", [])
        for key in required:
            if key not in data:
                errors.append(f"{path}.{key} is required")

        properties = schema.get("properties", {})
        for key, value in data.items():
            if key not in properties:
                if schema.get("additionalProperties") is False:
                    errors.append(f"{path}.{key} is not allowed")
                continue
            errors.extend(validate_schema(
                value, properties[key], f"{path}.{key}"))
        return errors

    if "type" in schema and schema["type"] == "array":
        if not isinstance(data, list):
            return [f"{path} must be an array"]
        if "minItems" in schema and len(data) < schema["minItems"]:
            errors.append(f"{path} has fewer than {schema['minItems']} items")
        if "maxItems" in schema and len(data) > schema["maxItems"]:
            errors.append(f"{path} has more than {schema['maxItems']} items")
        item_schema = schema.get("items", {})
        for idx, item in enumerate(data):
            errors.extend(validate_schema(item, item_schema, f"{path}[{idx}]"))
        return errors

    if "enum" in schema and data not in schema["enum"]:
        errors.append(f"{path} is not one of the allowed values")
        return errors

    if "oneOf" in schema:
        for candidate in schema["oneOf"]:
            candidate_errors = validate_schema(data, candidate, path)
            if not candidate_errors:
                return []
        return [f"{path} does not match any allowed schema variant"]

    if "type" in schema and schema["type"] == "string":
        errors.extend(validate_string_constraints(data, schema, path))
        return errors

    if "properties" in schema and isinstance(data, dict):
        return validate_schema(data, {"type": "object", **schema}, path)

    return []


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate the com.openai interface block using its JSON schema file."
    )
    parser.add_argument(
        "--plugin-path",
        type=Path,
        default=Path("plugins/formation-ia-agentique"),
        help="Plugin directory containing the root plugin.json manifest.",
    )
    parser.add_argument(
        "--schema",
        type=Path,
        default=None,
        help="Optional path to the JSON schema file. Defaults to the plugin schema under schemas/com.openai.interface.schema.json.",
    )
    args = parser.parse_args()

    plugin_dir = args.plugin_path.resolve()
    plugin_data = load_json(plugin_dir / "plugin.json")
    if not args.schema:
        schema_path = plugin_dir / "schemas" / "com.openai.interface.schema.json"
    else:
        schema_path = args.schema.resolve()

    if not schema_path.exists():
        raise FileNotFoundError(f"Schema file not found: {schema_path}")

    schema = load_json(schema_path)
    interface_data = get_interface_from_plugin(plugin_data)

    errors = validate_schema(interface_data, schema)
    if errors:
        print("OpenAI interface validation failed:")
        for item in errors:
            print(f"  - {item}")
        return 1

    print(f"OpenAI interface validation passed for {plugin_dir.name}.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
