# List the available commands (also the default when you run `just`).
list:
    @just --list

# Validate the plugin manifest and components with Claude Code.
validate-claude:
    claude plugin validate .

# Load this plugin in a Claude Code session.
launch-claude:
    claude --plugin-dir plugins/formation-ia-agentique

# Package the plugin as a ZIP archive for direct installation or GitHub release assets.
# Example: just zip-plugin formation-ia-agentique
zip-plugin plugin_name='formation-ia-agentique':
    python3 scripts/package_plugin.py --plugin-path "plugins/{{plugin_name}}" --output "dist/{{plugin_name}}.zip"

# Bump the plugin version in both manifests and create the matching Git tag.
# Example: just bump-version patch
bump-version part='patch':
    python3 scripts/bump_version.py --plugin-path "plugins/formation-ia-agentique" --part {{part}}

# Split the LangChain recap into numbered Markdown slides.
# For instance data/langchain-recap-5mn.md
# @see https://just.systems/man/en/recipe-parameters.html
split-slides slidev_file:
    python3 scripts/split_slides.py {{slidev_file}}
