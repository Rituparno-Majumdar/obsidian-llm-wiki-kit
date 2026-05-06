# Setup Guide — Local Models (Ollama / LM Studio / Open WebUI)

Running this system on a local model gives you full privacy and offline
capability. Performance depends heavily on model size and quantization.

---

## Prerequisites

- Ollama, LM Studio, or Open WebUI installed
- A capable model downloaded (see recommendations below)
- Vault copied from `template-vault/` to your Obsidian folder

---

## Setup by Platform

### Ollama

Embed the system prompt directly in a custom `Modelfile`:

```dockerfile
FROM llama3.3:70b

SYSTEM """
[Paste the full contents of template-vault/SYSTEM_PROMPT.md here.
Replace {{ORCHESTRATOR_NAME}} before pasting.]
"""
```

Build and run:

```bash
ollama create my-second-brain -f Modelfile
ollama run my-second-brain
```

The system prompt is baked into the model instance and loads automatically
every session.

To update the system prompt (e.g., after adding agents), edit the Modelfile
and rebuild: `ollama create my-second-brain -f Modelfile`

### LM Studio

1. Open LM Studio and load your model.
2. Go to the **Chat** tab.
3. Find the **System Prompt** field (in the sidebar or above the input box).
4. Paste the contents of `template-vault/SYSTEM_PROMPT.md`.
5. Replace `{{ORCHESTRATOR_NAME}}`.
6. Save the preset (optional) so you can reload it without re-pasting.

### Open WebUI

1. Open Open WebUI and go to **Settings** → **System Prompt**.
2. Create a new preset named "Second Brain".
3. Paste the contents of `template-vault/SYSTEM_PROMPT.md`.
4. Replace `{{ORCHESTRATOR_NAME}}`.
5. Set this preset as the default for your preferred model.

Alternatively, use Open WebUI's **Custom Models** feature to create a model
variant with the system prompt pre-loaded (similar to Ollama's Modelfile
approach).

---

## Model Recommendations

| Model Size | Capability |
|------------|------------|
| 70B+ (e.g., Llama 3.3 70B, Qwen 2.5 72B) | Full capability — routing, research, frontmatter, triads |
| 32B (e.g., Qwen 2.5 32B, Mistral 32B) | Good — occasional routing errors, recommend testing |
| 8B (e.g., Llama 3.1 8B, Gemma 2 9B) | Limited — reliable for Lookup and Query; struggles with complex Research routing and consistent frontmatter generation |

**Recommended baseline:** Llama 3.3 70B or Qwen 2.5 72B at Q4 quantization.
These models follow complex structured instructions reliably on modern
consumer hardware (32–64 GB RAM).

**Multilingual note:** Qwen 2.5 models have stronger multilingual capability
than Llama models. If your vault includes Chinese, Japanese, or Arabic
content, prefer a Qwen model.

---

## Limitations

**No web access.**
Local models have no internet connection. Research commands that normally
fetch URLs or search the web will fail or return only training-knowledge
results.

Workaround: provide sources manually.

```
Research the Stoic concept of ataraxia using the following text: [paste text]
```

Or use Ollama with a web-search plugin (e.g., via Open WebUI's RAG/search
integration) to restore this capability partially.

**No native file-write access.**
Like Claude Desktop and Gemini, local models cannot write files to your vault.
Copy output manually into Obsidian.

**No sub-agents.**
Local models run as a single inference process. Domain agents are simulated
as modes. With smaller models, persona consistency during agent-mode Research
may degrade in long sessions.

**Context window limits.**
Some local models have shorter effective context windows than cloud models.
If the orchestrator starts ignoring the system prompt mid-session, start a
fresh conversation.

---

## Tips for Smaller Models

If you are using an 8B or 13B model, use a shorter system prompt. Run the
wizard (`meta-prompt-wizard/WIZARD.md`) and select the **compact output**
option to generate a `SYSTEM_PROMPT_SHORT.md` with trimmed instructions.

Key instruction reductions for smaller models:
- Remove multilingual triad rules (unless you need them)
- Collapse the agent routing table to 3–4 entries maximum
- Remove the detailed frontmatter templates (keep only field names)

**Test routing explicitly** after setup. Ask:

```
Research quantum entanglement
```

The model should identify the appropriate domain (physics) and either invoke
that agent mode or name which agent it is simulating. If it just answers
directly without acknowledging agent routing, your routing table may need
simplification.

**Use Ollama's `--verbose` flag** during setup to monitor how much of the
system prompt the model is actually processing:

```bash
ollama run my-second-brain --verbose
```

Check the `eval_count` and `eval_duration` to ensure the system prompt is
being fully processed.
