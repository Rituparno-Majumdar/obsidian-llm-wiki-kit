"""
Vault linter for obsidian-llm-wiki-kit.

Checks for orphan pages, broken wikilinks, missing frontmatter, and
pages absent from wiki/index.md.

Author: obsidian-llm-wiki-kit
"""

import re
from pathlib import Path
from datetime import date

import click
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

REQUIRED_FRONTMATTER = {
    "concept": ["title", "type", "tags", "created", "last_updated"],
    "entity": ["title", "type", "subtype", "tags", "created", "last_updated"],
    "book": ["title", "type", "author", "tags", "status", "created", "last_updated"],
    "article": ["title", "type", "tags", "url", "created", "last_updated"],
    "paper": ["title", "type", "tags", "created", "last_updated"],
    "research": ["title", "type", "tags", "source_file", "created", "last_updated"],
}

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+?)(?:[|#][^\]]*?)?\]\]")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
TYPE_RE = re.compile(r"^type:\s*(.+)$", re.MULTILINE)


def extract_wikilinks(text: str) -> set[str]:
    return {m.group(1).strip() for m in WIKILINK_RE.finditer(text)}


def extract_frontmatter_type(text: str) -> str | None:
    fm = FRONTMATTER_RE.match(text)
    if not fm:
        return None
    m = TYPE_RE.search(fm.group(1))
    return m.group(1).strip() if m else None


def get_frontmatter_keys(text: str) -> set[str]:
    fm = FRONTMATTER_RE.match(text)
    if not fm:
        return set()
    return {line.split(":")[0].strip() for line in fm.group(1).splitlines() if ":" in line}


def title_to_filename(title: str) -> str:
    return title.replace("/", "-").strip()


@click.command()
@click.argument("vault_path", type=click.Path(exists=True, file_okay=False))
@click.option("--fix", is_flag=True, help="Create stub pages for missing wikilink targets.")
@click.option("--dry-run", is_flag=True, help="Preview actions without writing files.")
def main(vault_path: str, fix: bool, dry_run: bool) -> None:
    """Audit an obsidian-llm-wiki-kit vault for structural issues."""
    vault = Path(vault_path)
    wiki = vault / "wiki"

    if not wiki.exists():
        console.print(f"[red]No wiki/ directory found at {vault}[/red]")
        raise SystemExit(1)

    md_files = list(wiki.rglob("*.md"))
    page_names = {f.stem for f in md_files}

    orphans: list[str] = []
    broken_links: list[tuple[str, str]] = []
    missing_fm: list[tuple[str, list[str]]] = []
    absent_from_index: list[str] = []

    index_text = (wiki / "index.md").read_text(encoding="utf-8") if (wiki / "index.md").exists() else ""
    index_links = extract_wikilinks(index_text)

    incoming: dict[str, int] = {f.stem: 0 for f in md_files}

    for md in md_files:
        if md.name in ("index.md", "log.md", "overview.md"):
            continue
        text = md.read_text(encoding="utf-8")
        links = extract_wikilinks(text)

        for link in links:
            name = title_to_filename(link)
            if name in incoming:
                incoming[name] += 1
            elif name not in ("index", "log", "overview"):
                broken_links.append((md.stem, link))

        page_type = extract_frontmatter_type(text)
        if page_type and page_type in REQUIRED_FRONTMATTER:
            present = get_frontmatter_keys(text)
            missing = [k for k in REQUIRED_FRONTMATTER[page_type] if k not in present]
            if missing:
                missing_fm.append((md.stem, missing))

        if md.stem not in index_links and md.name not in ("index.md", "log.md", "overview.md"):
            absent_from_index.append(md.stem)

    for name, count in incoming.items():
        if count == 0 and name not in ("index", "log", "overview"):
            orphans.append(name)

    _print_report(md_files, orphans, broken_links, missing_fm, absent_from_index)

    if fix and broken_links:
        _fix_broken_links(wiki, broken_links, dry_run)


def _print_report(
    md_files: list[Path],
    orphans: list[str],
    broken_links: list[tuple[str, str]],
    missing_fm: list[tuple[str, list[str]]],
    absent_from_index: list[str],
) -> None:
    total = len(md_files)
    console.print()
    console.print(
        f"[bold]{total} total pages[/bold] | "
        f"[yellow]{len(orphans)} orphans[/yellow] | "
        f"[red]{len(broken_links)} broken links[/red] | "
        f"[magenta]{len(missing_fm)} frontmatter issues[/magenta] | "
        f"[blue]{len(absent_from_index)} absent from index[/blue]"
    )
    console.print()

    if orphans:
        t = Table("Orphan Pages", box=box.SIMPLE, style="yellow")
        for o in sorted(orphans):
            t.add_row(o)
        console.print(t)

    if broken_links:
        t = Table("Source Page", "Broken Link", box=box.SIMPLE, style="red")
        for src, link in sorted(broken_links):
            t.add_row(src, link)
        console.print(t)

    if missing_fm:
        t = Table("Page", "Missing Fields", box=box.SIMPLE, style="magenta")
        for page, fields in sorted(missing_fm):
            t.add_row(page, ", ".join(fields))
        console.print(t)

    if absent_from_index:
        t = Table("Absent from wiki/index.md", box=box.SIMPLE, style="blue")
        for p in sorted(absent_from_index):
            t.add_row(p)
        console.print(t)


def _fix_broken_links(wiki: Path, broken_links: list[tuple[str, str]], dry_run: bool) -> None:
    targets = {link for _, link in broken_links}
    for target in sorted(targets):
        stub_path = wiki / "concepts" / f"{title_to_filename(target)}.md"
        if stub_path.exists():
            continue
        today = date.today().isoformat()
        content = f"""---
title: "{target}"
type: concept
native_term: ""
tags: []
created: {today}
last_updated: {today}
---

## Core Idea

*Stub page — created automatically by lint_vault.py. Fill in content.*

## Why It Matters

## Connections

## Sources
"""
        if dry_run:
            console.print(f"[dim]dry-run:[/dim] would create stub → {stub_path.relative_to(wiki.parent)}")
        else:
            stub_path.write_text(content, encoding="utf-8")
            console.print(f"[green]created stub[/green] → {stub_path.relative_to(wiki.parent)}")


if __name__ == "__main__":
    main()
