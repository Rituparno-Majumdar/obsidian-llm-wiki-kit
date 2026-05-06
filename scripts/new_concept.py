"""
Create a new concept page with correct frontmatter.

Author: obsidian-llm-wiki-kit
"""

from pathlib import Path
from datetime import date

import click
from rich.console import Console

console = Console()


@click.command()
@click.argument("vault_path", type=click.Path(exists=True, file_okay=False))
@click.argument("concept_name")
@click.option("--dry-run", is_flag=True, help="Preview without writing.")
@click.option("--native-term", default="", help="Native-language term (e.g. Sanskrit, Japanese).")
@click.option("--tags", default="", help="Comma-separated tags.")
def main(vault_path: str, concept_name: str, dry_run: bool, native_term: str, tags: str) -> None:
    """Create a new concept page at wiki/concepts/<ConceptName>.md."""
    vault = Path(vault_path)
    concepts_dir = vault / "wiki" / "concepts"

    if not concepts_dir.exists():
        console.print(f"[red]wiki/concepts/ not found in {vault}[/red]")
        raise SystemExit(1)

    filename = concept_name.replace("/", "-").strip() + ".md"
    output_path = concepts_dir / filename

    if output_path.exists():
        console.print(f"[yellow]Page already exists:[/yellow] {output_path.relative_to(vault)}")
        raise SystemExit(1)

    today = date.today().isoformat()
    tag_list = [t.strip() for t in tags.split(",") if t.strip()]
    tag_yaml = str(tag_list) if tag_list else "[]"

    content = f"""---
title: "{concept_name}"
type: concept
native_term: "{native_term}"
tags: {tag_yaml}
created: {today}
last_updated: {today}
---

## Core Idea

## Why It Matters

## Connections

## Sources
"""

    if dry_run:
        console.print(f"[dim]dry-run:[/dim] would create → {output_path.relative_to(vault)}")
        console.print()
        console.print(content)
    else:
        output_path.write_text(content, encoding="utf-8")
        console.print(f"[green]Created[/green] → {output_path.relative_to(vault)}")
        console.print("[dim]Remember to add a wikilink in wiki/index.md[/dim]")


if __name__ == "__main__":
    main()
