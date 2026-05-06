# Creating Domain Agents

Agents are domain specialists that handle Research requests routed by the
orchestrator. This guide covers when to create one, how to design it, and
how to integrate it.

---

## When to Create an Agent vs. Using the Generalist

**Use the generalist (or your Archivist orchestrator directly) when:**
- The topic is cross-domain or interdisciplinary
- You research this domain rarely (once a month or less)
- The domain is already well-covered by a specialist in another category

**Create a dedicated agent when:**
- You research this domain regularly and want consistent depth and terminology
- The domain has specialized source conventions (e.g., citing primary texts
  in their original language, using domain-specific jargon)
- The domain benefits from a distinctive voice or perspective (e.g., a
  literary historian reads differently from a data scientist)

A good heuristic: if you find yourself correcting the generalist's framing
in the same domain repeatedly, it is time to create an agent.

---

## Naming Your Agent

Agent names are thematic — they evoke the domain without being literal job
titles. Good naming conventions:

| Approach | Examples |
|----------|---------|
| Historical figure | Herodotus (history), Euclid (mathematics), Avicenna (medicine) |
| Mythological figure | Hermes (esotericism), Thoth (ancient civilizations), Janus (transitions) |
| Fictional character | Aronnax (ocean science), Borges (synthesis), Scheherazade (narrative) |
| Abstract name | Logos (philosophy), Chronos (time / history), Cosmos (astronomy) |

Avoid generic names like "HistoryBot" or "PhilosophyAssistant." Thematic
names are easier to remember in routing tables and give the agent character.

---

## Filling In the Agent Template

Open `template-vault/agents/_TEMPLATE.md`. Below is a worked example using
the history of science as a neutral domain.

### Original template fields and example values

**`name:`** The agent's chosen name.
- Example: `Copernicus`

**`domain:`** One-line description of coverage.
- Example: `History of science — development of scientific thought from
  antiquity to the modern era`

**`trigger_phrases:`** Keywords and phrases the orchestrator uses to route
  to this agent. Be specific to avoid overlap with other agents.
- Example: `scientific revolution, history of science, natural philosophy,
  Galileo, Newton, Darwin, paradigm shift`

**`persona:`** 2–4 sentences describing the agent's voice, priorities, and
  approach. This shapes output tone and citation habits.
- Example: `You are Copernicus — a historian of science who traces the
  development of ideas across time. You prioritize primary sources and
  situate discoveries in their historical context. You note when modern
  interpretations differ from how contemporaries understood events.
  You are comfortable with both the technical content of science and
  the sociology of scientific communities.`

**`output_format:`** What kind of output this agent produces.
- Example: `Standard research output following raw/templates/research-prompt.md.
  Always include a timeline of key developments. Always cite original
  publication dates, not reprint dates.`

**`languages:`** Any special language handling.
- Example: `Latin passages from historical texts should be quoted with inline
  translation. No transliteration required.`

**`save_to:`** Where the agent saves its output.
- Example: `raw/research/YYYY-MM-DD-[topic-slug].md`

---

## Adding the Agent to the Routing Table

After creating the agent file, add it to the routing table in your
`CLAUDE.md` (or `SYSTEM_PROMPT.md`).

### Claude Code format (`CLAUDE.md`)

```markdown
## Agent Routing
- History of science, scientific revolution → **copernicus**
  (.claude/agents/copernicus.md)
- History (general), archaeology → **herodotus**
  (.claude/agents/herodotus.md)
- General / cross-domain → **archivist**
  (.claude/agents/generalist.md)
```

### Other platforms (SYSTEM_PROMPT.md)

For platforms that do not support separate agent files, include the agent's
persona and output format inline in the routing table section:

```markdown
## Agent Routing

When the user runs Research on history of science or scientific revolution,
adopt the following persona and guidelines:
- Name: Copernicus
- Persona: [paste persona text]
- Output format: [paste output format text]
- Save output to: raw/research/ (if file-write is available)

When the user runs Research on general history or archaeology:
[...next agent...]
```

---

## Platform Notes

### Claude Code

Each agent is a separate Markdown file in `.claude/agents/`. Claude Code
reads these as independent agent configurations and can spawn them as
sub-sessions. The orchestrator in `CLAUDE.md` references agents by file name.

### Claude Desktop / ChatGPT / Gemini

There is no sub-agent mechanism. All agents are modes — the orchestrator
shifts persona, executes the Research task, and shifts back. Include agent
definitions inline in `SYSTEM_PROMPT.md`.

### Local models (Ollama / LM Studio)

Inline mode works the same as cloud chat platforms. With 70B+ models, mode
consistency is reliable. With smaller models, keep agent personas short
(2–3 sentences) and routing triggers specific.

---

## Testing a New Agent

After adding the agent:

1. Start a new session (for Claude Code, restart; for chat platforms, start
   a new conversation).

2. Run a routing test:
   ```
   Research the role of Johannes Kepler in the scientific revolution
   ```
   The orchestrator should route to your new Copernicus agent, not the
   generalist. Check that:
   - The orchestrator names the agent it is invoking
   - The output follows the agent's format (timeline, Latin citation style, etc.)
   - The output is saved to `raw/research/` with a dated filename

3. Run a boundary test — a query that should NOT route to the new agent:
   ```
   Research Kantian ethics
   ```
   This should go to your philosophy agent, not Copernicus. If it routes
   incorrectly, tighten the trigger phrases in the routing table.

4. Run `Lookup [concept from the research output]` to confirm the agent's
   output uses wikilink format that will work on ingest.
