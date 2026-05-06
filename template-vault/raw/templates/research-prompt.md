<!--
AGENT INSTRUCTIONS — READ BEFORE USING THIS TEMPLATE
=====================================================

This template structures your research output for the `raw/research/` folder.
It is NOT the final wiki page — after the user reviews your output, they will
run `Ingest raw/research/[FileName]` to promote it into the wiki.

HOW TO USE:
1. Replace all {{ PLACEHOLDER }} values with real content.
2. Keep every section header — even if a section is sparse, include it
   with a note explaining why (e.g., "No primary sources identified yet.").
3. The Key Concepts section is the most important: each concept you name
   here will likely become its own wiki/concepts/ page on ingest.
4. Open Questions are genuinely valuable — do not omit them to appear
   more authoritative. Honest gaps help the user decide what to research next.
5. Save your completed output to:
   raw/research/YYYY-MM-DD-[topic-slug].md
   Example: raw/research/2024-03-15-stoic-ethics.md
6. Do NOT auto-ingest. The user reviews first.

DEPTH GUIDANCE:
- [DEPTH: quick]    → 400–600 words total, compress Key Concepts section
- [DEPTH: standard] → 4,000–8,000 words (default; this template targets this)
- [DEPTH: deep]     → no ceiling; expand every subsection exhaustively
-->

---
title: "{{ RESEARCH TITLE }}"
type: research
domain: "{{ PRIMARY DOMAIN — e.g., philosophy, linguistics, history }}"
topic_slug: "{{ topic-slug }}"
agent: "{{ AGENT NAME }}"
depth: standard
tags:
  - research
  - "{{ domain-tag }}"
source_file: "raw/research/YYYY-MM-DD-{{ topic-slug }}.md"
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
---

# {{ RESEARCH TITLE }}

*Research output by **{{ AGENT NAME }}** — generated YYYY-MM-DD*
*Depth: standard | Domain: {{ PRIMARY DOMAIN }}*

---

## Executive Summary

<!-- 150–250 words. What is the core answer to the research question?
     What are the 2–3 most important things the user should take away?
     Write this last, after completing all other sections. -->

{{ EXECUTIVE SUMMARY }}

---

## Background

<!-- Establish context. Cover:
     - Why this topic exists / how it arose historically or intellectually
     - What field(s) it belongs to
     - Any important terminological distinctions the user should know upfront
     - Scope of this research (what is included / excluded) -->

{{ BACKGROUND }}

---

## Key Concepts

<!-- This is the core section. For each major concept:
     - Give it a clear, standalone definition
     - Explain its significance within the domain
     - Name related concepts (these become wikilinks on ingest)
     Aim for 3–8 concepts depending on topic complexity. -->

### {{ CONCEPT 1 NAME }}

**Definition:** {{ One-sentence definition. }}

**Significance:** {{ Why does this concept matter? What does it explain or enable? }}

**Related concepts:** [[{{ Related Concept A }}]], [[{{ Related Concept B }}]]

---

### {{ CONCEPT 2 NAME }}

**Definition:** {{ One-sentence definition. }}

**Significance:** {{ Why does this concept matter? }}

**Related concepts:** [[{{ Related Concept }}]]

---

### {{ CONCEPT 3 NAME }}

**Definition:** {{ One-sentence definition. }}

**Significance:** {{ Why does this concept matter? }}

**Related concepts:** [[{{ Related Concept }}]]

---

<!-- Add additional ### subsections as needed. -->

---

## Key Figures / Entities

<!-- List important people, organizations, schools of thought, or tools
     associated with this topic. These become wiki/entities/ pages on ingest.
     Format: Name — brief role or contribution. -->

| Name | Type | Key Contribution |
|------|------|-----------------|
| {{ Person/Org Name }} | person / org / school | {{ One-line description }} |
| {{ Person/Org Name }} | person / org / school | {{ One-line description }} |

---

## Primary Sources & References

<!-- List the most important original texts, papers, or canonical sources.
     Do NOT fabricate citations. If you are uncertain, say so explicitly.
     Format entries as: Author, *Title* (Year). Notes if relevant. -->

1. {{ Author }}, *{{ Title }}* ({{ Year }}). {{ Optional note. }}
2. {{ Author }}, *{{ Title }}* ({{ Year }}). {{ Optional note. }}

*Note: References above are from training knowledge. The user should verify
publication details before citing in formal work.*

---

## Open Questions

<!-- Honest gaps, unresolved debates, areas needing further research.
     These are valuable — they guide the user's next Research commands. -->

- {{ Open question or unresolved debate 1 }}
- {{ Open question or unresolved debate 2 }}
- {{ Open question or unresolved debate 3 }}

---

## Cross-Domain Connections

<!-- Where does this topic intersect with other domains in the wiki?
     Name specific concepts or fields — these become cross-links on ingest.
     This section enables the Karpathy enrichment protocol. -->

- **{{ Domain A }}:** {{ How this topic connects to Domain A. }} → see [[{{ Concept in Domain A }}]]
- **{{ Domain B }}:** {{ How this topic connects to Domain B. }} → see [[{{ Concept in Domain B }}]]

---

*End of research output. Review with the user before ingesting.*
