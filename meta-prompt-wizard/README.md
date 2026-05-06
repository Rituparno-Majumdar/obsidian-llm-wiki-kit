# Meta-Prompt Wizard

The wizard interviews you and generates a fully personalized Obsidian LLM Wiki system — ready to copy into your vault with no manual editing.

---

## What It Does

You paste a single Markdown file into any LLM (Claude, ChatGPT, Gemini, local Ollama, or anything else). The LLM conducts a structured 5-section interview about your domains, your LLM setup, and your workflow preferences. After 12–18 minutes, it outputs all your configuration files, agent definitions, and vault init scripts — fully populated, zero placeholders.

---

## How to Use It

1. Open `WIZARD.md` (or `WIZARD_SHORT.md` for the express version).
2. Copy the entire file contents.
3. Open your LLM of choice in a fresh conversation.
4. Paste the wizard contents as your first message.
5. Follow the prompts — answer each section, then wait for the next.
6. After Section 5, the LLM generates all your output artifacts.
7. Copy each artifact into your vault:
   - `SYSTEM_PROMPT.md` → vault root (or wherever you keep your LLM's system context)
   - `CLAUDE.md` → vault root (Claude Code users only, replaces SYSTEM_PROMPT.md)
   - `agents/[name].md` → vault's `agents/` folder
   - `vault-init.sh` / `vault-init.ps1` → run once to scaffold your vault directories
8. Run the init script: `bash vault-init.sh` (add `--dry-run` first if you have existing notes).

---

## Which Variant to Use

| Variant | File | Time | Best For |
|---------|------|------|----------|
| Full wizard | `WIZARD.md` | ~15 min | New setups, capable models (GPT-4o, Claude Sonnet/Opus, Gemini 1.5 Pro+) |
| Quick wizard | `WIZARD_SHORT.md` | ~3 min | Fast starts, smaller models, or when you just want the basics |

Use the full wizard when:
- You have more than 3 domains or non-English content
- You want sub-agent or multi-mode routing
- You are using Claude Code and want the full CLAUDE.md generated

Use the quick wizard when:
- You want to be up and running in one exchange
- You are using a smaller local model (7B–13B parameter range)
- You plan to customize the output manually after generation

---

## What You Get

The full wizard (`WIZARD.md`) generates 5 artifacts:

1. **`SYSTEM_PROMPT.md`** — fully populated system prompt with your orchestrator name, domain routing, workflow rules, Karpathy enrichment protocol, and tone. Works with any LLM.
2. **`CLAUDE.md`** — same as above but using Claude Code idioms (sub-agents, terminal commands). Only generated if you pick Claude Code.
3. **Domain Agent Files** — one `agents/[name].md` per domain. Each agent has a name drawn from the domain's tradition, operating procedure, output format, and failure modes.
4. **`vault-init.sh` / `vault-init.ps1`** — shell scripts that create your full vault directory structure. Support `--dry-run` / `-DryRun` flags for safety.
5. **Routing Table** — a Markdown table mapping each domain to its agent name and trigger phrases, ready to paste into your config.

The quick wizard (`WIZARD_SHORT.md`) generates a streamlined version: `SYSTEM_PROMPT.md`, `vault-init.sh`, and a routing table.

---

## Tips

- **Works with any LLM.** The wizard uses no platform-specific syntax. Claude Code idioms only appear if you explicitly pick Claude Code in Section 2.
- **Longer, more capable models give better domain agents.** A 70B+ model will produce richer agent operating procedures and domain conventions than a 7B model. The quick wizard is calibrated for smaller models.
- **Run it again anytime.** You can re-run the wizard if your domains change, you switch LLM platforms, or you want to generate agents for new areas. Your vault content is never affected — only the config files change.
- **Existing vault safety.** The init scripts check for existing files before writing. Running them on an existing vault only creates missing directories.
- **Non-English vaults.** If any of your domains involve non-English languages, the wizard includes full multilingual triad formatting rules (native script + romanization + translation) in your system prompt.

---

## Examples

The `examples/` folder contains complete wizard transcripts with all generated artifacts:

- `example-run-philosopher.md` — Western philosophy, mythology, history of ideas. Claude Desktop, ancient Greek content.
- `example-run-developer.md` — Machine learning, distributed systems, programming language theory. ChatGPT, no sub-agents, modes-based output.
- `example-run-bilingual.md` — Japanese literature, Zen Buddhism, East Asian art history. Local Ollama, Japanese multilingual triads.
