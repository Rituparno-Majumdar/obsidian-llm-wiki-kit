# Multilingual Vault Guide

This guide covers how to handle non-English content in your vault — primary
texts, philosophical terms, historical sources — so that both the original
language and its meaning are preserved accurately.

---

## When to Use Triad Formatting

The triad format (native script → transliteration → translation) is for
**conceptually load-bearing passages** — terms or sentences where the
original language carries meaning that an English translation alone cannot
convey.

**Use triads when:**
- Introducing a key term for the first time (e.g., Sanskrit *dharma*,
  Arabic *fitra*, Greek *logos*)
- Quoting a passage that will anchor a concept page
- The term has no direct English equivalent and the transliteration aids
  pronunciation or searchability
- The passage comes from a primary source in a classical language

**Do not use triads for:**
- Contemporary texts where the original language is incidental
- Terms already established earlier in the same document
- Casual multilingual usage (names of people, places, titles)
- Languages that use the Roman alphabet (French, German, Latin —
  see separate rules below)

---

## The Triad Block Format

Every triad block follows this exact structure:

```
> **[Language]:** [native script passage]
> **Transliteration:** [romanized form with full diacritical marks]
> **Translation:** [English rendering]
> **Concept gloss:** [1–2 sentences on the term's significance]
```

All four lines are required. Do not omit the concept gloss — it is what
prevents the translation from being read out of context.

### Example — Sanskrit

> **Sanskrit:** अहिंसा परमो धर्मः
> **Transliteration:** ahiṃsā paramo dharmaḥ
> **Translation:** "Non-violence is the supreme dharma."
> **Concept gloss:** A formulation found across multiple Hindu texts and
> central to Jain ethics. *Ahiṃsā* designates the principle of not causing
> harm to any living being — adopted by Gandhi as a political method but
> rooted in a much older metaphysical tradition.

### Example — Arabic

> **Arabic:** الإجماع
> **Transliteration:** al-ijmāʿ
> **Translation:** "Consensus"
> **Concept gloss:** One of the four sources of Islamic law (*uṣūl al-fiqh*).
> Refers to the consensus of qualified scholars on a legal or theological
> question. Its scope and authority are debated between Sunni schools.

### Example — Classical Greek

> **Greek:** ἀρετή
> **Transliteration:** aretḗ
> **Translation:** "Virtue" or "excellence"
> **Concept gloss:** Central to Aristotelian ethics. *Aretē* does not map
> cleanly to "virtue" — it designates the excellence of a thing in fulfilling
> its function (*telos*). A knife's *aretē* is sharpness; a human's *aretē*
> is rational activity in accordance with reason.

---

## German — Two-Line Format

German uses the Roman alphabet and needs no transliteration. Use a two-line
block with an optional concept gloss:

```
> **Deutsch:** [original German passage]
> **Translation:** [English rendering]
> **Concept gloss:** [optional — include when the term is philosophically
> significant and the translation is contested]
```

### Example

> **Deutsch:** "Dasein ist das Seiende, dem es in seinem Sein um dieses
> Sein selbst geht."
> **Translation:** "Dasein is the being for whom, in its being, that being
> itself is an issue."
> **Concept gloss:** Heidegger's definition of human existence in *Being and
> Time* (1927). *Dasein* (literally "being-there") resists translation because
> it names a mode of being, not a noun. "Human being" flattens the ontological
> point; Heidegger preferred to leave it untranslated.

---

## East Asian Languages — Pinyin and Romaji

For Chinese and Japanese, the transliteration line carries the standard
romanization system.

### Chinese → Pinyin

> **Chinese:** 知行合一
> **Transliteration (Pinyin):** zhī xíng hé yī
> **Translation:** "The unity of knowledge and action."
> **Concept gloss:** Central doctrine of Wang Yangming's Neo-Confucian
> philosophy. Genuine knowledge of a moral principle necessarily manifests
> as action — knowing what is good and failing to do it indicates the knowing
> was incomplete.

### Japanese → Romaji (Hepburn system)

> **Japanese:** 侘び寂び
> **Transliteration (Romaji):** wabi-sabi
> **Translation:** "The beauty of imperfection and transience."
> **Concept gloss:** A Japanese aesthetic sensibility that finds beauty in
> impermanence, incompleteness, and irregularity. Rooted in Buddhist
> philosophy (*anicca*) and expressed most clearly in the tea ceremony and
> pottery traditions.

---

## Diacritical Marks

Preserve diacritical marks in all transliterations. They are not decorative —
they distinguish different sounds (and sometimes different words entirely).

Recommended standards:

| Language | Standard |
|----------|---------|
| Sanskrit / Pali | IAST (International Alphabet of Sanskrit Transliteration) |
| Arabic | ALA-LC or ISO 233 |
| Hebrew | SBL Academic Handbook |
| Ancient Greek | Standard polytonic romanization |
| Chinese | HSK Pinyin with tone marks |
| Japanese | Hepburn romanization |

If your LLM strips diacriticals from output, add a note to your system prompt:
> "Preserve all diacritical marks in transliterations. Do not simplify ā to a,
> ś to s, ḍ to d, etc."

If your text editor strips them, use a Unicode-aware editor (Obsidian handles
Unicode correctly).

---

## Setting Up Multilingual Support

### Via the Wizard

When you run the wizard (`meta-prompt-wizard/WIZARD.md`), it asks in
Section 1, Question 2:

> "Do you work with non-English source material? If so, which languages?"

Answer with the languages you use. The wizard will insert the appropriate
triad rules into your generated `CLAUDE.md` / `SYSTEM_PROMPT.md` and
reference this guide.

### Manual setup

Add the following to your `CLAUDE.md` or `SYSTEM_PROMPT.md` under the
Ingest or Research section:

```markdown
## Multilingual Rules
For any non-English passage in research output or ingested sources, apply
the triad format defined in `raw/templates/multilingual-research.md`.
German passages use the two-line format (no transliteration).
East Asian passages use pinyin (Chinese) or Hepburn romaji (Japanese)
as the transliteration. Never collapse a triad to English-only.
```

Then reference `raw/templates/multilingual-research.md` in your vault —
agents will check it for detailed formatting rules.

---

## Latin

Latin uses the Roman alphabet. Triads are not required. Inline glosses are
sufficient:

> *Cogito, ergo sum* ("I think, therefore I am") — Descartes,
> *Discours de la méthode*, 1637.

For contested or philosophically significant Latin terms, a brief gloss
is welcome but the full four-line triad is unnecessary.
