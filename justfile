# List the available commands (also the default when you run `just`).
list:
    @just --list

# Validate the plugin manifest and components with Claude Code.
validate-claude:
    claude plugin validate .

# Load a plugin in a Claude Code session.
launch-claude plugin_name='formation-langchain':
    claude --plugin-dir "plugins/{{plugin_name}}"

# Package every plugin as a ZIP archive for direct installation or GitHub release assets.
# Example: just zip-plugin
zip-plugin:
    for plugin_dir in plugins/*; do [ -d "$plugin_dir" ] || continue; plugin_name=$(basename "$plugin_dir"); python3 scripts/package_plugin.py --plugin-path "$plugin_dir" --output "dist/$plugin_name.zip"; done

# Bump every plugin version in both manifests and create the matching Git tag.
# Example: just bump-version patch
bump-version bump='patch':
    # Bump every plugin manifest to the same project version, then commit and tag once.
    new_version=$(python3 scripts/bump_version.py --plugin-path "plugins" --part "{{bump}}" ); git add -A ; git commit -am "Bump version to $new_version" ; git tag -a "v$new_version" -m "Release v$new_version"; git push --tags;

# Synchronize the Claude manifests from the Agent Plugin manifests.
# The root plugin.json stays authoritative; the Claude `name` remains separate.
sync-claude-plugin:
    python3 scripts/sync_claude_plugin.py --plugin-path "plugins"

# Validate the com.openai interface and other extensions metadata 
# against its JSON schema file for every plugin.
validate-openai-interface:
    python3 scripts/validate_agent_plugin_extensions.py --plugin-path "plugins"

# Split the LangChain recap into numbered Markdown slides.
# For instance data/langchain-recap-5mn.md
# @see https://just.systems/man/en/recipe-parameters.html
split-slides slidev_file:
    python3 scripts/split_slides.py {{slidev_file}}

# Regenerate both marketplace plugin lists from the plugin manifests.
update-marketplaces:
    python3 scripts/update_marketplaces.py
