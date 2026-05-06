# Setup Guide — Gemini

Gemini can run this system via Gems (custom AI personas). Gemini 1.5 Pro
and Gemini 2.0 Flash are recommended for this use case.

---

## Prerequisites

- Google account with Gemini Advanced subscription (required for Gems)
- Vault copied from `template-vault/` to your Obsidian folder
- Obsidian open with the vault loaded

---

## Setup Steps

### 1. Create a Gem

1. Go to [gemini.google.com](https://gemini.google.com).
2. Click **Gems** in the left sidebar → **New Gem** (or **Create a Gem**).
3. Give the Gem a name (e.g., "Second Brain Orchestrator").
4. In the **Instructions** field, paste the full contents of
   `template-vault/SYSTEM_PROMPT.md`.
5. Replace `{{ORCHESTRATOR_NAME}}` with your chosen name.
6. Click **Save**.

### 2. Upload vault files (optional)

Some Gem configurations allow file uploads. Upload `wiki/index.md` and
`wiki/overview.md` to give the Gem context about existing vault content.
This improves Lookup and cross-linking quality.

### 3. Test with Lookup

Open a conversation with your Gem and type:

```
Lookup zettelkasten
```

Expected: the Gem searches uploaded files (if any), finds no match in an
empty vault, and reports this correctly.

---

## Limitations

**No file-write access.**
Gemini cannot write files to your vault. After every Ingest, Research, or
Compare operation, copy the Gem's output manually into Obsidian.

**No sub-agents.**
Gems do not support spawning separate agent instances. Domain agents are
simulated as modes within a single Gem conversation.

**File upload limits.**
Gems have limits on the number and size of files that can be uploaded.
For large vaults, prioritize uploading `wiki/index.md` and key concept
pages over uploading every source file.

---

## Multilingual Advantage

Gemini has strong multilingual capability, including support for
Devanagari, Arabic, Chinese, Japanese, and other scripts. If you work with
non-English sources, Gemini handles triad formatting (native script +
transliteration + translation) reliably — often better than English-centric
models.

Recommended for:
- Sanskrit / Pali texts
- Arabic philosophical texts
- Classical Chinese or Japanese sources
- Any vault with substantial non-English content

See [09-multilingual-guide.md](09-multilingual-guide.md) for setup
instructions.

---

## Model Recommendations

| Model | Use Case |
|-------|----------|
| Gemini 2.0 Flash | Fast turnaround, handles long system prompts well, good for daily Ingest/Lookup |
| Gemini 1.5 Pro | Best reasoning, recommended for Research and Synthesize |
| Gemini 1.5 Flash | Lighter tasks; may miss edge cases in routing logic |

**Gemini 2.0 Flash** is particularly well-suited for this system because it
handles long system prompts without degradation, making it reliable for
sessions where the full `SYSTEM_PROMPT.md` is loaded.

---

## Tips

**Test long prompt persistence.**
After loading the Gem, send a few messages and then re-run `Lookup test`.
If the Gem has stopped following the wiki schema (e.g., generating output
without frontmatter), the system prompt may have degraded. Re-open the Gem
with a fresh conversation.

**Use Gemini's code execution for vault analysis.**
If your Gem has access to Google's code execution tool, you can upload a
ZIP of vault Markdown files and ask Gemini to search and analyze them
programmatically — similar to ChatGPT with Code Interpreter.

**Pair with Google Drive.**
If your vault is stored in Google Drive, Gemini can reference Drive files
directly via the Google Workspace integration. This partially compensates
for the lack of native file-write access.
