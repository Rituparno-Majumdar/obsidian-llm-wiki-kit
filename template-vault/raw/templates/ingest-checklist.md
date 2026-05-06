---
title: Ingest Checklist
type: template
tags:
  - template
  - ingest
  - checklist
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
---

# Ingest Checklist

> Run through this checklist for every Ingest operation.
> Copy it into a scratchpad, check off items as you go, then discard.

---

## Phase 1 — Pre-Ingest

- [ ] **Source type identified** — is this an article, paper, book, or
      research file? Determines target folder and frontmatter type.
- [ ] **Source is in the correct raw/ folder** — articles in `raw/articles/`,
      papers in `raw/papers/`, research files in `raw/research/`,
      books in `raw/books/`.
- [ ] **Existing wiki coverage checked** — run `Lookup [topic]` before
      writing anything. If a relevant concept page already exists, plan to
      enrich it rather than duplicate it.
- [ ] **3–5 key concepts identified** — list them before writing. These are
      your atomic units; each one will either create a new concept page or
      enrich an existing one.
- [ ] **Key entities identified** — list any people, organizations, tools,
      or products that warrant an entity page.

**Key concepts for this ingest:**
1. ___________________________________
2. ___________________________________
3. ___________________________________
4. ___________________________________
5. ___________________________________

**Key entities for this ingest:**
1. ___________________________________
2. ___________________________________
3. ___________________________________

---

## Phase 2 — During Ingest

### Source Page
- [ ] `wiki/sources/[SourceName].md` created
- [ ] Correct frontmatter type used (`article`, `paper`, `book`, or
      `research`)
- [ ] All required frontmatter fields filled: `title`, `type`, `tags`,
      `created`, `last_updated`
- [ ] `## Summary` section written (3–5 sentences minimum)
- [ ] `## Key Ideas` section written (bullet list)
- [ ] `## Concepts Extracted` section lists wikilinks to concept pages

### Concept Pages
- [ ] Each key concept has a page in `wiki/concepts/[ConceptName].md`
- [ ] New pages use the standard concept frontmatter schema
- [ ] Existing pages enriched — new content added, not overwritten
- [ ] Each concept page has at least one entry in `## Sources`

### Entity Pages
- [ ] Each key entity has a page in `wiki/entities/[EntityName].md`
- [ ] New pages use the standard entity frontmatter schema
- [ ] Existing pages enriched — `## Appearances In Wiki` updated

---

## Phase 3 — Post-Ingest (Karpathy Enrichment Protocol)

This phase cross-links the new source into the existing wiki. It is what
makes the vault grow as a connected graph rather than a pile of files.

- [ ] **Concept 1 searched:** `rg -li "[concept 1]" wiki/concepts/`
      — top result read, wikilink + one new sentence added → _____________
- [ ] **Concept 2 searched:** `rg -li "[concept 2]" wiki/concepts/`
      — top result read, wikilink + one new sentence added → _____________
- [ ] **Concept 3 searched:** `rg -li "[concept 3]" wiki/concepts/`
      — top result read, wikilink + one new sentence added → _____________
- [ ] **Concept 4 searched** (if applicable) → _____________
- [ ] **Concept 5 searched** (if applicable) → _____________
- [ ] **Enrichment log:** note which pages were enriched
      (report format: "Enriched: PageA, PageB; no match for ConceptC")

---

## Phase 4 — Administrative Updates

- [ ] `wiki/index.md` updated — new wikilinks added under the correct
      section (Concepts, Entities, or Sources)
- [ ] `wiki/log.md` entry appended in correct format:
      `## [YYYY-MM-DD] ingest | [description] — [X new, Y enriched]`

---

## Phase 5 — Quality Checks

- [ ] All frontmatter fields filled — no `YYYY-MM-DD` placeholders left
- [ ] All `[[wikilinks]]` in new pages resolve to real files
- [ ] No orphan pages created — every new page is linked from at least
      one other wiki page
- [ ] No source files modified — `raw/` folder contents are read-only
      after filing
- [ ] If multilingual content: triads are correctly formatted (native
      script → transliteration → translation → concept gloss)

---

## Ingest Summary (fill out and report to user)

| Field | Value |
|-------|-------|
| Source | |
| Source page created | |
| New concept pages | |
| Enriched concept pages | |
| New entity pages | |
| Enriched entity pages | |
| Pages enriched (Karpathy) | |
| Index updated | Yes / No |
| Log entry appended | Yes / No |
