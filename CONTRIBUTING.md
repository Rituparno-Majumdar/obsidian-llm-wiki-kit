# Contributing to obsidian-llm-wiki-kit

Thank you for considering a contribution. This project is a template and
documentation system — contributions that make it more useful for a wider
range of users are welcome.

---

## What Contributions Are Welcome

- **New agent examples** — domain-specific agent definitions using
  `_TEMPLATE.md`, with a completed worked example. Educational, neutral
  domains preferred (see guidelines below).
- **Platform setup guides** — if you have successfully run this system on a
  platform not covered in `docs/`, a setup guide addition is welcome.
- **Wizard improvements** — enhancements to `meta-prompt-wizard/WIZARD.md`
  that improve the generated system prompt quality.
- **Translations** — translating `SYSTEM_PROMPT.md`, `CLAUDE.md`, or docs
  into other languages (keep English as the canonical version).
- **Bug reports** — issues where the system prompt, templates, or scripts
  produce incorrect output.
- **Script improvements** — enhancements to `scripts/lint_vault.py` or
  `scripts/new_concept.py`, or new utility scripts.

---

## How to Contribute an Agent Example

Agent examples live in `template-vault/agents/examples/`. Each example
demonstrates a completed agent for a neutral, educational domain.

### Requirements

1. **Follow `_TEMPLATE.md` exactly.** Every field must be filled. No
   `{{ PLACEHOLDER }}` values left in the submitted file.
2. **Use a neutral, educational domain.** Suitable domains include:
   history of science, comparative mythology, classical literature, ecology,
   linguistics, ancient civilizations, mathematics, art history, etc.
   Avoid politically sensitive, commercially motivated, or highly personal
   domains.
3. **Include a worked example.** After the agent definition, include a
   sample Research prompt and a 200–400 word sample output showing how the
   agent would respond. Use `---` to separate the definition from the example.
4. **No personal data.** The example must not reference real people's private
   information, personal vaults, or proprietary knowledge bases.
5. **Test on at least one LLM.** Confirm that the agent definition produces
   correct routing and output when loaded in a supported LLM.

---

## Pull Request Checklist

Before submitting a PR, confirm all of the following:

- [ ] No personal data in any file (no real names of private individuals,
      no personal vault content, no API keys)
- [ ] No `{{ PLACEHOLDER }}` or `TODO` values left in submitted files
- [ ] Tested on at least one LLM (name the LLM in the PR description)
- [ ] All wikilinks in example content resolve to real or plausible page names
- [ ] New files follow the existing naming conventions
      (lowercase, hyphens, no spaces in filenames)
- [ ] Docs additions match the existing docs style (no emojis, no informal
      language in setup guides)
- [ ] If adding a script: follows the Python standards in the repo
      (click + rich + pathlib, --dry-run flag, no print())

---

## Issue Templates

### Bug Report

Please include:
- **Platform:** Claude Code / Claude Desktop / ChatGPT / Gemini / Ollama /
  LM Studio / Other
- **LLM model:** (e.g., Claude Sonnet 3.7, GPT-4o, Llama 3.3 70B)
- **Steps to reproduce:** exact command or prompt used
- **Expected behavior:** what should happen
- **Actual behavior:** what actually happened
- **System prompt version:** which version of `SYSTEM_PROMPT.md` or
  `CLAUDE.md` you are using (commit hash or date)

### Agent Suggestion

If you want a particular domain covered by a contributed agent example but
are not submitting one yourself:
- **Domain:** what subject area
- **Trigger phrases:** what Research requests should route to this agent
- **Suggested name:** a thematic name following the naming conventions in
  `docs/08-creating-agents.md`
- **Why useful:** one or two sentences on why this domain benefits from
  a dedicated agent

---

## Code of Conduct

This project follows the
[Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating,
you agree to uphold its standards.

---

## Development Setup

To test the scripts locally:

```bash
cd obsidian-llm-wiki-kit/scripts
pip install click rich
python lint_vault.py ../template-vault --dry-run
python new_concept.py ../template-vault "Test Concept" --dry-run
```

No other dependencies are required for the documentation and template files.
