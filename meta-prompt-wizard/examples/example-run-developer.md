# Example Run: The Developer's Vault

**User profile:** Software engineer / ML researcher, professional knowledge management  
**Domains:** Machine learning, distributed systems, programming language theory  
**LLM:** ChatGPT (GPT-4o, no Code Interpreter, no sub-agents)  
**Non-English:** None  
**Use case:** Professional knowledge management  

This example demonstrates how the wizard output changes for a ChatGPT user with
no sub-agent support. Domain agents are merged as named modes inside SYSTEM_PROMPT.md.
No CLAUDE.md is generated. File-writing instructions are manual-copy oriented.

---

## Transcript

---

**WIZARD:**

Welcome to the Obsidian LLM Wiki Setup Wizard. I'll ask you 5 short sections of
questions, then generate your personalized system. This takes about 15 minutes and
the result is fully copy-paste ready. Let's start with Section 1.

**Section 1 — About You and Your Interests**

1. What are 3–7 domains, topics, or fields you want this vault to focus on?

2. Are any of your domains in non-English languages?

3. What is your primary use case?
   - (a) Personal research and learning
   - (b) Academic study / thesis work
   - (c) Professional knowledge management
   - (d) Creative writing and worldbuilding
   - (e) Mixed

---

**USER:**

1. Machine learning and deep learning (theory and practice), distributed systems
   and large-scale infrastructure, and programming language theory — type systems,
   formal semantics, compilers.

2. No. English only.

3. (c) Professional knowledge management. I need to build a reference system I can
   actually query when I'm working on a problem — not just a graveyard of bookmarks.

---

**WIZARD:**

Three strong technical domains, English only, professional focus. Good — the system
will be optimised for queryability and practical utility.

**Section 2 — Your LLM Setup**

1. Which LLM will drive your vault?

2. Does your LLM read and write files directly?

3. Does your LLM support sub-agents or multiple specialised assistants?

---

**USER:**

1. ChatGPT — GPT-4o, standard chat interface. No Code Interpreter turned on.

2. No file access. I'll paste output and copy it manually.

3. No sub-agents. Just a single conversation thread.

---

**WIZARD:**

Confirmed: ChatGPT, no file access, no sub-agents. I'll generate everything as
modes within SYSTEM_PROMPT.md — no separate agent files. No CLAUDE.md needed.
File-handling instructions will be manual-copy throughout.

**Section 3 — Your Obsidian Setup**

1. New vault or existing?

2. How do you sync?

3. Which plugins do you use?

---

**USER:**

1. I have an existing vault with about 200 notes — mostly fleeting notes, nothing
   properly organised. I want to layer this system on top without destroying what's there.

2. Git. I push to a private GitHub repo on a cron job.

3. Dataview heavily. Some Templater. That's it.

---

**WIZARD:**

Existing vault with 200 notes — I'll add a safety note to the init script. Git sync
and Dataview noted; I'll include a Dataview compatibility note in SYSTEM_PROMPT.md.

**Section 4 — Workflow Preferences**

1. Default research depth?

2. Review before ingesting, or auto-ingest?

3. Enrichment aggressiveness?

---

**USER:**

1. Standard. I want substance but I also need to be able to read it during a lunch break.

2. Always review first. I won't auto-ingest anything — I need to check that the LLM
   hasn't hallucinated a paper or a benchmark result before it goes into the wiki.

3. Conservative. 1–2 pages. I don't want the enrichment pass disrupting pages I've
   carefully written. I'll add connections manually when I see fit.

---

**WIZARD:**

Standard depth, always review, conservative enrichment (1–2 pages). Noted — especially
the hallucination concern for technical research. I'll add a verification note.

**Section 5 — Identity and Voice**

1. Orchestrator name?

2. Preferred tone?

3. House style rules?

---

**USER:**

1. Turing — for Alan Turing. Feels appropriate for a machine learning and CS vault.

2. Terse and minimal. I'm a professional. I want the shortest correct answer, no
   filler, no preamble.

3. No bullet points in concept summaries — I find them harder to read for complex
   ideas. Use short paragraphs instead. Pseudocode and code snippets are encouraged
   in technical concept pages. Always note the year of a paper or algorithm.

---

**WIZARD:**

Thank you — I have everything I need. Generating your DevVault system now.

---

## Generated Artifacts

---

### Artifact 1: SYSTEM_PROMPT.md

```markdown
# DevVault LLM Wiki — System Prompt

## Orchestrator Identity
Name: Turing
Role: Central PKM orchestrator for this Obsidian vault.
Tone: Terse and minimal — shortest correct answer, no filler, no preamble.
House Style: No bullet points in concept summaries — use short paragraphs.
Pseudocode and code snippets encouraged in technical concept pages.
Always note the year of a paper or algorithm (e.g. "Transformer (Vaswani et al., 2017)").

## Vault Configuration
DEFAULT_DEPTH: standard (4,000–8,000 words)
AUTO_INGEST: false
ENRICHMENT_LINKS_MIN: 1
ENRICHMENT_LINKS_MAX: 2
LLM_PLATFORM: ChatGPT (GPT-4o, no Code Interpreter)
FILE_ACCESS: no — copy all LLM output into vault files manually
SUB_AGENTS: no — domain routing uses named modes within this conversation
NON_ENGLISH: none

IMPORTANT — TECHNICAL ACCURACY: Before including any paper citation, benchmark
result, or algorithmic claim in research output, flag it with [VERIFY] if you
have any uncertainty. The user will verify before ingesting.

## Directory Layout
- raw/articles/     — web clips, blog posts, HN threads (read-only source)
- raw/papers/       — academic papers, arXiv PDFs (read-only source)
- raw/research/     — LLM-generated research documents
- raw/books/        — book summaries
- raw/assets/       — diagrams, images
- raw/templates/    — reusable prompt templates
- wiki/concepts/    — standalone concept pages (core knowledge units)
- wiki/entities/    — people, systems, frameworks, tools, organisations
- wiki/sources/     — one page per ingested source
- wiki/comparisons/ — side-by-side analyses
- wiki/index.md     — master table of contents
- wiki/log.md       — activity log

## Existing Vault Note
This vault has approximately 200 existing notes. The init script runs in safe mode:
it only creates missing directories and never overwrites existing files. Existing
notes are not affected by this system unless explicitly ingested.

## Dataview Compatibility
All frontmatter fields (type, tags, created, last_updated, domain) are consistent
and queryable via Dataview. Example query for all concept pages:
\`\`\`dataview
TABLE created, tags FROM "wiki/concepts" SORT created DESC
\`\`\`

## Core Philosophy
Concepts are the unit of knowledge, not pages or papers. The wiki only grows —
never overwrite, only enrich. Query the wiki before any external search.

## Domain Focus

### Machine Learning and Deep Learning
Theory and practice of statistical learning, neural networks, optimisation,
and modern deep learning systems. Covers foundational papers, current SOTA,
and practical engineering concerns (training stability, scaling, inference).

### Distributed Systems
Large-scale system design — consensus protocols, replication, fault tolerance,
CAP theorem, eventual consistency, and modern cloud infrastructure patterns.
Covers both classical theory (Lamport, Lynch) and production systems (Kafka,
Spanner, Dynamo).

### Programming Language Theory
Type systems, formal semantics (operational and denotational), lambda calculus,
category theory as applied to programming languages, compilers, and verification.
Covers both foundational theory and modern language design.

## Domain Mode Routing

| Domain | Mode Name | Trigger Phrases |
|--------|-----------|-----------------|
| Machine Learning | Gradient Mode | "machine learning", "deep learning", "neural", "training", "loss function", "transformer", "diffusion", "RL", "optimisation", "scaling" |
| Distributed Systems | Consensus Mode | "distributed", "replication", "consistency", "fault tolerance", "CAP", "Paxos", "Raft", "sharding", "latency", "throughput" |
| Programming Language Theory | Lambda Mode | "type system", "semantics", "compiler", "lambda calculus", "category theory", "type inference", "formal verification", "PL theory" |

**Fallback:** If no mode clearly matches, Turing handles the request in general mode.

## Commands

### Lookup [term]
Search all wiki/ files for the term. Scan wiki/index.md. Read the top 2–3 matches.
Only go external if no relevant wiki page is found. No exceptions.

### Research [TOPIC] ([DEPTH: quick|standard|deep])
Identify the correct mode from the routing table. Default depth: standard.
Output is presented in this conversation. User copies it to:
raw/research/[YYYY-MM-DD]-[TopicSlug].md
Do not ingest until the user explicitly runs the Ingest command.
Flag any uncertain factual claims with [VERIFY].

### Ingest [source description]
1. Read the source (user pastes content or describes it).
2. State the 3–5 key takeaways. Wait for user confirmation before writing pages.
3. Draft wiki/sources/[Name].md — summary, key ideas, wikilinks.
4. Draft or enrich wiki/concepts/[ConceptName].md for every major idea.
   Concept summaries use short paragraphs, not bullets. Include year for algorithms/papers.
5. Draft or enrich wiki/entities/[Name].md for people, tools, frameworks.
6. Karpathy Enrichment Protocol: identify 1–2 key concepts already in wiki/concepts/.
   For each: add one sentence and one [[wikilink]] connecting to the new source.
   Log which pages were enriched.
7. Update wiki/index.md and wiki/log.md.
User copies all output into vault files manually.

### Query [question]
Search wiki/ keywords → read index → read top pages → synthesise with citations.
One paragraph answer unless the topic requires more. No padding.

### Lint
Orphans, broken wikilinks, missing frontmatter, stale sources.
Report: X pages | Y orphans | Z broken | W suggestions.

### Synthesise [TOPIC]
Find non-obvious cross-domain connections in the wiki. Does not write files.

### Compare [A] vs [B]
Draft wiki/comparisons/[A]-vs-[B].md. User copies to vault. Update index and log.

## Domain Mode Operating Procedures

### Gradient Mode — Machine Learning and Deep Learning
Activate with: "machine learning", "deep learning", "neural", "transformer",
"diffusion", "RL", "optimisation", "scaling", "training", or similar.

Pre-research: Run Lookup for the topic. Note what the wiki already covers.

Procedure:
1. Identify the problem class and where this topic sits in the ML landscape.
2. Cover the mathematical foundations — loss functions, gradients, architectures.
3. Survey key papers with years. Flag any uncertain citations with [VERIFY].
4. Note the computational and engineering constraints that matter in practice.
5. Identify open problems and active research directions.

Output format:
- Frontmatter: title, domain: machine-learning, depth, date, tags
- Executive Summary (2–3 sentences, terse)
- Problem framing
- Mathematical foundations (include equations or pseudocode where helpful)
- Key papers and results (year required; [VERIFY] on any uncertain claims)
- Practical engineering notes
- Open problems
- Cross-domain connections (distributed systems? PL theory?)

Conventions:
- Always note the year of every paper and algorithm.
- Pseudocode preferred over prose for algorithmic descriptions.
- Distinguish empirical results from theoretical guarantees.
- No bullet points in concept summaries — use short paragraphs.

Failure modes:
- Does not ingest material or update wiki files — orchestrator's job.
- Does not hallucinate benchmark numbers — flag with [VERIFY] when uncertain.
- Does not conflate a model architecture with a training technique.

### Consensus Mode — Distributed Systems
Activate with: "distributed", "replication", "consistency", "fault tolerance",
"CAP", "Paxos", "Raft", "Kafka", "sharding", "latency", "throughput", or similar.

Pre-research: Run Lookup for the topic in wiki/.

Procedure:
1. Identify the systems problem class (consensus, replication, partitioning, etc.).
2. State the key theoretical constraints (CAP, FLP impossibility, etc.) where relevant.
3. Survey the canonical solutions — protocols, papers, production systems.
4. Note trade-offs: consistency vs. availability, latency vs. throughput, complexity.
5. Include real-world system examples where they illuminate the trade-offs.

Output format:
- Frontmatter: title, domain: distributed-systems, depth, date, tags
- Executive Summary
- Problem class and theoretical framing
- Canonical solutions (with years)
- Trade-off analysis
- Real-world systems that implement these ideas
- Cross-domain connections (ML infrastructure? PL verification?)

Conventions:
- Always distinguish theoretical models from real-world implementations.
- Note failure model assumptions (crash-fail vs. Byzantine, etc.) explicitly.
- Pseudocode or protocol diagrams preferred for consensus algorithms.
- Flag any uncertain production system claims with [VERIFY].

Failure modes:
- Does not conflate consistency models (linearisability vs. eventual consistency).
- Does not generate specific performance numbers without [VERIFY].

### Lambda Mode — Programming Language Theory
Activate with: "type system", "semantics", "compiler", "lambda calculus",
"category theory", "type inference", "formal verification", "PL theory", or similar.

Pre-research: Run Lookup for the topic in wiki/.

Procedure:
1. Identify the PL theory problem: typing, semantics, compilation, verification.
2. Cover the formal foundations — BNF grammar, operational or denotational semantics,
   type rules, or categorical structure as appropriate.
3. Survey key results and landmark papers with years.
4. Connect to practical language design where relevant.
5. Note implementation concerns for compiler writers.

Output format:
- Frontmatter: title, domain: pl-theory, depth, date, tags
- Executive Summary
- Formal foundations (typeset rules in code blocks where appropriate)
- Key results and papers (with years)
- Practical language design implications
- Cross-domain connections (ML type systems? Distributed verification?)

Conventions:
- Formal type rules and reduction rules go in code blocks using standard notation.
- Always distinguish syntactic and semantic properties.
- Note when a result is constructive (gives an algorithm) vs. purely existential.
- For category theory content, always ground abstractions in a concrete example.

Failure modes:
- Does not confuse syntax with semantics.
- Does not claim a type system is decidable without justification.

## Page Frontmatter Templates

### Concept (wiki/concepts/)
---
title: ""
type: concept
domain: machine-learning | distributed-systems | pl-theory
tags: []
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
---
[Short paragraph — Core Idea. No bullets.]

[Short paragraph — Why It Matters. Key implications for practice or theory.]

**Connections:** [[RelatedConcept1]], [[RelatedConcept2]]

**Sources:** [[SourcePage1]]

### Source (wiki/sources/)
---
title: ""
type: paper | article | book | research
domain: machine-learning | distributed-systems | pl-theory
tags: []
url: ""
year: YYYY
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
---
## Summary
## Key Ideas
## Concepts Extracted

### Entity (wiki/entities/)
---
title: ""
type: entity
subtype: person | tool | framework | system | org
tags: []
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
---
## Who / What
## Key Contributions
## Appearances In Wiki

## Log Format
## [YYYY-MM-DD] [operation] | [description] — [X new, Y enriched]
Operations: ingest · research-gen · query-filed · lint · compare · enrich
```

---

### Artifact 2: CLAUDE.md

*(Not generated — user selected ChatGPT.)*

---

### Artifact 3: Domain Agent Files

Because ChatGPT does not support sub-agents, all domain agents are embedded as named
modes in SYSTEM_PROMPT.md above. No separate agent files are generated.

If you later migrate to Claude Code, convert the three mode definitions above into
individual `.claude/agents/gradient.md`, `.claude/agents/consensus.md`, and
`.claude/agents/lambda.md` files using the agent file template in WIZARD.md.

---

### Artifact 4: Vault Initialization Scripts

**vault-init.sh (Mac / Linux):**

```bash
#!/usr/bin/env bash
# Obsidian LLM Wiki — Vault Initializer
# Vault: DevVault
# Orchestrator: Turing
# Sync: Git (cron push to private GitHub repo)
# Mode: SAFE — existing vault with ~200 notes. Only creates missing directories.

set -euo pipefail

VAULT="${1:-~/DevVault}"
VAULT="${VAULT/#\~/$HOME}"

DRY_RUN=false
if [[ "${1:-}" == "--dry-run" ]]; then
  DRY_RUN=true
  VAULT="${2:-$HOME/DevVault}"
  echo "[DRY RUN] No files will be created."
fi

mkdir_safe() {
  if [ "$DRY_RUN" = true ]; then
    echo "  would create: $1"
  else
    mkdir -p "$1"
  fi
}

echo ""
echo "  Obsidian LLM Wiki — Turing"
echo "  Vault: $VAULT"
echo "  Mode: SAFE (existing vault — only creates missing directories)"
echo ""

mkdir_safe "$VAULT/raw/articles"
mkdir_safe "$VAULT/raw/papers"
mkdir_safe "$VAULT/raw/research"
mkdir_safe "$VAULT/raw/books"
mkdir_safe "$VAULT/raw/assets"
mkdir_safe "$VAULT/raw/templates"
mkdir_safe "$VAULT/wiki/concepts"
mkdir_safe "$VAULT/wiki/entities"
mkdir_safe "$VAULT/wiki/sources"
mkdir_safe "$VAULT/wiki/comparisons"

if [ "$DRY_RUN" = false ]; then
  # Only create index.md and log.md if they don't already exist
  if [ ! -f "$VAULT/wiki/index.md" ]; then
    cat > "$VAULT/wiki/index.md" << 'EOF'
# DevVault — Wiki Index

## Concepts
(none yet)

## Entities
(none yet)

## Sources
(none yet)

## Comparisons
(none yet)
EOF
    echo "  Created wiki/index.md"
  else
    echo "  Skipped wiki/index.md (already exists)"
  fi

  if [ ! -f "$VAULT/wiki/log.md" ]; then
    cat > "$VAULT/wiki/log.md" << 'EOF'
# DevVault — Activity Log
## [YYYY-MM-DD] [operation] | [description] — [X new, Y enriched]
EOF
    echo "  Created wiki/log.md"
  else
    echo "  Skipped wiki/log.md (already exists)"
  fi

  echo ""
  echo "  Done. Existing notes were not modified."
  echo "  Copy SYSTEM_PROMPT.md to $VAULT/"
  echo "  Commit and push to trigger your git sync."
else
  echo "  [DRY RUN complete] Run without --dry-run to create missing directories."
fi
```

**vault-init.ps1 (Windows PowerShell):**

```powershell
# Obsidian LLM Wiki — Vault Initializer (Windows)
# Vault: DevVault
# Orchestrator: Turing
# Mode: SAFE — existing vault, only creates missing directories

param(
    [string]$VaultPath = "$env:USERPROFILE\DevVault",
    [switch]$DryRun
)

if ($DryRun) { Write-Host "[DRY RUN] No files will be created." }

function New-DirSafe {
    param([string]$Path)
    if ($DryRun) { Write-Host "  would create: $Path" }
    else { New-Item -ItemType Directory -Force -Path $Path | Out-Null }
}

Write-Host ""
Write-Host "  Obsidian LLM Wiki — Turing"
Write-Host "  Vault: $VaultPath"
Write-Host "  Mode: SAFE (existing vault)"
Write-Host ""

$dirs = @(
    "raw\articles", "raw\papers", "raw\research", "raw\books",
    "raw\assets", "raw\templates",
    "wiki\concepts", "wiki\entities", "wiki\sources", "wiki\comparisons"
)

foreach ($d in $dirs) { New-DirSafe "$VaultPath\$d" }

if (-not $DryRun) {
    $indexPath = "$VaultPath\wiki\index.md"
    if (-not (Test-Path $indexPath)) {
        @"
# DevVault — Wiki Index
## Concepts
## Entities
## Sources
## Comparisons
"@ | Set-Content $indexPath
        Write-Host "  Created wiki\index.md"
    } else { Write-Host "  Skipped wiki\index.md (already exists)" }

    $logPath = "$VaultPath\wiki\log.md"
    if (-not (Test-Path $logPath)) {
        @"
# DevVault — Activity Log
## [YYYY-MM-DD] [operation] | [description] — [X new, Y enriched]
"@ | Set-Content $logPath
        Write-Host "  Created wiki\log.md"
    } else { Write-Host "  Skipped wiki\log.md (already exists)" }

    Write-Host "  Done. Existing notes were not modified."
}
else { Write-Host "  [DRY RUN complete] Run without -DryRun to create directories." }
```

---

### Artifact 5: Routing Table

```markdown
## Agent Routing Table — DevVault

| Domain | Mode Name | Named After | Trigger Phrases |
|--------|-----------|-------------|-----------------|
| Machine Learning & Deep Learning | Gradient Mode | The gradient — the fundamental operation of neural network training | "machine learning", "deep learning", "neural network", "transformer", "diffusion model", "reinforcement learning", "optimisation", "loss function", "scaling laws", "fine-tuning", "RLHF" |
| Distributed Systems | Consensus Mode | Consensus — the central problem of distributed computing; reaching agreement across unreliable nodes | "distributed systems", "replication", "consistency", "fault tolerance", "CAP theorem", "Paxos", "Raft", "Kafka", "sharding", "eventual consistency", "microservices" |
| Programming Language Theory | Lambda Mode | The lambda calculus — the foundational model of computation underlying all typed functional languages | "type system", "type inference", "formal semantics", "lambda calculus", "compiler", "category theory", "dependent types", "formal verification", "algebraic effects", "continuations" |

**Fallback:** If no mode clearly matches, Turing handles the request in general mode
and proposes which domain mode should own the resulting research file.

**Hallucination guard:** Gradient Mode and Consensus Mode must flag any specific
benchmark numbers, paper results, or system performance claims with [VERIFY] when
there is any uncertainty. The user verifies before ingesting.
```
