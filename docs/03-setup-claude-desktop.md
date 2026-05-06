# Setup Guide — Claude Desktop / Claude.ai Projects

Claude Desktop and Claude.ai Projects give you a conversational interface
with persistent context via the Projects feature. This is a good option if
you prefer a chat UI over a terminal.

---

## Prerequisites

- A Claude.ai Pro subscription (Projects feature required)
- Vault copied from `template-vault/` to your Obsidian folder
- Obsidian open with the vault loaded

---

## Setup Steps

### 1. Use SYSTEM_PROMPT.md, not CLAUDE.md

The `CLAUDE.md` file is specific to Claude Code's auto-load mechanism.
For Claude Desktop and Claude.ai, use `SYSTEM_PROMPT.md` instead — it
contains the same instructions formatted for manual paste.

### 2. Create a Project

1. Go to [claude.ai](https://claude.ai) and click **Projects** in the
   left sidebar.
2. Click **New Project**.
3. Name it (e.g., "My Second Brain").
4. Open **Project Instructions**.
5. Paste the entire contents of `template-vault/SYSTEM_PROMPT.md`.
6. Replace `{{ORCHESTRATOR_NAME}}` with your chosen name.
7. Save the instructions.

The instructions persist across all conversations within this Project.

### 3. Set your orchestrator name

Before pasting, open `SYSTEM_PROMPT.md` in a text editor and replace
`{{ORCHESTRATOR_NAME}}` globally. Alternatively, find-and-replace inside
the Project Instructions text box after pasting.

### 4. Upload vault snapshots (optional)

Claude.ai Projects supports file uploads. You can upload Markdown files
from your vault for the LLM to reference during a session. This partially
compensates for the lack of direct file access.

To share vault state:
1. In your Project, click **Add content** → **Upload files**.
2. Upload `wiki/index.md`, `wiki/overview.md`, and any concept pages you
   want the LLM to draw on.
3. Re-upload periodically as the vault grows.

This is a workaround, not a native integration. The LLM reads the uploaded
files but cannot write back to them.

### 5. Test with Lookup

In your Project conversation, type:

```
Lookup zettelkasten
```

Because the LLM has no direct file access, it will search the uploaded files
(if any) and its context window. It will correctly report no results for an
empty vault.

---

## Limitations

**No file-write access.**
Claude Desktop cannot write files to your vault. After every Ingest,
Research, or Compare operation, you must manually copy the LLM's output
into Obsidian and save it as a Markdown file in the correct folder.

Workflow:
1. Ask the LLM to generate the wiki page.
2. The LLM outputs a formatted Markdown block in the chat.
3. Copy the output.
4. In Obsidian, create a new file in the correct folder and paste.
5. Manually update `wiki/index.md` and `wiki/log.md`.

**No sub-agents.**
Claude Desktop does not support spawning separate agent instances. Domain
agents are simulated as modes within a single conversation: the orchestrator
"becomes" the relevant agent for the duration of the Research task.

This works adequately for most Research commands but lacks the isolation
of true sub-agents. The orchestrator's persona may drift in very long
sessions.

**Context window limits in long sessions.**
If a conversation grows very long, early instructions may fade from
effective context. Paste the system prompt again, or start a new
conversation in the same Project (Project Instructions persist).

---

## Tips

**Use Artifacts for formatted output.**
Claude Desktop renders Markdown in Artifacts (the side panel). Ask the LLM
to write wiki pages as Artifacts for easier reading and copying:

> "Write the concept page as an Artifact so I can copy it directly."

**Upload index.md at the start of each session.**
Uploading `wiki/index.md` gives the LLM a current map of the vault and
enables more accurate Lookup and cross-linking.

**Batch operations in one session.**
Because file-write is manual, batch multiple Ingest operations before
copying output to Obsidian. Ask the LLM to generate all pages in sequence,
then copy them all at once.
