# List the available commands (also the default when you run `just`).
list:
    @just --list

# Validate the plugin manifest and components with Claude Code.
validate-claude:
    claude plugin validate .

# Load this plugin in a Claude Code session.
launch-claude:
    claude --plugin-dir plugins/formation-ia-agentique

# Split the LangChain recap into numbered Markdown slides.
# For instance data/langchain-recap-5mn.md
# @see https://just.systems/man/en/recipe-parameters.html
split-slides slidev_file:
    python3 scripts/split_slides.py {{slidev_file}}
