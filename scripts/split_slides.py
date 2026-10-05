from pathlib import Path
import argparse


DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "data/langchain-recap-5mn.md"
SEPARATOR = "---\n\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Split a Markdown presentation into numbered slides.")
    parser.add_argument("markdown_file", nargs="?", type=Path, default=DEFAULT_INPUT)
    markdown_file = parser.parse_args().markdown_file

    markdown = markdown_file.read_text(encoding="utf-8")
    if markdown.startswith("---\n"):
        _, frontmatter_end, body = markdown.partition("\n---\n\n")
        if frontmatter_end:
            markdown = body

    slides = [slide.strip() for slide in markdown.split(SEPARATOR) if slide.strip()]
    output_dir = markdown_file.parent / markdown_file.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    for number, slide in enumerate(slides, start=1):
        (output_dir / f"{number:02}.md").write_text(f"{slide}\n", encoding="utf-8")

    print(f"Wrote {len(slides)} slides to {output_dir}")


if __name__ == "__main__":
    main()
