#!/usr/bin/env python3
"""Detect cross-references between the skills of each plugin and draw one PNG graph per plugin.

A reference is any mention of another skill's name (whole word) in the text files
of a skill folder (SKILL.md and references/). Plugins are independent: a skill may
only reference skills of its own plugin, so each plugin is analysed separately.
The PNGs are rendered with Graphviz (`dot` must be installed).

Warnings are printed on stdout:
- a name that looks like a skill but matches none in the same plugin (a backticked
  kebab-case name with at least two hyphens, or a name right after the word "skill"),
  including a skill that only exists in another plugin;
- a known skill name written without backticks: the convention is `skill-name`.
README.md is checked against the skills of all plugins.

Usage:
    python3 scripts/skills_graph.py [--plugin-path plugins] [--output-dir dist]
"""

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

TEXT_SUFFIXES = {".md", ".txt", ".py", ".sh", ".json", ".yaml", ".yml"}

# Kebab-case names that are legitimately mentioned but are not skills.
# Plugin names and names found in plugin manifests (e.g. MCP tools) are added automatically.
NOT_SKILLS = {"agent-service-toolkit"}

KEBAB = r"[a-z0-9]+(?:-[a-z0-9]+){2,}"
BACKTICKED_KEBAB = re.compile(rf"`({KEBAB})`")
AFTER_SKILL_WORD = re.compile(rf"\b(?:skill|skills|compétence)\s+[\"'«“]?\s*({KEBAB})", re.IGNORECASE)


def find_skills(plugin_dir: Path) -> dict[str, Path]:
    """Return {skill_name: skill_dir} for one plugin."""
    return {md.parent.name: md.parent for md in sorted(plugin_dir.glob("skills/*/SKILL.md"))}


def skill_text(skill_dir: Path) -> str:
    parts = []
    for path in sorted(skill_dir.rglob("*")):
        if path.is_file() and path.suffix in TEXT_SUFFIXES:
            parts.append(path.read_text(encoding="utf-8", errors="ignore"))
    return "\n".join(parts)


def find_edges(skills: dict[str, Path]) -> set[tuple[str, str]]:
    patterns = {
        name: re.compile(rf"(?<![\w-]){re.escape(name)}(?![\w-])") for name in skills
    }
    edges = set()
    for source, skill_dir in skills.items():
        text = skill_text(skill_dir)
        for target, pattern in patterns.items():
            if target != source and pattern.search(text):
                edges.add((source, target))
    return edges


def known_non_skills(plugin_root: Path) -> set[str]:
    names = set(NOT_SKILLS)
    for plugin_dir in plugin_root.iterdir():
        if not plugin_dir.is_dir():
            continue
        names.add(plugin_dir.name)
        for manifest in (plugin_dir / "plugin.json", plugin_dir / ".claude-plugin" / "plugin.json"):
            if manifest.is_file():
                names.update(re.findall(rf'"({KEBAB})"', manifest.read_text(encoding="utf-8")))
    return names


def check_mentions(
    files: list[Path], skills: set[str], non_skills: set[str], elsewhere: frozenset[str] = frozenset()
) -> list[str]:
    """Warn about unknown skill-like names and skill names written without backticks."""
    bare = re.compile(
        r"(?<![\w`/.-])(" + "|".join(map(re.escape, sorted(skills, key=len, reverse=True))) + r")(?![\w`/-])"
    )
    warnings = []
    for path in files:
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            where = f"{path}:{line_no}"
            if re.match(r"\s*name\s*:", line):  # frontmatter name field
                continue
            candidates = set(BACKTICKED_KEBAB.findall(line)) | set(AFTER_SKILL_WORD.findall(line))
            for name in sorted(candidates - skills - non_skills):
                if name in elsewhere:
                    warnings.append(f"{where}: skill '{name}' belongs to another plugin, it cannot be referenced here")
                else:
                    warnings.append(f"{where}: unknown skill '{name}'")
            for name in sorted(set(bare.findall(line))):
                warnings.append(f"{where}: write skill name as `{name}` (backticks)")
    return warnings


def to_dot(plugin: str, skills: dict[str, Path], edges: set[tuple[str, str]]) -> str:
    lines = [
        "digraph skills {",
        f'    label="{plugin}"; labelloc=t; fontsize=18;',
        '    rankdir=TB; nodesep=0.4; ranksep=0.6; fontname="Helvetica";',
        '    node [shape=box, style="rounded,filled", fillcolor="#f5f5f5", fontname="Helvetica", fontsize=11];',
        '    edge [color="#555555", arrowsize=0.7];',
    ]
    lines += [f'    "{name}";' for name in sorted(skills)]
    lines += [f'    "{source}" -> "{target}";' for source, target in sorted(edges)]
    lines.append("}")
    return "\n".join(lines)


def render_png(dot_source: str, output: Path) -> None:
    if not shutil.which("dot"):
        raise SystemExit("Graphviz 'dot' not found: install graphviz (e.g. apt install graphviz, brew install graphviz)")
    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["dot", "-Tpng", "-Gdpi=150", "-o", str(output)], input=dot_source, text=True, check=True)


def summary(skills: dict[str, Path], edges: set[tuple[str, str]]) -> list[str]:
    referenced = {target for _, target in edges}
    orphans = sorted(set(skills) - referenced)
    return [
        f"{len(skills)} skills, {len(edges)} references.",
        "Skills referenced by no other skill: " + (", ".join(orphans) or "none"),
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--plugin-path", default="plugins", type=Path)
    parser.add_argument("--output-dir", default=Path("dist"), type=Path, help="Folder for the PNG files")
    args = parser.parse_args()

    plugins = {d.name: find_skills(d) for d in sorted(args.plugin_path.iterdir()) if d.is_dir()}
    plugins = {name: skills for name, skills in plugins.items() if skills}
    if not plugins:
        print(f"No skills found under {args.plugin_path}")
        return 1

    non_skills = known_non_skills(args.plugin_path)
    all_skills = {name for skills in plugins.values() for name in skills}
    total_warnings = 0

    for plugin, skills in plugins.items():
        print(f"== {plugin}")
        elsewhere = frozenset(all_skills - set(skills))
        files = [p for d in skills.values() for p in sorted(d.rglob("*.md"))]
        warnings = check_mentions(files, set(skills), non_skills, elsewhere)
        for warning in warnings:
            print(f"Warning: {warning}")
        total_warnings += len(warnings)

        edges = find_edges(skills)
        output = args.output_dir / f"skills-graph-{plugin}.png"
        render_png(to_dot(plugin, skills, edges), output)
        print("\n".join(summary(skills, edges)))
        print(f"Wrote {output}\n")

    readme = args.plugin_path.parent / "README.md"
    if readme.is_file():
        print("== README.md")
        warnings = check_mentions([readme], all_skills, non_skills)
        for warning in warnings:
            print(f"Warning: {warning}")
        total_warnings += len(warnings)

    print(f"{total_warnings} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
