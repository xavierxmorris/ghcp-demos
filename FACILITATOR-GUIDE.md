# Facilitator guide: teach the decision, not just the prompt

The suite contains **16 demos**, numbered 00–15: **15 independent repositories**
for 00–14 and a documentation-only operator guide for 15 in this index.
Each standalone demo's README provides orientation and links to a deeper `WORKSHOP.md`.
Demo 15 contains its presenter track and operator lab in the same guide.
Use the short presenter track to show the idea; use the workshop to let
participants test it, make a bounded change, and explain the evidence.

The extra plugin-spec demo is not part of this listed sequence.

## Workshop catalog

Times are planning estimates after setup. Model latency, cloud queues, image
downloads, account provisioning, and billing-report/alert delays are additional.
Links for 00–14 point to standalone repositories; publishing this index does not
publish their guide files. Demo 15 is tracked and published with this index.

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
| 14 | [Private: Jenkins pattern decisions](https://github.com/xavierxmorris/ghcp-demo-14-jenkins-to-github-actions-hackathon/blob/main/WORKSHOP.md) (access required) | 90 min lab / 3 build days | Source-linked triage, inactive reusable-workflow drafts, policy refusal, and human decisions |
| 15 | [Cost centres and AI Credit budgets](demo-15-cost-centre-ai-credits.md) | 10–15 min presenter / 45–60 min operator lab | Cohort/UUID mapping, shared versus inherited limits, effective-budget explanation, redacted evidence, and rollback |

## Choose a session

| Session | Suggested selection | Keep outside the session |
| --- | --- | --- |
| Business and testing, 90 minutes | Selected acceptance exercises from 00 and 10 | Live app generation and toolchain installation |
| Developer foundations, two half-days | 01-03, then 04-06 | Unbounded refactors and real organization housekeeping |
| AI systems and evidence, half-day | Offline 07, research 08, authorized replay 09 | Azure provisioning and live Figma access unless prepared |
| Modernization, half-day plus setup | 11-13 | Real exports, production databases, and changing legacy evidence |
| CI modernization hack, three build days | 14 | Repository migration, production CI, estate-wide conversion and unapproved data/model access |
| Enterprise cost governance, 45–60 minutes | 15; operator-led, with read-only comparison fallback | Production-default changes, deliberate threshold/pool exhaustion, and waiting for delayed reports/alerts |

Do not compress all sixteen into a single "hands-on" session. A room can watch
many demos; participants need time to inspect and challenge a smaller number.

## Before participants arrive

1. Confirm the audience, intended outcome, repository access, and available time.
2. Open each demo as its own workspace. Do not use the entire user profile or
   the index folder as the context for an individual coding exercise. Demo 15
   is the exception: read its guide here; the operator works in the enterprise UI.
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

For demo 15, separately confirm enterprise-owner or billing-manager billing
access, an authorised team administrator, appropriate Copilot licences for
non-production-critical test users, and the enterprise's current UI/API support.
Prepare before-state teams, cost centres, budgets, policies, and usage evidence.
Check collisions, stale resources, direct assignments, and every potentially
overlapping budget. Agree the maximum real spend, bounded task count, alert
recipients, stop conditions, and rollback owners. A billing role alone does not
prove permission to create enterprise teams.

**Billing safety:** AI Credits are real consumption; an alert-only budget does
not enforce a spend ceiling and reporting can lag. Do not lower or replace a
production universal budget, exhaust a pool, or deliberately block developer
work. Use ordinary authorised test-user Copilot activity only, never stafftools,
charge generators, private endpoints, or synthetic production billing emission.
If safe isolation/headroom is unverified, use comparison-only mode. Preserve
evidence, stop activity, restore only demo changes, and use GitHub Support for
unexplained attribution/enforcement. Keep raw billing data and identity mappings
outside the public repository.

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
| 14 | Python is deterministic; synthetic outcomes are not a customer conversion rate, and the default customer policy emits no drafts |
| 15 | Documentation-only; no runner or pre-created enterprise resources. Live enterprise state is unverified. ULB specificity differs from independent hard-budget headroom; future attribution/alerts can remain pending |

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
| 14 `-Manual` / `-Check` / `-Live` | Print-only commands / offline contracts / explicit-consent, read-only Copilot on shipped synthetic context; no migration or auto-merge |
| 15 no runner | UI-first operator lab; GET-only reporting examples and separately warned optional mutations, not automated billing setup |

Prefer normal interactive approval for new agent-driven work. A new folder,
source hash comparison, or an instruction saying "do not touch" is not a
security sandbox. Do not execute all-tools-allowed live modes in a valuable
working tree merely because they are convenient.

## Facilitate the learning loop

Ask participants to **predict**, **observe**, **explain**, **challenge**, and **recover**:

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
For demo 15, challenge budget-precedence assumptions by comparing settings and
effective-budget evidence, not by creating a real outage. Recover means
restoring controls and membership; it does not undo charges or historical attribution.

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
For demo 15, substitute a non-sensitive activity purpose/ledger for prompt
contents, record shared/inherited/effective-budget evidence and alert delivery
status, and require rollback confirmation. Mark delayed attribution pending;
a comparison-only session is not a live enforcement test.

Do not put personal data, credentials, private designs, or customer telemetry
into a public evidence bundle. Retain private evidence only in approved storage.

## Version-sensitive claims to recheck

Documentation refresh date: **2026-09-07** for demos 00–14; demo 15's billing
sources were checked **14 September 2026**. These sources are rolling pages;
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
| Enterprise AI Credit controls | [Demo 15 sources and boundaries](demo-15-cost-centre-ai-credits.md#references); REST **2026-03-10**, current UI labels/rollout must be rechecked; no live enterprise verification |

The refresh also observed Node **24.13.0**, Python **3.14.2**, and azd **1.28.0**.
That is not a claim that every demo was deployed or exercised on every one of
those versions. Individual guides separate local observations from historical
cloud/compiler evidence.

## Maintaining and publishing the suite

The index tracks its own files only. Child demo repos are ignored and keep their
own remotes and commits. Update a demo's README and workshop together; update
the catalog/prerequisites when a runnable contract changes.
Demo 15 is a top-level guide, so update it and both index catalogs together.
The suite has 16 demos but only 15 standalone demo repositories. Do not add a
demo-15 repository entry to `repos.txt` or create a separate repository.

`repos.txt` is a `name|description[|public or private]` publishing inventory,
not a dependency manifest. Legacy two-column entries retain their default
creation behavior. Explicit private entries are created privately and refused
if the remote is not private; the checked repository and origin push URL must match.
The publishing scripts can create repositories and push branches. They do not
commit new edits in existing repos, enable required reviews, or validate a demo.
Review visibility and account ownership explicitly, and retain demos 09 and 14's
privacy unless separately authorized to publish their contents. Keep private
source material and engagement context out of this public index.

For repeat sessions, use fresh exercise clones or preserve participant branches.
Stop only processes you started and remove only identified exercise outputs.
Do not reset an entire working tree or global Copilot configuration as cleanup.
