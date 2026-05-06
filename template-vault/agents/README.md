# Agents — How They Work

This guide explains the agent system in the LLM Wiki Kit: what agents are, how to create them, how they are named, how the orchestrator routes to them, and how to adapt them for platforms other than Claude Code.

---

## 1. What Agents Are

Agents are domain-specialist subagents spawned by the orchestrator (defined in `CLAUDE.md` or `SYSTEM_PROMPT.md`) to handle research in specific areas of your knowledge base.

Each agent:

- **Owns exactly one domain** — history, science, philosophy, a specific craft, etc.
- **Has a dedicated identity** — a name, a description the orchestrator reads when deciding whether to invoke it, a defined set of tools, and a fixed output format.
- **Saves research to `raw/research/`** — never to the wiki directly. The wiki grows only through the `Ingest` command, which you run manually after reviewing the output.
- **Never auto-ingests** — the agent writes a file and returns its path. You decide when to ingest.

The orchestrator is not an agent — it is the system prompt itself (defined in `CLAUDE.md`). Agents are subordinate to it. The orchestrator spawns the right agent based on topic, collects the output path, and waits for your instruction.

---

## 2. Anatomy of an Agent File

Each agent is defined in a single Markdown file with YAML frontmatter followed by structured sections.

### Frontmatter

```yaml
---
name: agent-slug
description: >
  One-line trigger description. The orchestrator reads this line to decide
  when to spawn this agent.
tools: [Read, Write, WebSearch, WebFetch]
---
```

| Field | Purpose |
|---|---|
| `name` | The slug used by the orchestrator in the routing table. Must be lowercase, hyphen-separated. |
| `description` | A single declarative sentence describing what topics trigger this agent. The orchestrator scans descriptions to route requests. Be specific — vague descriptions cause mis-routing. |
| `tools` | A list of tools the agent has access to. Adjust based on your LLM platform. Common values: `Read`, `Write`, `Bash`, `WebSearch`, `WebFetch`. Lint-style agents typically only need `Read` and `Bash`. |

### Body Sections

After the frontmatter, every agent file must contain:

| Section | Purpose |
|---|---|
| **Role** | A paragraph describing what domain this agent owns, what expertise it demonstrates, and what kinds of sources it prefers. |
| **When to Invoke** | Bullet list of trigger phrases — the specific commands or request patterns that should route to this agent. |
| **Operating Procedure** | Numbered steps the agent follows on every invocation. The first step must always be Lookup. |
| **Output Format** | Required frontmatter fields, required sections, citation style, and any special passage formatting (e.g., block quotes, foreign-language triads). |
| **Domain Conventions** | Any domain-specific formatting rules, preferred terminology, standard sources, or special handling. Delete this section if the domain has no special conventions. |
| **Failure Modes** | How the agent handles out-of-scope requests, unavailable sources, or ambiguous instructions. |

---

## 3. The Mandatory Lookup-First Rule

**Every agent must run Lookup against the wiki before doing any external research.**

The procedure is:

```
rg -li "<key term>" wiki/
```

Run this for 3–5 key terms from the research request. Scan `wiki/index.md` for matching wikilinks and tags. Read the top 2–3 candidate files in full.

If the wiki already has substantial coverage of the topic, the agent must:
1. Summarize what is already there.
2. Ask whether external research is still needed.
3. If yes, proceed. If no, stop.

This prevents the most common failure mode in wiki-based PKM systems: duplicate concept pages that diverge over time. An agent that skips Lookup is a poorly configured agent.

---

## 4. Naming Conventions

Agent names should be **memorable, domain-relevant, and drawn from mythology, literary history, or thematic vocabulary**.

Good naming heuristics:

- A history agent might be named after Herodotus (the first historian).
- A science agent might be named after Kepler (a foundational astronomer).
- A literature agent might be named after Borges (a librarian-author known for encyclopedic writing).
- A linguistics agent might be named after Panini (the Sanskrit grammarian).
- A philosophy agent might be named after Sophia (Greek for wisdom).

The name does not need to be from the same cultural tradition as the domain — it just needs to be evocative and easy to remember. A cooking agent named Escoffier works. A music theory agent named Pythagoras works. A cryptography agent named Enigma works.

**Reserved names** — do not reuse these, as they are already defined in the template:

> `Generalist` · `Librarian` · `Synthesizer`

The actual example agents in this kit use the names **Archivist**, **Codex**, and **Nexus** — these are also reserved within a deployed kit, though you can rename them to suit your preferences.

---

## 5. Platform Notes

Agent files as described here work natively in **Claude Code**, where the `.claude/agents/` directory is natively supported and the system can spawn subagents from file definitions.

On other platforms, agents are simulated as **modes** — named personas or instruction blocks added to your system prompt.

### ChatGPT (Custom GPT or System Prompt)

Add each agent as a labeled block in your system prompt:

```
## AGENT: historian
Triggered by: Research [history topic]
Role: You are a history specialist. Before any external search, scan the wiki...
Output: Save to raw/research/YYYY-MM-DD-[slug].md
```

Trigger phrases must be unambiguous — the model switches behavior based on keyword matching in your message.

### Gemini / Other API Models

Same approach as ChatGPT. Use a `SYSTEM_PROMPT.md` file and add agent sections with explicit trigger phrases and output instructions.

### Ollama (Local Models)

For local models, keep the agent section short. Local models with smaller context windows may lose agent instructions mid-session. Keep each agent block under 300 words and repeat the trigger phrase format explicitly.

---

## 6. How to Add a New Agent

Follow these steps exactly:

1. **Copy `_TEMPLATE.md`** from this directory.

2. **Rename the file** using the agent's slug (e.g., `historian.md`, `chef.md`, `cryptographer.md`). Place it in `template-vault/agents/` (or `.claude/agents/` in a deployed vault).

3. **Fill in the frontmatter** — set `name`, write a precise one-sentence `description`, and list the `tools` the agent needs.

4. **Write the body sections** — Role, When to Invoke, Operating Procedure, Output Format, Domain Conventions, Failure Modes. Remove placeholder text. Do not leave any `{{...}}` tokens in place.

5. **Add an entry to the routing table** in `CLAUDE.md` (or `SYSTEM_PROMPT.md`). See the example routing table below.

6. **Test with a simple Research request.** Ask the orchestrator to research a basic topic in the new domain. Verify that:
   - The correct agent is invoked.
   - Lookup runs first.
   - Output lands in `raw/research/` with correct frontmatter.
   - The agent does not auto-ingest.

---

## 7. Reserved Names

The following names are used by the template system and must not be reused for custom agents:

| Name | Role |
|---|---|
| `Generalist` | Placeholder label for the cross-domain example agent |
| `Librarian` | Placeholder label for the vault hygiene example agent |
| `Synthesizer` | Placeholder label for the synthesis example agent |

Within a deployed kit, the example agents use:

| Name | Role |
|---|---|
| `Archivist` | Cross-domain generalist research |
| `Codex` | Vault health and linting |
| `Nexus` | Cross-page synthesis and connection-finding |

---

## 8. Example Routing Table

The routing table lives in `CLAUDE.md` (or `SYSTEM_PROMPT.md`). It maps topic domains to agent slugs. The orchestrator reads this table when deciding which agent to spawn.

A completed routing table looks like this:

```markdown
## Agent Routing Table

Pick the best specialist agent directly based on the topic — no routing layer needed:

- History, historical events, civilizations → **herodotus**
- Science, physics, biology, chemistry, cosmology → **kepler**
- Literature, fiction, poetry, narrative analysis → **borges**
- Philosophy, ethics, metaphysics, epistemology → **sophia**
- Technology, software, computing, AI → **turing**
- General / cross-domain topics that don't fit a specialist → **archivist**

Agent saves output to `raw/research/YYYY-MM-DD-[TopicSlug].md`.
Do NOT auto-ingest — review first, then run `Ingest raw/research/[FileName]`.
```

Routing entries should be ordered from most specific to least specific. The generalist entry (`archivist` or equivalent) must always be last — it is the fallback.

---

## Directory Structure

```
template-vault/agents/
├── README.md          ← this file
├── _TEMPLATE.md       ← blank skeleton for new agents
└── examples/
    ├── generalist.md  ← Archivist — cross-domain research
    ├── librarian.md   ← Codex — vault health and linting
    └── synthesizer.md ← Nexus — cross-page synthesis
```
