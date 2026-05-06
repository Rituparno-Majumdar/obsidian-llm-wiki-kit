<!--
MULTILINGUAL RESEARCH — FORMATTING GUIDE
========================================

OPTIONAL MODULE: Only include this template in your vault if you regularly
work with non-English sources (classical texts, historical documents,
philosophical traditions in their original languages).

This guide defines the formatting rules your orchestrator and agents must
follow whenever research output includes non-English passages.
-->

---
title: Multilingual Research Formatting Guide
type: template
tags:
  - template
  - multilingual
  - formatting
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
---

# Multilingual Research Formatting Guide

---

## 1. The Triad Format

Any non-English passage that carries conceptual weight must appear as a **triad
block** — three lines in strict order:

```
> **[Language]:** [native script passage]
> **Transliteration:** [romanized form with diacritical marks]
> **Translation:** [English rendering]
> **Concept gloss:** [brief explanation of the term's significance — 1–2 sentences]
```

### Why a triad?

The native script anchors the concept to its tradition. The transliteration
allows pronunciation and searchability for readers without the script. The
translation makes it accessible. The concept gloss prevents the translation
from being read out of context. Collapsing to English-only loses all three.

---

## 2. Example Triad Blocks

### Sanskrit

> **Sanskrit:** धर्मक्षेत्रे कुरुक्षेत्रे समवेता युयुत्सवः
> **Transliteration:** dharma-kṣetre kuru-kṣetre samavetā yuyutsavaḥ
> **Translation:** "On the field of dharma, the field of Kuru, assembled and
> eager to fight..."
> **Concept gloss:** The opening verse of the Bhagavad Gita. *Dharma-kṣetra*
> (field of dharma) is read by commentators as both a literal battlefield and
> a metaphor for the arena of moral action.

### Arabic

> **Arabic:** الفلسفة خادمة اللاهوت
> **Transliteration:** al-falsafa khādimatu al-lāhūt
> **Translation:** "Philosophy is the handmaid of theology."
> **Concept gloss:** A formulation of the relationship between reason and
> revelation in medieval Islamic and Christian scholasticism. Contested by
> Averroes, who reversed the hierarchy.

### Greek

> **Greek:** γνῶθι σεαυτόν
> **Transliteration:** gnōthi seautón
> **Translation:** "Know thyself."
> **Concept gloss:** Inscribed at Delphi; adopted by Socrates as the founding
> imperative of philosophical self-examination.

---

## 3. When to Use Triads vs. Inline Translation

**Use a full triad block when:**
- The passage is a key term, sloka, aphorism, or definition being introduced
  for the first time
- The original word carries untranslatable nuance (e.g., Sanskrit *dharma*,
  Greek *logos*, Arabic *fitra*)
- The passage will appear as a wikilink target or concept page anchor

**Use inline translation (no triad) when:**
- The passage is incidental or purely illustrative
- The term is already established earlier in the document
- The context is a contemporary or casual text where the original language
  is stylistic rather than conceptual

**Example of acceptable inline usage:**
> Ibn Rushd (also known as Averroes) argues in the *Fasl al-Maqal*
> (literally "The Decisive Treatise") that philosophy and Islamic law
> are not in fundamental conflict.

---

## 4. Diacritical Marks

Preserve diacritical marks in all transliterations. Common systems:

| Language | Standard | Example |
|----------|----------|---------|
| Sanskrit / Pali | IAST (International Alphabet of Sanskrit Transliteration) | ś, ṭ, ḍ, ṃ, ā, ī, ū |
| Arabic | ALA-LC or DIN 31635 | ā, ī, ū, ḥ, ḫ, ḏ, ġ |
| Hebrew | SBL Academic | š, ṭ, ṣ, ḥ |
| Greek | Standard polytonic | ā, ō, ph, th, kh |

If your LLM or editor strips diacriticals, note this explicitly:
`[Diacriticals omitted — IAST transcription intended]`

---

## 5. German — Two-Line Format (No Transliteration)

German does not require transliteration. Use a two-line block:

```
> **Deutsch:** [original German passage]
> **Translation:** [English rendering]
> **Concept gloss:** [brief explanation]
```

### Example

> **Deutsch:** "Die Sprache ist das Haus des Seins."
> **Translation:** "Language is the house of Being."
> **Concept gloss:** Heidegger's formulation from the *Letter on Humanism*
> (1947). Language is not merely a tool for describing Being but the medium
> in which Being discloses itself.

---

## 6. East Asian Languages — Pinyin / Romaji as Transliteration

For Chinese and Japanese, the transliteration line carries pinyin (Chinese)
or romaji (Japanese):

### Chinese

> **Chinese:** 无为而无不为
> **Transliteration (Pinyin):** wú wéi ér wú bù wéi
> **Translation:** "Act without acting, and nothing is left undone."
> **Concept gloss:** Core principle of Daoist philosophy (*wuwei*). The
> paradox dissolves when *wei* is understood as forced or contrived action,
> not action in general.

### Japanese

> **Japanese:** 物の哀れ
> **Transliteration (Romaji):** mono no aware
> **Translation:** "The pathos of things" or "the gentle sadness of
> impermanence."
> **Concept gloss:** An aesthetic concept central to classical Japanese
> literature, particularly the *Tale of Genji*. Designates a bittersweet
> sensitivity to transience.

---

## 7. Latin — Transliteration Optional

Latin uses the Roman alphabet. Transliteration is not required unless the
text uses Medieval or reconstructed Classical pronunciation notation. Inline
glosses are sufficient for Latin passages:

> *Cogito, ergo sum* — "I think, therefore I am" (Descartes, *Discourse on
> the Method*, 1637). The axiomatic foundation of Cartesian rationalism.

---

## 8. Setup Note

To activate multilingual formatting in your vault:

1. Reference this file in your CLAUDE.md or SYSTEM_PROMPT.md under the
   Ingest section.
2. Instruct your orchestrator: *"For any non-English passage in research
   output, apply the triad format defined in
   `raw/templates/multilingual-research.md`."*
3. The wizard (`meta-prompt-wizard/WIZARD.md`) will ask about multilingual
   needs in Section 1, Question 2 and insert the appropriate instruction
   automatically.

If you do NOT work with non-English sources, you can safely delete this file
and the associated instructions.
