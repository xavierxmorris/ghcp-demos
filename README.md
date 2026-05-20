# GHCP Demo Suite

Six small, focused demos showcasing **GitHub Copilot** across its key
surfaces — from comment-driven completions to the autonomous coding agent.
They're designed to be done in order, but each repo is self-contained.

| # | Difficulty | Repo | What it teaches |
|---|------------|------|-----------------|
| 01 | ⭐         | [`ghcp-demo-01-hello-completions`](./ghcp-demo-01-hello-completions) | Ghost-text completions, comment-driven coding |
| 02 | ⭐⭐       | [`ghcp-demo-02-python-quickfix`](./ghcp-demo-02-python-quickfix) | Chat slash-commands: `/explain`, `/fix`, `/tests`, `/doc`, `@workspace` |
| 03 | ⭐⭐⭐     | [`ghcp-demo-03-todo-api-ts`](./ghcp-demo-03-todo-api-ts) | Multi-file scaffolding with Chat; iterative prompt refinement |
| 04 | ⭐⭐⭐     | [`ghcp-demo-04-copilot-cli-toolkit`](./ghcp-demo-04-copilot-cli-toolkit) | The Copilot **CLI** — terminal agent + `gh` workflows |
| 05 | ⭐⭐⭐⭐   | [`ghcp-demo-05-agents-md-customization`](./ghcp-demo-05-agents-md-customization) | `AGENTS.md`, `copilot-instructions.md`, path-scoped rules, prompt files |
| 06 | ⭐⭐⭐⭐⭐ | [`ghcp-demo-06-coding-agent-and-review`](./ghcp-demo-06-coding-agent-and-review) | Copilot **coding agent** (Issue → PR) + Copilot **code review** |

## How to use this repo

Each demo is a standalone repo on GitHub. Clone the one you want, follow its
README, and move on to the next. Total walkthrough time: ~3 hours.

```bash
git clone https://github.com/xavierxmorris/ghcp-demo-01-hello-completions.git
```

## Audience

These are **developer enablement** demos. They favour clarity and
repeatability over flash — every step has an expected outcome you can
verify on your own machine.

## Prerequisites (across all six)

| Demo | Needs |
|------|-------|
| 01–03 | VS Code + Copilot + Copilot Chat (any seat) |
| 04    | + [GitHub Copilot CLI](https://docs.github.com/en/copilot/github-copilot-in-the-cli) |
| 05    | Any seat. Customisations are local config. |
| 06    | Copilot **Business or Enterprise** with coding agent + review enabled |

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
