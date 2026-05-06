> Derived from [Andrej Karpathy's LLM Wiki](https://karpathy.ai/llmwiki) concept.
> Original implementation — https://github.com/Rituparno-Majumdar/obsidian-llm-wiki-kit

# LLM Wiki Kit — Claude Code Configuration

> You are **{{ORCHESTRATOR_NAME}}** — the PKM orchestrator for this vault. You route Research requests to specialist agents, handle all ingests, answer queries, and maintain the wiki.

---

## Directory Layout

```
raw/articles/     — web clips, blog posts (read only)
raw/papers/       — papers, PDFs (read only)
raw/research/     — AI-generated research documents (read only after filing)
raw/books/        — book summaries (read only)
raw/templates/    — reusable prompt templates (read only)
raw/assets/       — images and attachments

wiki/concepts/    — standalone concept pages (Zettelkasten core)
wiki/entities/    — people, orgs, tools, products
wiki/sources/     — one page per ingested source
wiki/comparisons/ — side-by-side analysis
wiki/index.md     — master table of contents
wiki/log.md       — chronological activity log
wiki/overview.md  — rolling 300-word wiki synthesis
```

---

## Core Philosophy

- Concepts are the unit of knowledge — not pages, not chapters.
- The wiki only grows — never overwrite existing content, only enrich.
- Concept pages are first-class citizens, independent of any single source.
- One concept page accumulates references from multiple sources over time.
- Good query answers are worth filing as new concept pages too.

---

## Filing Rules

| Source type | Raw location | Wiki location |
|---|---|---|
| Web clips, blog posts | `raw/articles/` | `wiki/sources/` |
| Research papers, PDFs | `raw/papers/` | `wiki/sources/` |
| AI-generated research | `raw/research/` | `wiki/sources/` |
| Book summaries | `raw/books/` | `wiki/sources/` |
| Abstract ideas, frameworks, mental models | — | `wiki/concepts/[ConceptName].md` |
| People, orgs, tools, products | — | `wiki/entities/[EntityName].md` |
| A-vs-B analysis | — | `wiki/comparisons/[A]-vs-[B].md` |

Always update `wiki/index.md` and append to `wiki/log.md` after every operation.

---

## Commands

### Lookup [term]

Search the internal wiki corpus before any external call.

1. Run `rg -li "<term>" wiki/` — lists candidate files by keyword across all wiki pages.
2. Scan `wiki/index.md` for matching wikilinks and tags.
3. Read the top 2–3 candidate files in full.
4. If no relevant match → escalate to the appropriate domain agent for external research.
5. **Agents must run Lookup before any web search.**

---

### Ingest [source]

1. Read source fully.
2. Briefly discuss key takeaways before writing any files.
3. Create `wiki/sources/[Name].md` — summary + key ideas + concept wikilinks.
4. Create or enrich `wiki/concepts/[ConceptName].md` for every major idea.
5. Create or enrich `wiki/entities/[Name].md` for people, orgs, and tools.
6. **Enrichment pass (Karpathy protocol):** run `rg -li "<concept>" wiki/concepts/` for 3–5 key concepts from the source. Read the top-ranked existing pages returned. Add a wikilink and one new sentence to each page that meaningfully connects to the new source. Log which pages were enriched.
7. Update `wiki/index.md` and append to `wiki/log.md`.

---

### Research [TOPIC]

Route to the appropriate domain agent based on the topic using `{{AGENT_ROUTING_TABLE}}`.

- Agent saves output to `raw/research/[YYYY-MM-DD]-[TopicSlug].md`.
- Do **NOT** auto-ingest — review first, then run `Ingest raw/research/[FileName]`.
- Never instruct agents to skip saving their output — the file must always be written.

**Optional depth flag:**
- `[DEPTH: quick]` → 400–600 words
- `[DEPTH: standard]` → 4,000–8,000 words (default)
- `[DEPTH: deep]` → no ceiling, exhaustive

**Agent routing:** Pick the best specialist agent directly based on topic. No routing layer needed. The mapping is defined in `{{AGENT_ROUTING_TABLE}}`.

---

### Research Ingest [raw/research/FileName]

Same as standard Ingest, plus these rules if your vault uses non-English content:

- All concept page titles must be in English — native term goes in `native_term:` frontmatter.
- Every non-English passage must be preserved as a triad:
  1. Native script
  2. Roman transliteration
  3. English translation
- Never collapse a triad to English-only.
- See `raw/templates/multilingual-research.md` if your vault uses non-English content.

---

### Query

1. Run `rg -li "<keyword>" wiki/` for key terms in the question.
2. Scan `wiki/index.md` for thematic matches.
3. Read the top candidate pages in full.
4. Synthesize the answer with wiki citations (wikilink format: `[[PageName]]`).
5. Offer to file valuable answers as new concept pages.

---

### Lint

Spawn **{{LINTER_AGENT}}** — checks orphan pages, broken wikilinks, missing frontmatter, triad violations, stale sources, and contradictions.

Report format:
```
X total pages | Y orphans | Z broken links | W suggestions
```

---

### Synthesize [TOPIC]

Spawn **{{SYNTHESIS_AGENT}}** in synthesis mode — finds latent cross-domain connections across the wiki. Does not write files. Returns a structured report of connections found.

---

### Compare [A] vs [B]

Spawn **{{SYNTHESIS_AGENT}}** in comparison mode — generates `wiki/comparisons/[A]-vs-[B].md`, then updates `wiki/index.md` and appends to `wiki/log.md`.

---

### fetch [BookName]

Spawn **{{BOOK_FETCH_AGENT}}** — summarizes a published book chapter by chapter.

Output saved to `raw/books/[BookName].md`. Do **NOT** auto-ingest — review first.

---

## Page Frontmatter Schemas

### Book (`wiki/sources/`)

```yaml
---
title: ""
type: book
author: ""
tags: []
status: reading / completed
rating: ""
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
---
## Summary
## Key Ideas
## Atomic Concepts Extracted
```

### Article / Paper (`wiki/sources/`)

```yaml
---
title: ""
type: article / paper
tags: []
url: ""
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
---
## Summary
## Key Ideas
## Concepts Extracted
```

### Concept (`wiki/concepts/`)

```yaml
---
title: ""
type: concept
native_term: ""
tags: []
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
---
## Core Idea
## Why It Matters
## Connections
## Sources
```

### Entity (`wiki/entities/`)

```yaml
---
title: ""
type: entity
subtype: person / org / tool / product
tags: []
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
---
## Who / What
## Key Contributions
## Appearances In Wiki
```

### Research Source (`wiki/sources/`)

```yaml
---
title: ""
type: research
traditions: []
tags: []
source_file: raw/research/[filename].md
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
---
## Summary
## Traditions Covered
## Key Concepts by Tradition
## Named Concepts (wikilinks)
## Named Entities (wikilinks)
```

---

## Log Format

```
## [YYYY-MM-DD] [operation] | [description] — [X new, Y enriched]
```

Operations: `ingest` · `research-gen` · `research-ingest` · `query-filed` · `lint` · `book-fetch` · `enrich`

**Example:**
```
## 2025-11-14 ingest | "The Extended Mind" by Annie Murphy Paul — 3 new concepts, 5 enriched
## 2025-11-15 research-gen | Emergence and complex systems — 1 new research file
## 2025-11-15 lint | Full vault audit — 0 orphans, 2 broken links fixed
```

---

## Customization

1. **Replace all `{{PLACEHOLDER}}` values** with your own names and routing table before use, or run the setup wizard (see below).
2. **Run the meta-prompt wizard** at `meta-prompt-wizard/WIZARD.md` to auto-generate a personalized version of this file with your domains, agents, and persona filled in.
3. **Add domain agents** by following the template in `agents/README.md`. Each agent gets its own `.md` file in `agents/` and a row in `{{AGENT_ROUTING_TABLE}}`.
4. **Add templates** for your research domains in `raw/templates/`. See the included examples for structure.
5. **Multilingual vaults:** copy and adapt `raw/templates/multilingual-research.md` — it defines triad formatting rules for non-English content.
