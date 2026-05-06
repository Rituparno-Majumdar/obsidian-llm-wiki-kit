# Quickstart — 10 Minutes to a Working Vault

> **Prerequisites:** Obsidian installed. An LLM of your choice set up (Claude,
> ChatGPT, Gemini, or a local model). Git optional but recommended.

---

## Step 1 — Copy the template vault

```bash
git clone https://github.com/your-username/obsidian-llm-wiki-kit.git
cp -r obsidian-llm-wiki-kit/template-vault ~/my-second-brain
```

Or download the ZIP from GitHub and copy the `template-vault/` folder manually.

The folder you end up with (`~/my-second-brain` above, or whatever you name it)
is your vault. It is just a folder of Markdown files — Obsidian adds no database
files to it.

---

## Step 2 — Open the folder as an Obsidian vault

1. Open Obsidian.
2. Click **Open another vault** → **Open folder as vault**.
3. Select the folder you copied in Step 1.
4. Obsidian will open with the template structure intact.

You will see folders (`raw/`, `wiki/`) and a few files in the root. That is
the entire vault scaffold.

---

## Step 3 — Choose your LLM path

### Option A: Claude Code (recommended — full features)

Claude Code reads `CLAUDE.md` automatically when you open the vault folder.
No copy-paste required.

```bash
cd ~/my-second-brain
claude
```

See [02-setup-claude-code.md](02-setup-claude-code.md) for full instructions.

### Option B: Any other LLM

Open `template-vault/SYSTEM_PROMPT.md` and paste its contents as the system
prompt for your LLM of choice.

- Claude Desktop / Claude.ai Projects → [03-setup-claude-desktop.md](03-setup-claude-desktop.md)
- ChatGPT → [04-setup-chatgpt.md](04-setup-chatgpt.md)
- Gemini → [05-setup-gemini.md](05-setup-gemini.md)
- Local models (Ollama / LM Studio) → [06-setup-local-ollama.md](06-setup-local-ollama.md)

---

## Step 4 — Set your orchestrator name

Open `CLAUDE.md` (or `SYSTEM_PROMPT.md`) and replace every instance of
`{{ORCHESTRATOR_NAME}}` with a name of your choice. This is the persona your
LLM will use when acting as the PKM orchestrator.

Common choices: Archivist, Nemo, Sage, Keeper, Atlas.

```bash
# Example: replace in CLAUDE.md
sed -i '' 's/{{ORCHESTRATOR_NAME}}/Archivist/g' ~/my-second-brain/CLAUDE.md
```

---

## Step 5 — Set up agent routing

Your orchestrator routes Research commands to domain specialists (agents).
You have two options:

**Option A — Manual:** Open `CLAUDE.md` and fill in the agent routing table.
Each row maps a domain to an agent name and file path. See
[08-creating-agents.md](08-creating-agents.md) for guidance.

**Option B — Wizard (recommended for new users):** Open
`meta-prompt-wizard/WIZARD.md` and follow the interactive prompts. The wizard
generates a complete, personalized `CLAUDE.md` with routing table, agent
definitions, and formatting rules based on your answers.

---

## Step 6 — Test with a Lookup

In your LLM session, type:

```
Lookup zettelkasten
```

Expected response: the orchestrator searches `wiki/` with `rg`, checks
`wiki/index.md`, finds no results (the vault is empty), and reports this
clearly. An empty-vault result is correct — it means the system is working.

If the orchestrator does not search the vault and instead answers from
general knowledge, your system prompt is not loaded correctly. Return to
Step 3.

---

## Step 7 — Your first Ingest

Drop an article URL or paste article text and run:

```
Ingest [url or paste article text here]
```

The orchestrator will:
1. Read the source and discuss key takeaways with you briefly.
2. Create `wiki/sources/[ArticleName].md`.
3. Create or enrich concept pages in `wiki/concepts/`.
4. Create or enrich entity pages in `wiki/entities/`.
5. Run the Karpathy enrichment pass (cross-linking into existing pages).
6. Update `wiki/index.md` and append to `wiki/log.md`.

After the first ingest, open Obsidian's Graph View to see your first nodes.

---

## What's next?

- Run `Research [topic]` to have a domain agent write a research document.
- Run `Lint` to check vault health (orphan pages, broken links).
- Run `Synthesize [topic]` to find cross-domain connections.
- Read [07-philosophy.md](07-philosophy.md) to understand why the system
  works the way it does.
