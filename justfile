# List the available commands (also the default when you run `just`).
list:
    @just --list

# Validate the plugin manifest and components with Claude Code.
validate:
    claude plugin validate .

# Load this plugin in a Claude Code session.
launch:
    claude --plugin-dir .

# Split the LangChain recap into numbered Markdown slides.
split-slides:
    python3 scripts/split_slides.py data/langchain-recap-5mn.md
