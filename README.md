# GHCP Demo Suite

Fourteen small, focused demos showcasing **GitHub Copilot** across its key surfaces —
from comment-driven completions, through the autonomous coding agent, out to MCP
servers, hosted agents on Microsoft Foundry, and mainframe modernisation.
Each repo is self-contained; choose a learning path rather than assuming every
participant needs to complete the entire sequence.

| # | Difficulty | Repo | What it teaches |
|---|------------|------|-----------------|
| 00 | ⭐         | [`ghcp-demo-00-design-to-clickthrough`](https://github.com/xavierxmorris/ghcp-demo-00-design-to-clickthrough) | Copilot for **non-developers** — a one-page BRD becomes a clickable app, then the BRD changes and the app follows |
| 01 | ⭐         | [`ghcp-demo-01-hello-completions`](https://github.com/xavierxmorris/ghcp-demo-01-hello-completions) | Ghost-text completions, comment-driven coding |
| 02 | ⭐⭐       | [`ghcp-demo-02-python-quickfix`](https://github.com/xavierxmorris/ghcp-demo-02-python-quickfix) | Chat-assisted root-cause analysis, regression tests, and accurate documentation |
| 03 | ⭐⭐⭐     | [`ghcp-demo-03-todo-api-ts`](https://github.com/xavierxmorris/ghcp-demo-03-todo-api-ts) | Multi-file scaffolding with Chat; iterative prompt refinement |
| 04 | ⭐⭐⭐     | [`ghcp-demo-04-copilot-cli-toolkit`](https://github.com/xavierxmorris/ghcp-demo-04-copilot-cli-toolkit) | The Copilot **CLI** — terminal agent + `gh` workflows |
| 05 | ⭐⭐⭐⭐   | [`ghcp-demo-05-agents-md-customization`](https://github.com/xavierxmorris/ghcp-demo-05-agents-md-customization) | `AGENTS.md`, `copilot-instructions.md`, path-scoped rules, prompt files |
| 06 | ⭐⭐⭐⭐⭐ | [`ghcp-demo-06-coding-agent-and-review`](https://github.com/xavierxmorris/ghcp-demo-06-coding-agent-and-review) | Copilot **cloud agent** (formerly coding agent), Issue → PR, and separate **code review** |
| 07 | ⭐⭐⭐⭐⭐ | [`ghcp-demo-07-foundry-hosted-agents`](https://github.com/xavierxmorris/ghcp-demo-07-foundry-hosted-agents) | Copilot as pair-programmer for **hosted agents on Azure AI Foundry** — tool calling, grounding, deploy, evaluate, CI/CD |
| 08 | 📄 (reading) | [`ghcp-demo-08-foundry-control-plane-vs-foundry-local`](https://github.com/xavierxmorris/ghcp-demo-08-foundry-control-plane-vs-foundry-local) | **Copilot as a research tool** — a sourced brief where every claim is traced to first-party docs |
| 09 | ⭐⭐⭐⭐   | `ghcp-demo-09-figma-design-to-code` 🔒 | **MCP servers** in Copilot CLI — fixture replay, Figma access, and an assessed static HTML/CSS conversion |
| 10 | ⭐         | [`ghcp-demo-10-ato-brd-to-clickthrough`](https://github.com/xavierxmorris/ghcp-demo-10-ato-brd-to-clickthrough) | A BRD becomes a click-through app **and** a traced test pack that runs itself — separate BA and **tester** tracks |
| 11 | ⭐⭐⭐     | [`ghcp-demo-11-excel-merge-agent`](https://github.com/xavierxmorris/ghcp-demo-11-excel-merge-agent) | A **committed agent**, not a chat transcript — the agent edits YAML, deterministic Python moves the data |
| 12 | ⭐⭐⭐     | [`ghcp-demo-12-cobol-c-interop`](https://github.com/xavierxmorris/ghcp-demo-12-cobol-c-interop) | COBOL ↔ **C interop** with an explicit ABI boundary, proven on both build paths |
| 13 | ⭐⭐⭐⭐   | [`ghcp-demo-13-modernize-legacy-cobol-app`](https://github.com/xavierxmorris/ghcp-demo-13-modernize-legacy-cobol-app) | COBOL → **Node.js, Java 25, and .NET 10** with one executable **golden-master parity harness** |

🔒 = repo is **private** and requires access. Private design fixtures are not
automatically approved for redistribution.

## Continuous integration

See **[CI maintenance](CI.md)** for each demo's actual gate, intentional
workshop failures, dependency-update policy, pinned tooling, and the generated
activity-report workflow. Each standalone repository runs its own CI; the
index does not publish or clone the demos during validation.

## Go deeper

Every listed demo now has a **`WORKSHOP.md`** linked from its README: a timed
participant lab with repository-specific contracts, prompts, expected outcomes,
negative/boundary cases, troubleshooting, evidence to keep, and explicit limits.
These complement the short demos; they do not replace the starter exercises
with completed solutions.

Use **[FACILITATOR-GUIDE.md](FACILITATOR-GUIDE.md)** for all 14 workshop links,
baseline expectations, run-mode differences, and session preparation.

| Learning path | Demos | Learning outcome |
| --- | --- | --- |
| Requirements and acceptance | 00, 10 | Trace a document change to behavior and meaningful assertions |
| Developer foundations | 01-06 | Move from local suggestions to bounded, reviewed agent changes |
| Agents, evidence, and design | 07, 08, 09 | Separate tool correctness, research claims, and MCP/design evidence |
| Data and modernization | 11, 12, 13 | Protect business meaning across rules, ABI boundaries, and language changes |

Demo **00** is the odd one out on purpose: it's aimed at business analysts and
product owners rather than developers, and it needs no toolchain at all.
Demo **08** is a written research brief rather than a hands-on lab — it's here
because "use Copilot to research something and make it checkable" is a real
Copilot workflow.
Demos **10**, **12** and **13** are the modernisation track: a BRD-to-app-plus-tests
lab, a COBOL/C interop boundary, and a COBOL-to-Node.js/Java/.NET migration held honest by a
golden-master parity harness.

### Mainframe modernization to Java and .NET

| Goal | Start here | What it establishes |
| --- | --- | --- |
| Keep a rule in COBOL and review its C boundary | [Demo 12](https://github.com/xavierxmorris/ghcp-demo-12-cobol-c-interop) | Source ownership, ABI contracts, and build-path evidence |
| Move original behavior to Java/.NET/Node | [Demo 13 front page](https://github.com/xavierxmorris/ghcp-demo-13-modernize-legacy-cobol-app) | Recorded COBOL observations compared with independent ports |
| Apply the method to mainframe-shaped records | [CardDemo](https://github.com/xavierxmorris/azure-mainframe-modernization-carddemo) | A read-only .NET slice and shared Java/.NET numeric contracts |

Start with the [Copilot value guide](https://github.com/xavierxmorris/ghcp-demo-13-modernize-legacy-cobol-app/blob/main/docs/COPILOT-VALUE.md)
to separate AI assistance from compiler execution, comparison evidence, and
human approval. For a taxation-office context, use the
[original-COBOL evidence pack](https://github.com/xavierxmorris/ghcp-demo-13-modernize-legacy-cobol-app/tree/main/examples/tax-office),
not independently invented tax rules.

CardDemo is a companion repository, not a fifteenth numbered demo. The labs
do not claim automatic COBOL conversion, full mainframe parity, a productivity
percentage, or production/compliance certification.

## How to use this repo

This repo is an **index + publishing tooling** repo. Each demo is a standalone
GitHub repo — clone the one you want, follow its README, and move on to the next.

```bash
git clone https://github.com/xavierxmorris/ghcp-demo-01-hello-completions.git
```

Rough timings for the original short walkthroughs: **~3 hours** for the core path (demos 01–06), **~6 hours** if you
also do 00, 07 and 09. Demo 08 is a 15-minute read. Demos 10 and 12 each run as a
90-second presenter track or a short hands-on exercise; 11 and 13 are longer
build-and-verify labs.

The deeper workshop tracks take longer: plan **5-6 hours** for all foundation
labs, split across sessions, with setup and cloud queues additional. Individual
workshop times are estimates, not measured generation-speed claims.

> **Layout note:** if you clone all the demos as subfolders of this repo, they
> stay independent git repos. `.gitignore` excludes every `ghcp-demo-*/` folder
> so the index repo only ever tracks its own top-level files.

## Audience

These are **developer enablement** demos. They favour clarity and
repeatability over flash — every step has an expected outcome you can
verify on your own machine.

Demo 00 is the exception: it's built for **business analysts, product owners and
operations leads**, and deliberately requires no toolchain.

## Prerequisites (by demo)

| Demo | Needs |
|------|-------|
| 00    | Browser for replay; PowerShell for the runner. Copilot/network only for live authoring. |
| 01    | Copilot-enabled editor, browser, and Python 3 or another trusted HTTP server for JavaScript module imports. |
| 02    | VS Code Chat, Python 3.10+, an isolated environment, and the declared pytest dependency. |
| 03    | VS Code Chat, Node 20+, npm, and the declared TypeScript/Express 4/Vitest dependencies. |
| 04    | [Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli), Python, and Git; `gh` only for the optional GitHub exercise. |
| 05    | Supported Chat surface, Python 3.10+, and declared dependencies. Prompt-file support differs between extension-host and Agent Host sessions. |
| 06    | An eligible paid Copilot plan and allowed cloud-agent/review policies; an authorized repo/fork. Python 3.11+ and Node 20+ for local work. See the starter gaps before running. |
| 07    | Python/development requirements for offline domain tests. Azure subscription, model access, `az`, `azd`, compatible extensions, and budget for the cloud track. |
| 08    | Browser to read; network only to refresh sources. No Azure deployment. |
| 09    | Repo access. Node 18+ and PowerShell for raw replay; Python for HTTP preview. Copilot for agent-driven replay; authorized Figma client/account/file access and plan/seat allowance for live calls. |
| 10    | Browser for replay; PowerShell for the runner. Node, declared `playwright-core`, and Edge for fresh automation. |
| 11    | Python 3.10+ and the package's `dev` extra for tests. No Excel installation or database connector. Use a sample-only clone. |
| 12    | Docker Desktop for the container build, or GnuCOBOL + GCC for a native Linux run. |
| 13    | Node 20.11+ for the original port/harness. Optional Java 25 and .NET 10 SDKs for the new targets. The multi-language Docker/devcontainer includes all three plus GnuCOBOL. No application packages. |

Access and service guidance was reviewed **7 September 2026** against
[GitHub cloud-agent documentation](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent),
[code review](https://docs.github.com/en/copilot/concepts/agents/code-review), and
[Figma rate limits/access](https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/).
Quotas, previews, and organization policies can change independently of the code.

## The setup these demos were built with

Demos 04, 05, 07 and 09 explore a customised Copilot install. This is the shape
of the environment they were authored and tested against — useful as a
reference for what "configured Copilot" actually looks like in practice.

The original examples used **GitHub Copilot CLI 1.0.79** on Windows 11 /
PowerShell 7. The documentation refresh inspected **1.0.84-1** on
**7 September 2026**. These are recorded versions, not a requirement that every
demo use an identical global installation.

**MCP servers** (`~/.copilot/mcp-config.json`) — extend the agent with tools
beyond the filesystem and shell:

| Server | Transport | Why |
|--------|-----------|-----|
| [`context7`](https://github.com/upstash/context7) | local (`node`) | Current, version-accurate docs for third-party libraries and frameworks |
| [`microsoft-learn`](https://learn.microsoft.com/api/mcp) | http | First-party Microsoft / Azure / .NET docs + official code samples — the sourcing backbone for demos 07 and 08 |
| [`figma`](https://mcp.figma.com/mcp) | http | Design context, variables and screenshots for demo 09 |
| `figma-demo` | local (`node`) | Offline replay of captured Figma responses, so demo 09 can be run without burning Figma quota |

Register one with `copilot mcp add`, or `/mcp` inside the CLI. Enterprise
environments will usually add internal servers on top of these — those are
omitted here.

**Custom agents** (`~/.copilot/agents/*.agent.md`) — narrow, single-purpose
subagents that run in their own context window, layered on top of the CLI's
built-ins (`explore`, `task`, `general-purpose`, `code-review`,
`security-review`, `research`, `rubber-duck`):

- `explore` — fast read-only codebase Q&A
- `task` — runs verbose builds/tests/lints, returns the signal not the noise
- `rubber-duck` — second opinion from a *different* model family, to break
  single-model blind spots
- `python-reviewer` — house Python conventions

Project-scoped agents live in `.github/agents/` and travel with the repo.
Agent names and availability depend on the host and configuration; inspect
`/agent` and `/env` rather than assuming every listed custom agent is built in.

**Skills** (`~/.copilot/skills/`) — reusable procedural playbooks the agent
loads on demand: document generation (`docx`, `pptx`, `xlsx`), design and
front-end work (`canvas-design`, `frontend-design`, `figma-design-to-code`,
`web-design-reviewer`, `ui-screenshots`, `theme-factory`), and workflow helpers
(`code-checklist`, `loop`, `web-artifacts-builder`). Skill packs can also be
installed from plugin marketplaces — the Azure pack (`azure-deploy`,
`azure-diagnostics`, `azure-kubernetes`, `azure-cost`, and ~30 more) is what
demo 07 leans on.

**Instruction layering** — this is the single highest-leverage customisation,
and the subject of demo 05. These are different scopes of context, not a
universal override chain:

```
~/.copilot/copilot-instructions.md          personal CLI defaults
<repo>/.github/copilot-instructions.md      repository conventions
<repo>/AGENTS.md                           repository agent contract
<repo>/.github/instructions/*.instructions.md  matched file/task guidance
<subdir>/AGENTS.md                         nested guidance where supported
```

Applicable instructions are combined; avoid conflicting rules and inspect
what actually loaded. VS Code does not use custom instruction files for
inline suggestions. Nested discovery and prompt-file behavior vary by host.
See [current VS Code guidance](https://code.visualstudio.com/docs/agent-customization/custom-instructions).

**Canvases** — interactive side panels (kanban boards, whiteboards, data-flow
diagrams) for work that's easier to see than to describe in chat.

## Pushing these to GitHub

This is not a monorepo: each demo has its own Git history, remote, and working
tree. Committing the index does not commit any ignored child repository.
Inspect and commit each intended change separately before publishing.

The scripts below are **publishing tools**, not setup or validation commands.
They can create repositories and push `main`; creation is public by default.
Review the authenticated account, target list, visibility, and staged content
first, especially for private demo 09.

```powershell
# Windows / PowerShell
.\push-all.ps1
```

```bash
# macOS / Linux
./push-all.sh
```

The scripts read `repos.txt`, create missing repos under the authenticated
`gh` user, and push `main`. They do not commit new edits in already-initialized
repos, and they do not configure issue/wiki settings or establish branch
protection. `-Private` (PowerShell) or `--private` (Bash) controls creation
visibility; existing repositories are not made public by that choice.

## License

The index is MIT licensed; see `LICENSE`. Check each demo's license and any
separate rights/permissions for incorporated design assets before redistribution.
