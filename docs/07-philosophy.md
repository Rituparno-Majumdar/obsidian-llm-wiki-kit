# Philosophy — Why This System Works the Way It Does

---

## The Problem This Solves

Most people who read a lot don't retain or connect what they read. Notes pile
up in apps, browser tabs multiply, highlights get exported and forgotten.
The knowledge is technically "stored" but practically inaccessible — you
can't reason with a pile of highlights.

This system is an attempt to solve that problem structurally, not through
discipline or habit, but through architecture.

---

## Andrej Karpathy's LLM Wiki Concept

In early 2024, Andrej Karpathy sketched an idea: give an LLM your raw notes
and ask it to compile them into a structured wiki. The raw notes are chaotic
and personal; the LLM produces clean, interlinked, queryable knowledge.

The insight was that LLMs are excellent at exactly the work humans skip:
writing clean summaries, extracting atomic ideas, linking concepts across
sources, generating frontmatter, maintaining consistent formatting.

This system is a productionized version of that idea. The raw notes live in
`raw/` — unedited, unsorted, as-captured. The wiki in `wiki/` is the
compiled, structured output. The LLM is the compiler.

---

## The Zettelkasten Method

Zettelkasten (German: "slip box") was developed by the sociologist Niklas
Luhmann, who used it to write over 70 books and 400 articles. The core
principle: **the concept, not the source, is the atomic unit of knowledge.**

In a traditional note-taking system, you annotate the book. In a Zettelkasten,
you extract the idea from the book and give it its own standalone note,
connected to other ideas — regardless of where they came from. Over time, the
network of notes becomes capable of generating new ideas through unexpected
connections.

This is why `wiki/concepts/` is the core of this vault. A concept page like
`Cognitive Load.md` accumulates references from cognitive science papers,
design books, philosophy texts, and personal experience — because they all
touch the same idea. The concept grows independent of any single source.

---

## How This System Combines Both

This system runs the Karpathy workflow (LLM as compiler) inside a Zettelkasten
structure (concepts as atoms):

1. **Raw input** goes into `raw/` — unprocessed, preserved.
2. **The LLM ingests** — extracts concepts, identifies entities, writes
   standalone pages.
3. **Concepts accumulate** — each new ingest enriches existing concept pages
   rather than creating isolated source summaries.
4. **The wiki grows as a graph** — Obsidian's graph view shows the
   connections; Lint checks for orphans.

The result is a knowledge base that is queryable, browsable, and genuinely
useful for synthesis — not a graveyard of highlights.

---

## Why Obsidian

Obsidian stores everything as plain Markdown files on your local machine.
No proprietary format, no database, no vendor lock-in. If Obsidian
disappears, your files are still readable with any text editor.

Key properties that make Obsidian right for this system:

- **`[[wikilinks]]`** — the native link format that makes the graph work
- **Graph view** — visual map of concept connections
- **YAML frontmatter** — metadata that Obsidian reads natively (Properties view)
- **Plugin ecosystem** — Dataview, Templater, and others extend the vault
  without touching the core structure
- **Local-first** — sync via iCloud, Obsidian Sync, or Git without lock-in

---

## The Enrichment Loop (Karpathy Protocol)

Every Ingest operation ends with an enrichment pass: for each key concept
extracted from the new source, search the existing wiki for pages that
discuss that concept, read the top match, and add a cross-link plus one new
sentence.

This is the compound interest of knowledge management. The first ingest does
almost nothing — there is nothing to cross-link to. The tenth ingest starts
to feel connected. By the hundredth ingest, concepts have ten or twenty
references from completely different domains, and querying the vault produces
genuinely surprising synthesis.

Without the enrichment pass, each ingest is isolated. The vault fills up
but does not become more intelligent. The cross-linking pass is what makes
the whole greater than the sum of its parts.

---

## Credits

- **Andrej Karpathy** — the original LLM Wiki concept. His 2024 posts and
  discussions on LLMs as personal knowledge compilers inspired this system's
  core workflow.
- **Niklas Luhmann** — the Zettelkasten method, documented in Sönke Ahrens'
  *How to Take Smart Notes* (2017), which remains the best introduction.
- **Sönke Ahrens** — *How to Take Smart Notes* — popularized Luhmann's method
  for a general audience.
- **Implementation** — this repo was built and refined by me, with contributions from the community.

---

## A Note on LLM Agnosticism

This system is deliberately not tied to any single LLM. The same vault
structure and the same commands work with Claude, ChatGPT, Gemini, and
local models. The system prompt is the interface; the LLM is the engine.

If a better model ships tomorrow, you switch the engine without touching
the vault. Your knowledge — the Markdown files in `wiki/` — belongs to you.
