# Setup Guide — ChatGPT

ChatGPT can run this system via Custom GPTs or ChatGPT Projects. Both
options work; each has different tradeoffs.

---

## Prerequisites

- ChatGPT Plus or Team subscription (required for Custom GPTs and Projects)
- Vault copied from `template-vault/` to your Obsidian folder
- Obsidian open with the vault loaded

---

## Option A: Custom GPT (recommended)

Custom GPTs allow you to pre-load the system prompt and optionally upload
vault files as Knowledge. The GPT persists and can be reused without
re-pasting instructions.

### Steps

1. Go to [chatgpt.com](https://chatgpt.com) and click **Explore GPTs** →
   **Create a GPT**.
2. Switch to the **Configure** tab.
3. In the **Instructions** field, paste the full contents of
   `template-vault/SYSTEM_PROMPT.md`.
4. Replace `{{ORCHESTRATOR_NAME}}` with your chosen orchestrator name.
5. Under **Knowledge**, upload key vault files:
   - `wiki/index.md`
   - `wiki/overview.md`
   - Any concept or source pages you want the GPT to reference
6. Save and name your GPT (e.g., "My Second Brain").

The GPT will retrieve uploaded Knowledge files using its internal search
when responding to Lookup, Query, and Ingest commands.

### Updating Knowledge

Re-upload vault files periodically as the vault grows. There is no automatic
sync — this is a manual step each time you want the GPT to reflect vault
changes.

---

## Option B: ChatGPT Projects

Projects keep a persistent system message and file context across
conversations.

### Steps

1. In ChatGPT, click **Projects** → **New Project**.
2. Click the settings icon and paste the contents of `SYSTEM_PROMPT.md`
   into the **Instructions** field.
3. Replace `{{ORCHESTRATOR_NAME}}`.
4. In the project file area, upload vault snapshot files as needed.
5. Start a new conversation inside the Project.

---

## Limitations

**No native file-write access.**
ChatGPT cannot write directly to your vault. Copy LLM output manually
into Obsidian after every Ingest, Research, or Compare operation.
See the copy workflow in [03-setup-claude-desktop.md](03-setup-claude-desktop.md)
— the same steps apply here.

**No sub-agents.**
ChatGPT has no mechanism for spawning separate agent instances. Domain
agents are simulated as modes: the orchestrator shifts persona for Research
tasks and then returns to orchestrator mode. This works for most use cases
but is less isolated than Claude Code's sub-agent model.

**No Code Interpreter required — but it helps.**
The system works without Code Interpreter enabled. However, if you enable
it, the GPT can process structured data from uploaded files more reliably
and can generate analysis tables.

---

## Model Recommendation

**GPT-4o** is strongly recommended. It handles complex routing logic,
long system prompts, and structured output (YAML frontmatter, wikilink
syntax) reliably.

**GPT-3.5 / GPT-4o mini** may struggle with:
- Multi-step routing decisions (which agent handles which domain)
- Maintaining triad formatting for multilingual content
- Generating consistent YAML frontmatter

If you are on a free plan and limited to GPT-3.5, consider using
`SYSTEM_PROMPT_SHORT.md` (a stripped-down version from the wizard) to
reduce instruction complexity.

---

## Tips

**Test routing explicitly.**
After setup, test with a domain-specific Research request:

```
Research the philosophy of Immanuel Kant
```

The orchestrator should route this to your philosophy agent (or simulate
the mode). If it answers directly as the orchestrator without invoking an
agent mode, your routing table may need tightening.

**Use the Analyze Data capability for vault exports.**
You can export your vault as a ZIP of Markdown files and upload it to a
Custom GPT with Code Interpreter. The GPT can then search across files using
Python, which is more powerful than the default Knowledge retrieval.

**Re-paste the system prompt for very long sessions.**
ChatGPT can lose effective context of early instructions in very long
conversations. If the orchestrator stops following formatting rules
(e.g., stops generating frontmatter), paste the key sections of
`SYSTEM_PROMPT.md` again in a new message.
