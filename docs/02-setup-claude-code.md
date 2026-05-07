# Setup Guide — Claude Code

Claude Code is the recommended platform for this system. It has full file-write
access, supports sub-agents, and reads `CLAUDE.md` automatically — no
copy-paste required.

---

## Prerequisites

- Claude Code CLI installed (`npm install -g @anthropic-ai/claude-code` or
  follow the [official install instructions](https://docs.anthropic.com/claude-code))
- Vault copied from `template-vault/` to your target folder
- Anthropic API key or Claude subscription active

---

## Setup Steps

### 1. Open the vault in Claude Code

```bash
cd ~/my-second-brain   # or wherever your vault folder is
claude
```

Claude Code detects `CLAUDE.md` at the folder root and loads it as project
instructions automatically. You will see a confirmation in the startup output.

### 2. Confirm CLAUDE.md is loaded

In the Claude Code session, type:

```
What are your active instructions?
```

The orchestrator should describe its role, the vault structure, and the
available commands (Lookup, Ingest, Research, etc.). If it responds with
generic behavior, `CLAUDE.md` is not being read — check Step 3.

### 3. Copy example agents (optional)

The repo includes three example agents (Archivist, Codex, Nexus) in `template-vault/agents/examples/`. Claude Code only loads agents from `.claude/agents/` inside your vault. To activate them:

```bash
mkdir -p <your-vault>/.claude/agents
cp template-vault/agents/examples/*.md <your-vault>/.claude/agents/
```

You can also skip this and create your own agents using `template-vault/agents/_TEMPLATE.md`.

### 4. Set your orchestrator name

In `CLAUDE.md`, replace `{{ORCHESTRATOR_NAME}}` with a name of your choice:

```bash
sed -i '' 's/{{ORCHESTRATOR_NAME}}/Curator/g' ~/my-second-brain/CLAUDE.md
```

> Linux users: use `sed -i` without the `''`.

Restart the Claude Code session after editing `CLAUDE.md`.

### 5. Add domain agents

Agents live in `.claude/agents/` inside your vault. Each agent is a Markdown
file following the schema in `template-vault/agents/_TEMPLATE.md`.

```
my-second-brain/
  .claude/
    agents/
      generalist.md    ← copy from template-vault/agents/examples/
      history.md       ← your custom agent
      philosophy.md    ← your custom agent
  CLAUDE.md
  ...
```

The routing table in `CLAUDE.md` maps domains to agent file names. Update it
to match the agents you create:

```markdown
## Agent Routing
- History, archaeology → **herodotus** (.claude/agents/history.md)
- Western philosophy → **sophia** (.claude/agents/philosophy.md)
- General / cross-domain → **archivist** (.claude/agents/generalist.md)
```

See [08-creating-agents.md](08-creating-agents.md) for the full agent design guide.

### 6. Test with Lookup

```
Lookup zettelkasten
```

Expected: the orchestrator runs `rg -li "zettelkasten" wiki/`, checks
`wiki/index.md`, finds no results (empty vault is correct), and reports this.

### 7. Run your first Ingest

```
Ingest https://example.com/some-article
```

Claude Code has file-write access, so all wiki pages, index updates, and log
entries are written to disk automatically.

---

## Feature Parity

Claude Code has **full feature parity** with the system design:

| Feature | Status |
|---------|--------|
| File read / write | Full — all wiki pages written to disk |
| Sub-agents | Full — separate `.claude/agents/*.md` files |
| Web search | Full — agents can fetch URLs |
| CLAUDE.md auto-load | Full — no manual paste required |
| Lint command | Full — spawns codex agent |
| Research + file save | Full — output written to `raw/research/` |

---

## Gotchas

**CLAUDE.md must be at the vault root.**
Claude Code looks for `CLAUDE.md` in the directory you open, not in
subdirectories. If you open a parent folder instead of the vault folder,
`CLAUDE.md` will not be found.

**Sub-agents require separate files.**
Each domain agent must have its own file in `.claude/agents/`. Agents
defined inline in `CLAUDE.md` text will be interpreted as instructions to
the orchestrator, not as independent agent definitions.

**Restart after editing CLAUDE.md.**
Changes to `CLAUDE.md` are only picked up at session start. Exit and re-run
`claude` after any edits.

**iCloud sync and file locks.**
If your vault is in an iCloud-synced folder, Claude Code writes may
occasionally conflict with iCloud's sync process. Run `claude` from a local
folder if you experience file-write errors, or pause iCloud sync during
heavy ingest sessions.
