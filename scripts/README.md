# Scripts

Optional helper scripts. Not required to use the system — the LLM handles most operations. These are for users who want command-line utilities.

## lint_vault.py

Audits a vault for structural issues: orphan pages, broken wikilinks, missing frontmatter fields, and pages absent from `wiki/index.md`.

```bash
python scripts/lint_vault.py <path-to-vault>
python scripts/lint_vault.py <path-to-vault> --fix      # create stubs for broken wikilink targets
python scripts/lint_vault.py <path-to-vault> --dry-run  # preview without writing
```

## new_concept.py

Creates a new concept page with correct frontmatter and today's date.

```bash
python scripts/new_concept.py <path-to-vault> "Concept Name"
python scripts/new_concept.py <path-to-vault> "Concept Name" --dry-run
```

## Requirements

```bash
pip install click rich
```
