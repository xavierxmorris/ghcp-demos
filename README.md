# GHCP Demo Suite

Ten small, focused demos showcasing **GitHub Copilot** across its key surfaces —
from comment-driven completions, through the autonomous coding agent, out to MCP
servers and hosted agents on Azure AI Foundry. They're designed to be done in
order, but each repo is self-contained.

| # | Difficulty | Repo | What it teaches |
|---|------------|------|-----------------|
| 00 | ⭐         | [`ghcp-demo-00-design-to-clickthrough`](https://github.com/xavierxmorris/ghcp-demo-00-design-to-clickthrough) | Copilot for **non-developers** — a one-page BRD becomes a clickable app, then the BRD changes and the app follows |
| 01 | ⭐         | [`ghcp-demo-01-hello-completions`](https://github.com/xavierxmorris/ghcp-demo-01-hello-completions) | Ghost-text completions, comment-driven coding |
| 02 | ⭐⭐       | [`ghcp-demo-02-python-quickfix`](https://github.com/xavierxmorris/ghcp-demo-02-python-quickfix) | Chat slash-commands: `/explain`, `/fix`, `/tests`, `/doc`, `@workspace` |
| 03 | ⭐⭐⭐     | [`ghcp-demo-03-todo-api-ts`](https://github.com/xavierxmorris/ghcp-demo-03-todo-api-ts) | Multi-file scaffolding with Chat; iterative prompt refinement |
| 04 | ⭐⭐⭐     | [`ghcp-demo-04-copilot-cli-toolkit`](https://github.com/xavierxmorris/ghcp-demo-04-copilot-cli-toolkit) | The Copilot **CLI** — terminal agent + `gh` workflows |
| 05 | ⭐⭐⭐⭐   | [`ghcp-demo-05-agents-md-customization`](https://github.com/xavierxmorris/ghcp-demo-05-agents-md-customization) | `AGENTS.md`, `copilot-instructions.md`, path-scoped rules, prompt files |
| 06 | ⭐⭐⭐⭐⭐ | [`ghcp-demo-06-coding-agent-and-review`](https://github.com/xavierxmorris/ghcp-demo-06-coding-agent-and-review) | Copilot **coding agent** (Issue → PR) + Copilot **code review** |
| 07 | ⭐⭐⭐⭐⭐ | [`ghcp-demo-07-foundry-hosted-agents`](https://github.com/xavierxmorris/ghcp-demo-07-foundry-hosted-agents) | Copilot as pair-programmer for **hosted agents on Azure AI Foundry** — tool calling, grounding, deploy, evaluate, CI/CD |
| 08 | 📄 (reading) | [`ghcp-demo-08-foundry-control-plane-vs-foundry-local`](https://github.com/xavierxmorris/ghcp-demo-08-foundry-control-plane-vs-foundry-local) | **Copilot as a research tool** — a sourced brief where every claim is traced to first-party docs |
| 09 | ⭐⭐⭐⭐   | `ghcp-demo-09-figma-design-to-code` 🔒 | **MCP servers** in Copilot CLI — register Figma, convert a design to production HTML/CSS |

🔒 = repo is currently **private**; the link will 404 until it's published.

Demo **00** is the odd one out on purpose: it's aimed at business analysts and
product owners rather than developers, and it needs no toolchain at all.
Demo **08** is a written research brief rather than a hands-on lab — it's here
because "use Copilot to research something and make it checkable" is a real
Copilot workflow.

## How to use this repo

This repo is an **index + publishing tooling** repo. Each demo is a standalone
GitHub repo — clone the one you want, follow its README, and move on to the next.

```bash
git clone https://github.com/xavierxmorris/ghcp-demo-01-hello-completions.git
```

Rough timings: **~3 hours** for the core path (demos 01–06), **~6 hours** if you
also do 00, 07 and 09. Demo 08 is a 15-minute read.

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
| 00    | Nothing. Runs off the filesystem — no install, no server, no network. |
| 01–03 | VS Code + Copilot + Copilot Chat (any seat) |
| 04    | + [GitHub Copilot CLI](https://docs.github.com/en/copilot/github-copilot-in-the-cli) |
| 05    | Any seat. Customisations are local config. |
| 06    | Copilot **Business or Enterprise** with coding agent + review enabled |
| 07    | + An **Azure subscription** with AI Foundry access, plus `az` and `azd` CLIs |
| 08    | Nothing — it's a written brief. |
| 09    | + [GitHub Copilot CLI](https://docs.github.com/en/copilot/github-copilot-in-the-cli) and a Figma account. A Figma **Dev or Full seat** is required — View/Collab seats hit a hard MCP tool-call limit. |

## The setup these demos were built with

Demos 04, 05, 07 and 09 assume a customised Copilot install. This is the shape
of the environment they were authored and tested against — useful as a
reference for what "configured Copilot" actually looks like in practice.

**GitHub Copilot CLI** `1.0.79` on Windows 11 / PowerShell 7.

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

**Skills** (`~/.copilot/skills/`) — reusable procedural playbooks the agent
loads on demand: document generation (`docx`, `pptx`, `xlsx`), design and
front-end work (`canvas-design`, `frontend-design`, `figma-design-to-code`,
`web-design-reviewer`, `ui-screenshots`, `theme-factory`), and workflow helpers
(`code-checklist`, `loop`, `web-artifacts-builder`). Skill packs can also be
installed from plugin marketplaces — the Azure pack (`azure-deploy`,
`azure-diagnostics`, `azure-kubernetes`, `azure-cost`, and ~30 more) is what
demo 07 leans on.

**Instruction layering** — this is the single highest-leverage customisation,
and the subject of demo 05. Instructions merge from broad to narrow:

```
~/.copilot/copilot-instructions.md      personal defaults, every session
  └─ <repo>/.github/copilot-instructions.md   repo-wide conventions
      └─ <repo>/AGENTS.md                     agent-facing repo contract
          └─ <subdir>/AGENTS.md               path-scoped overrides
```

**Canvases** — interactive side panels (kanban boards, whiteboards, data-flow
diagrams) for work that's easier to see than to describe in chat.

## Pushing these to GitHub

If you've cloned this monorepo locally and want to publish each demo as its
own GitHub repo:

```powershell
# Windows / PowerShell
.\push-all.ps1
```

```bash
# macOS / Linux
./push-all.sh
```

The scripts read `repos.txt`, create a public repo per line under your
authenticated `gh` user, push `main`, and disable wiki/issues defaults you
don't need.

## License

MIT for every demo. See `LICENSE`.
