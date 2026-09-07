# Facilitator guide: teach the decision, not just the prompt

The suite contains **14 independent repositories**, numbered 00-13.
Each demo's README provides orientation and links to a deeper `WORKSHOP.md`.
Use the short presenter track to show the idea; use the workshop to let
participants test it, make a bounded change, and explain the evidence.

The extra plugin-spec demo is not part of this listed sequence.

## Workshop catalog

Times are planning estimates after setup. Model latency, cloud queues, image
downloads, and account provisioning are additional. Links point to the standalone
repositories; publishing this index does not publish their guide files.

| Demo | Deeper guide | Suggested time | Participant deliverable |
| --- | --- | --- | --- |
| 00 | [Requirements to acceptance](https://github.com/xavierxmorris/ghcp-demo-00-design-to-clickthrough/blob/main/WORKSHOP.md) | 45-60 min | Manual acceptance matrix and v1.1 impact assessment |
| 01 | [Explainable completions](https://github.com/xavierxmorris/ghcp-demo-01-hello-completions/blob/main/WORKSHOP.md) | 30 min | Input/output contract and a detected leap-year defect |
| 02 | [Root-cause debugging](https://github.com/xavierxmorris/ghcp-demo-02-python-quickfix/blob/main/WORKSHOP.md) | 45 min | Focused pricing repair and controlled promo-date tests |
| 03 | [Reviewable API slices](https://github.com/xavierxmorris/ghcp-demo-03-todo-api-ts/blob/main/WORKSHOP.md) | 60-75 min | Domain/HTTP contract, negative cases, and coherent build output |
| 04 | [Bounded terminal automation](https://github.com/xavierxmorris/ghcp-demo-04-copilot-cli-toolkit/blob/main/WORKSHOP.md) | 45-60 min | Dry-run byte checks and source-lined log analysis |
| 05 | [Testable instruction contracts](https://github.com/xavierxmorris/ghcp-demo-05-agents-md-customization/blob/main/WORKSHOP.md) | 60 min | Controlled comparison and Decimal boundary tests |
| 06 | [Delegation and review](https://github.com/xavierxmorris/ghcp-demo-06-coding-agent-and-review/blob/main/WORKSHOP.md) | 60-90 min | Agent-ready issue, acceptance matrix, reviewed revision |
| 07 | [Tools versus agent quality](https://github.com/xavierxmorris/ghcp-demo-07-foundry-hosted-agents/blob/main/WORKSHOP.md) | 60 min offline | Tool contract and correctly targeted evaluation plan |
| 08 | [Falsifiable research](https://github.com/xavierxmorris/ghcp-demo-08-foundry-control-plane-vs-foundry-local/blob/main/WORKSHOP.md) | 45 min | Claim ledger and architecture decision record |
| 09 | [Private: MCP and design evidence](https://github.com/xavierxmorris/ghcp-demo-09-figma-design-to-code/blob/main/WORKSHOP.md) (access required) | 45 min | Fixture provenance and design/accessibility scorecard |
| 10 | [Requirements versus assertions](https://github.com/xavierxmorris/ghcp-demo-10-ato-brd-to-clickthrough/blob/main/WORKSHOP.md) | 60 min | Independent arithmetic and a classified failure report |
| 11 | [Reconciliation semantics](https://github.com/xavierxmorris/ghcp-demo-11-excel-merge-agent/blob/main/WORKSHOP.md) | 60 min | Approved field/rule decisions and observed run evidence |
| 12 | [The maintained ABI boundary](https://github.com/xavierxmorris/ghcp-demo-12-cobol-c-interop/blob/main/WORKSHOP.md) | 60 min | Field-level ABI explanation and two-path build evidence |
| 13 | [Characterization and remediation](https://github.com/xavierxmorris/ghcp-demo-13-modernize-legacy-cobol-app/blob/main/WORKSHOP.md) | 75 min | Legacy observation, modern outcome, and sign-off rationale |

## Choose a session

| Session | Suggested selection | Keep outside the session |
| --- | --- | --- |
| Business and testing, 90 minutes | Selected acceptance exercises from 00 and 10 | Live app generation and toolchain installation |
| Developer foundations, two half-days | 01-03, then 04-06 | Unbounded refactors and real organization housekeeping |
| AI systems and evidence, half-day | Offline 07, research 08, authorized replay 09 | Azure provisioning and live Figma access unless prepared |
| Modernization, half-day plus setup | 11-13 | Real exports, production databases, and changing legacy evidence |

Do not compress all fourteen into a single "hands-on" session. A room can watch
many demos; participants need time to inspect and challenge a smaller number.

## Before participants arrive

1. Confirm the audience, intended outcome, repository access, and available time.
2. Open each demo as its own workspace. Do not use the entire user profile or
   the index folder as the context for an individual coding exercise.
3. Record Git revision, runtime/editor/CLI versions, selected model, and any
   nondefault instructions, agents, skills, or MCP servers.
4. Prepare a dedicated clone and synthetic fixtures. Preserve existing work.
5. Run the appropriate baseline and record expected failures or skips.
6. Pre-authorize accounts and budgets separately from code/tool permissions.
7. Keep an honest fallback: shipped pages, captured evidence, or local analysis.
   A replay is not a live run.

Use the README's prerequisites, not a blanket "any Copilot seat and no setup."
Cloud-agent policy, code-review policy, Figma access, and Azure permissions are
separate gates.

## Know the starting state

| Demo | Important baseline distinction |
| --- | --- |
| 00 | `-Check` checks assets; historical browser assertions are not rerun |
| 01 | Helpers are empty; serve JavaScript modules over HTTP |
| 02 | Two pricing failures are intentional; do not patch them before the learner exercise |
| 03 | Repository/router/server stubs and a build-root mismatch are learner work |
| 04 | No dry-run/argparse yet; transcript output is not the current CSV contract |
| 05 | One subtotal test passes while tax remains unimplemented |
| 06 | PATCH, browser-origin, frontend-test/lockfile, and historical review-workflow gaps are explicit starter work |
| 07 | Offline tests do not validate the model; saved eval configs are historical/nonportable |
| 08 | July feature matrix is dated; September refresh is scoped, not comprehensive |
| 09 | Raw replay is local; the full runner changes user configuration and output |
| 10 | Preflight can exit zero while reporting stale saved results |
| 11 | Current drift is semantically meaningful; `-Drift` restores clean samples afterward |
| 12 | Two build paths share a compiler and are not independent implementations |
| 13 | Node-only success is not fresh COBOL replay; compare remediation claims to scenario IDs |

An expected failure is a teaching artifact. An environment failure is a setup
problem. An unexpected regression is a defect. Do not conflate them to improve
a pass count.

## There is no universal runner contract

Inspect the particular runner before executing it. Flag names are not consistent
enough to infer behavior across the suite.

| Runner | Important behavior |
| --- | --- |
| 00 `-Manual` / `-Live` | Presenter pacing / all-tools-allowed generation in the current clone |
| 10 `-Verify` / `--target` | Writes saved results and can bootstrap unspecified dependencies / alternate-target checks leave saved results unchanged |
| 11 `-Manual` / `-Drift` | Prints commands / generates, rejects, then restores synthetic fixtures |
| 12 `-Check` / `-Live` | Recreates build output / copied-workspace guardrail challenge |
| 13 `-Manual` / `-Live` | Prints commands / pauses through the verification story |
| 09 full runner/reset | User skill/MCP changes and an all-interface preview; reset deletes generated output, and `-Screenshot` overwrites a reference with an unpinned tool |

Prefer normal interactive approval for new agent-driven work. A new folder,
source hash comparison, or an instruction saying "do not touch" is not a
security sandbox. Do not execute all-tools-allowed live modes in a valuable
working tree merely because they are convenient.

## Facilitate the learning loop

Ask participants to **predict**, **observe**, **explain**, and **challenge**:

| Step | Facilitator prompt | Evidence |
| --- | --- | --- |
| Predict | What should happen, and which contract says so? | Independent expected result |
| Observe | What did the actual command or UI do? | Output, screenshot, or trace |
| Explain | Which code, rule, or source accounts for the result? | File/rule/case/source reference |
| Challenge | What deliberate error would this check detect? | Meaningful failing case |
| Recover | Did the bounded correction restore the contract? | Focused rerun and diff |

Avoid the "better prompt always produces better code" storyline. A model may
succeed without the extra instruction or fail with it. Measure what happened.
Do not require participants to stage a model failure to make the talk work.

## Evidence and acceptance rubric

| Level | What the participant can show |
| --- | --- |
| Demonstrated | Reproduces the supplied happy path and explains the tool used |
| Understood | Explains a negative/boundary case and cites the governing contract |
| Applied | Makes a bounded change with regression evidence and no unrelated edits |
| Evaluated | Identifies limitations, tests the test/oracle, and justifies a release decision |

Use this as a learning rubric, not a certification of production readiness.
Each participant's handoff should contain the revision, versions, input/context,
prompt, expected versus observed result, relevant diff, and unresolved limitations.
Include observed elapsed time only if it was actually measured.

Do not put personal data, credentials, private designs, or customer telemetry
into a public evidence bundle. Retain private evidence only in approved storage.

## Version-sensitive claims to recheck

Documentation refresh date: **2026-09-07**. These sources are rolling pages;
their retrieval date is not an invented product release date.

| Topic | Current source / boundary |
| --- | --- |
| CLI behavior | [CLI docs](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli); local help inspected at **1.0.84-1** |
| Instruction scope | [VS Code instructions](https://code.visualstudio.com/docs/agent-customization/custom-instructions); no inline-suggestion application or guaranteed combined order |
| Prompt files | [VS Code prompt files](https://code.visualstudio.com/docs/agent-customization/prompt-files); extension-host versus Agent Host distinction |
| Cloud agent / review | [Cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent) and [review](https://docs.github.com/en/copilot/concepts/agents/code-review); separate policies, optional approval preview |
| Hosted-agent costs | [Foundry hosted agents](https://learn.microsoft.com/azure/foundry/agents/concepts/hosted-agents); active-session compute as well as model/evaluation use |
| Figma | [Access and limits](https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/); plan, seat, client, and read-tool exemptions |
| COBOL | [GnuCOBOL](https://gnucobol.sourceforge.io/); stable **3.2**, released **2023-07-28**, distinct from the demos' 3.1.2 baseline |

The refresh also observed Node **24.13.0**, Python **3.14.2**, and azd **1.28.0**.
That is not a claim that every demo was deployed or exercised on every one of
those versions. Individual guides separate local observations from historical
cloud/compiler evidence.

## Maintaining and publishing the suite

The index tracks its own files only. Child demo repos are ignored and keep their
own remotes and commits. Update a demo's README and workshop together; update
the catalog/prerequisites when a runnable contract changes.

`repos.txt` is a `name|description` publishing inventory, not a dependency manifest.
The publishing scripts can create repositories and push branches. They do not
commit new edits in existing repos, enable required reviews, or validate a demo.
Review visibility and account ownership explicitly, and retain demo 09's privacy
unless separately authorized to publish its contents.

For repeat sessions, use fresh exercise clones or preserve participant branches.
Stop only processes you started and remove only identified exercise outputs.
Do not reset an entire working tree or global Copilot configuration as cleanup.
