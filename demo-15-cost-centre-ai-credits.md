# Demo 15: cost centres and AI Credit budgets

An **operator/facilitator-led GitHub Enterprise Cloud billing demo**, not a
coding exercise. Target:
[GB18030-Action](https://github.com/enterprises/GB18030-Action).
This guide lives in the suite index; there is no separate demo repository or runner.
Use the [facilitator guide](FACILITATOR-GUIDE.md) for the shared learning rubric.

**Feature-validation note — 14 September 2026:** checked against the official
public sources in [References](#references), including REST API version
**2026-03-10**. These are rolling documentation pages, not dated release notes.
**GitHub billing features and UI labels can change.** No live configuration,
entitlement, enforcement, or usage in GB18030-Action was verified when writing
this guide. Recheck the current documentation and the enterprise UI before
each session. Prefer the UI if the API and UI differ.

> [!WARNING]
> AI Credit use is real billable consumption: included credits are finite and
> additional usage can incur charges. This is not a billing simulator. Reports
> and alerts can lag; an alert-only budget is **not a spend ceiling**. Obtain an
> approved spend ceiling, authorised test users, a stop procedure, and a rollback
> owner before changing anything. Never exhaust an enterprise pool to make the
> demonstration work. Use comparison-only mode when safety cannot be established.

## 1. Learning outcomes and presenter story

The story: give power users visibility without blocking them at the shared
cost-centre target; give standard users a predictable inherited per-person hard
limit; explain what the enterprise default does for everyone else. Learners
should distinguish allocation, included pool consumption, paid spending,
user-level defaults, and independent overlapping controls.

| Cost centre | Cohort | Monthly budget | Behaviour |
| --- | --- | --- | --- |
| `AI-DEMO-POWER-USERS` | Enterprise team | $10–$20 USD shared | Alerts at 75%, 90%, and 100%; do not stop usage at this budget |
| `AI-DEMO-STANDARD-USERS` | Enterprise team | $2–$5 USD per user | Each eligible member inherits a hard limit; stop at the effective limit |
| Enterprise default | Everyone else, unless a more specific user budget applies | Low, approved, non-disruptive test amount | Demonstrate default selection and independent overlapping-budget precedence |

These are **whole-dollar budget settings**, not free credits, guaranteed prompt
counts, or reservations of the enterprise pool. Start with one licensed test
user per cohort. Do not put the same user in both.

### Two rules, not one

1. **Select the applicable user-level budget:** explicit individual `user`
   overrides `multi_user_cost_center`, which overrides the universal
   `multi_user_customer` default. These amounts **do not add together**; a
   superseded user default is not another active limit.
2. **Then evaluate independent applicable controls:** the selected user-level
   budget and active hard spending limits can still overlap. The applicable
   control with the least remaining headroom blocks first. Shared cost-centre,
   organisation, and enterprise spending budgets govern metered charges after
   pool exhaustion; user-level budgets govern consumption in **both** phases.

An alert-only shared budget cannot override a hard user limit or a paid-usage
policy. Power users may still inherit the enterprise user default: “do not stop”
describes their **shared cost-centre budget**, not unlimited Copilot access.
See [section 10](#10-demonstrate-overlapping-budget-precedence) for worked cases.

### Presenter track: 10–15 minutes

Prepare the approved configuration and any redacted historical evidence before
the talk. Do not include provisioning, reporting delays, or a threshold-crossing
exercise in this time estimate.

| Time | Presenter action | Audience evidence |
| --- | --- | --- |
| 0–2 min | Predict who can spend, who is capped, and where costs belong | Scenario and two-rule explanation |
| 2–5 min | Observe both teams/cost centres and open the two budget types | Membership, UUIDs, shared versus per-user settings |
| 5–8 min | Explain a dated usage view and user-filtered effective budget | Expected/observed table; included versus paid amounts |
| 8–11 min | Challenge “raising the shared budget unblocks everyone” | Compare remaining headroom; do not create an outage |
| 11–15 min | Recover: show rollback ownership and restoration evidence | Starting-state comparison and honest limitations |

### Operator lab: 45–60 minutes

| Time | Operator work | Deliverable |
| --- | --- | --- |
| 0–10 min | Safety checks and baseline capture | Approved scope, spend ceiling, collision/overlap inventory |
| 10–20 min | Create test teams and cost centres, or use direct users | Membership/UUID mapping |
| 20–30 min | Configure the two budget types; inspect the existing default | Budget IDs, flags, selected user-level budgets |
| 30–40 min | One bounded task per cohort and read-only reporting | Timestamped evidence, or explicitly pending attribution |
| 40–50 min | Explain and challenge precedence using values/evidence | Headroom comparison without deliberate exhaustion |
| 50–60 min | Stop activity, restore, and reconcile | Rollback record and acceptance status |

Reporting and email delivery may require a later follow-up outside the lab.
For a 45-minute session, shorten the walkthrough using prepared evidence, not
the safety or recovery checks.

| Learning loop | Prompt | Evidence |
| --- | --- | --- |
| Predict | Which user budget wins, and which independent control could block next? | Written expectation before changes |
| Observe | What do membership, effective-budget output, and usage actually show? | Redacted UI/API evidence with timestamps |
| Explain | Is this allocation, pool consumption, a default override, or a spending limit? | Current official source and applicable budget IDs |
| Challenge | Would raising only the shared budget help a user at their hard limit? | Counterexample using configured values, not extra spending |
| Recover | Did we restore membership and controls without claiming to undo charges? | Before/after comparison and rollback confirmation |

**Honesty notes:** this guide does not establish feature availability in the
target enterprise, guarantee prompt costs or immediate reporting, or certify
billing correctness. Earlier roadmap research is context only, not evidence of
shipping behaviour. No private repositories, customer incidents, unreleased
flags, stafftools, or internal APIs are required.

## 2. Pre-demo safety checks

Complete this before saving any UI change or running an optional mutation.

- [ ] Confirm enterprise-owner or billing-manager billing access. Team creation
  may need a separately authorised enterprise owner; billing access alone is
  not proof of team-management permission.
- [ ] Confirm the enterprise/account type, Copilot plan, billing platform, and
  visible budget types. Use only authorised, non-production-critical test
  identities with existing appropriate Copilot access.
- [ ] Capture existing enterprise teams, membership and licence sources, cost
  centres/resources, budgets, policies, included usage controls, cost-centre
  exclusions, and relevant usage/report state in approved private storage.
- [ ] Search for both demo names in active **and deleted** cost centres and in
  teams. Check stale/deleted users, duplicate resources, and existing direct
  assignments. Do not reuse a collision or move someone from a production cost
  centre just because the name looks suitable.
- [ ] Review applicable enterprise, organisation, repository, `cost_center`,
  universal `multi_user_customer`, `multi_user_cost_center`, and explicit `user`
  budgets. Record product/SKU, amount, consumed amount, hard-stop flag, alerts,
  exclusions, and any individual override expiry. Resolve the selected
  user-level budget separately from independent spending limits.
- [ ] Record the **AI credit paid usage** policy without enabling it just for
  this demo. Paid usage can be blocked by policy even when a budget has room.
  Do not change production pool controls, licences, or billing identities.
- [ ] Agree the maximum approved incremental real spend, maximum number of
  tasks, time window, alert recipients, and a safety margin for in-flight
  requests/reporting delay. A $10–$20 alert-only target cannot enforce this
  approval. If a bounded authorised run cannot be justified, use UI/read-only
  comparison with no new consumption.
- [ ] Name the operator, billing rollback owner, team/identity owner, evidence
  owner, and follow-up owner. Confirm they can restore the baseline.
- [ ] Stop on unexpected blocking, reassignment, unmapped qualifying usage,
  unsupported controls, unexplained consumption, or any risk of exceeding
  approved spend. Stop new test requests first, preserve evidence, and follow
  [recovery](#12-cleanup-and-restoration); use GitHub Support for anomalies.

Use only ordinary test-user Copilot activity. **Do not use stafftools, manual
charge generators, private/internal endpoints, or synthetic production billing
emission tools.** Do not grant broad roles, organisation membership, model
access, or extra seats as an incidental part of demonstrating cost allocation.

### Private operator worksheet

Fill this in outside the repository. Keep real identity/ID mappings private;
use stable aliases in anything shared.

| Variable/evidence | Value to record |
| --- | --- |
| Enterprise | `GB18030-Action`; confirm in the browser and API host |
| Power and standard actors | `POWER_TEST_USERNAME`, `STANDARD_TEST_USERNAME` |
| Teams | `POWER_TEAM_ID_OR_SLUG`, `STANDARD_TEAM_ID_OR_SLUG`; record actual returned values |
| Cost centres | `POWER_COST_CENTRE_UUID`, `STANDARD_COST_CENTRE_UUID` |
| Budgets | `POWER_BUDGET_ID`, `STANDARD_BUDGET_ID`, `DEFAULT_BUDGET_ID`; optional explicit-user budget ID |
| Time range | `YYYY-MM-DD`, start/end time and timezone; report month/year |
| Spend/activity approval | `MAX_APPROVED_USD`, task count, deadline, stop margin, approver role |
| Recipients and owners | `ALERT_RECIPIENT_LOGIN`, operator/rollback/identity/evidence owner aliases |
| Evidence | Approved private location; baseline, after-change, and restored captures |

Do not store secrets, tokens, real user names, customer data, private usage
records, or Azure subscription IDs in this repository. Avoid recording
sensitive prompt content. Screenshots need review too.

## 3. Create two enterprise teams or test cohorts

**UI changes — authorised operator only.** See
[Creating enterprise teams](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/create-enterprise-teams).

1. Open the target enterprise. Select **People** → **Enterprise teams**.
2. Check name collisions, then select **Create Enterprise team**. Create a
   demo-only power cohort and a demo-only standard cohort; record each actual
   team ID/slug. The cost-centre names in the scenario can also identify the
   teams if those names are unused.
3. Leave organisation access, enterprise roles, ruleset bypass, new licence
   assignments, and model access unchanged. Assigning organisation access can
   add members directly, broaden permissions, and consume licences.
4. Open each team, select **Add members**, search for its authorised test
   username, select it, and click **Add**. Verify one intended member per team
   and no unexpected privileges.
5. Record membership and licence-source evidence before assigning the team to
   a cost centre.

An enterprise team assigned to a cost centre keeps membership current as
people join or leave the team. That does **not** prove the billing UI/report
will refresh synchronously. Avoid cross-team overlap: current allocation docs
say that, for teams assigned to different cost centres, the **team created
first** determines the user's team-derived allocation. A direct assignment to
another cost centre takes precedence.

**Availability/fallback:** enterprise teams and IdP synchronisation are not the
same feature. Current docs describe enterprise teams for personal-account and
Enterprise Managed Users enterprises, but enterprise-team IdP sync is an EMU
capability; personal-account team sync is for organisation teams. Verify the
actual enterprise type, policy, and UI. If enterprise teams or the assignment
picker are unavailable, keep two authorised direct-user cohorts and add those
users in section 4. Label that route **direct-user fallback**: it does not
demonstrate automatic team membership synchronisation. Do not substitute an
organisation team, change IdP groups, or guess an enterprise-team REST endpoint.

## 4. Create the two cost centres

**UI changes — authorised operator only.**

1. At the enterprise, open **Billing and licensing** → **Cost centers**
   (cost centres in prose; preserve the UI's spelling).
2. Select **New cost center**, enter `AI-DEMO-POWER-USERS`, and under
   **Resources** select only the power enterprise team. For the fallback,
   select only `POWER_TEST_USERNAME` directly.
3. Leave Azure billing identity/subscription and included usage controls
   unchanged. A cost-centre pool cap is a different control, not the $10–$20
   spending budget.
4. Select **Create cost center**. Open its details and record the actual UUID
   from the UI URL/details or the read-only API lookup in section 11.
5. Repeat for `AI-DEMO-STANDARD-USERS` and its team/direct test user.
6. Confirm name, UUID, active state, resources, resolved members, and no
   unintended reassignment before creating budgets.

Direct user assignment takes precedence over indirect organisation-derived
assignment for licensed-product allocation. Team-derived allocation also
requires checking existing direct assignments and other teams. A user-based
cost centre is **not** a product-isolation mechanism: assigning a user can
affect other licensed-product allocation, not only AI Credits.

Future qualifying usage should begin attributing to the new cost centre.
Historical usage is not retroactively reassigned by creating or editing it.
See [Cost centre allocation](https://docs.github.com/en/enterprise-cloud@latest/billing/reference/cost-center-allocation).

### Optional mutation: create a cost centre and add a direct user

> [!WARNING]
> These POST requests change real enterprise billing allocation. Prefer the
> UI. Revalidate the [current cost-centre REST docs](https://docs.github.com/en/enterprise-cloud@latest/rest/billing/cost-centers?apiVersion=2026-03-10),
> complete section 2, and initialise the variables in section 11 first.
> Execute individual requests only after review; do not run the entire guide.
> Do not create duplicates of cost centres already created in the UI.

PowerShell 7 examples using documented endpoints:

```powershell
$CostCentreName = 'AI-DEMO-POWER-USERS'
gh api --hostname github.com --method POST @ApiHeaders `
  "$BillingBase/cost-centers" -f "name=$CostCentreName"
if ($LASTEXITCODE -ne 0) { throw 'Cost-centre creation failed; stop and inspect.' }
```

Capture the returned `id` in `$POWER_CC_ID`. Repeat the individually reviewed
creation request with `AI-DEMO-STANDARD-USERS` and capture `$STANDARD_CC_ID`.
Use the following request **only for the direct-user fallback**:

```powershell
gh api --hostname github.com --method POST @ApiHeaders `
  "$BillingBase/cost-centers/$POWER_CC_ID/resource" -f "users[]=$POWER_USER"
if ($LASTEXITCODE -ne 0) { throw 'Resource assignment failed; stop and inspect.' }
```

For standard users, substitute `$STANDARD_CC_ID` and `$STANDARD_USER`.
Inspect `reassigned_resources` even on a successful response. Any unexpected
previous cost centre is a stop/recovery condition, not a successful demo.
Do not combine team and direct assignments to make an unexplained result pass.

## 5. Create the power users' shared Bundled AI credits budget

**UI changes — authorised operator only.**

1. Open **Billing and licensing** → **Budgets and alerts** → **New budget**.
2. Under **Budget Type**, select **Bundled AI credits budget**. If shown,
   choose **Next: Configure budget**.
3. Under **Budget scope**, select **Cost center**, then
   `AI-DEMO-POWER-USERS`. Do **not** choose **Users**.
4. Set the approved amount between **$10 and $20 USD**.
5. Leave **Stop usage when budget limit is reached** **disabled**.
6. Enable **Receive budget threshold alerts** for the documented **75%, 90%,
   and 100%** thresholds. Under **Alert Recipients**, select the approved
   recipients; confirm expected account-owner/billing-manager notifications.
7. Create the budget, capture its ID, and reopen it to confirm every setting.

This is one **shared cost-centre metered-spending target**, not $10–$20 for
each user and not a cap on included-pool use. For this intentionally alert-only
demonstration, charges may continue beyond the target. The separately approved
activity limit and operator stop procedure remain essential.

### Optional mutation: shared budget REST example

> [!WARNING]
> POSTing this body creates a real alert-only budget, not a hard spending cap.
> Validate the [current budget request schema](https://docs.github.com/en/enterprise-cloud@latest/rest/billing/budgets?apiVersion=2026-03-10)
> and target UI before execution. Replace placeholders privately, use an
> approved whole-dollar amount, and do not duplicate a UI-created budget.

For `POST /enterprises/{enterprise}/settings/billing/budgets`:

```json
{
  "budget_amount": 10,
  "prevent_further_usage": false,
  "budget_scope": "cost_center",
  "budget_entity_name": "POWER_COST_CENTRE_UUID",
  "budget_type": "BundlePricing",
  "budget_product_sku": "ai_credits",
  "budget_alerting": {
    "will_alert": true,
    "alert_recipients": ["ALERT_RECIPIENT_LOGIN"]
  }
}
```

`budget_entity_name` is the **cost-centre UUID**, not its display name.
Recipients are GitHub login names, not email addresses. The documented
thresholds come from enabling alerts; do not invent a threshold-array field.
If using `gh api`, place the reviewed JSON in an approved private file:

```powershell
$PowerBodyPath = 'C:\APPROVED-PRIVATE-STORAGE\power-budget.json'
gh api --hostname github.com --method POST @ApiHeaders `
  "$BillingBase/budgets" --input "$PowerBodyPath"
if ($LASTEXITCODE -ne 0) { throw 'Budget creation failed; stop and inspect.' }
```

Record the returned budget ID and verify it with a GET. Do not assume a
particular response envelope without inspecting it.

## 6. Create the standard users' inherited per-user budget

**UI changes — authorised operator only.**

1. Open **Budgets and alerts** → **New budget** →
   **Bundled AI credits budget**.
2. Choose **Users** under **Budget scope**, then select the cost centre
   `AI-DEMO-STANDARD-USERS` rather than a specific user. Labels/layout can
   vary; confirm that the result means **one per-user amount for every member**.
3. Set **$2–$5 USD per user**, within the approved test plan.
4. Ensure hard-stop behaviour. Current docs say user-level budgets **always**
   enforce a hard stop and do not offer the stop-usage switch. If the UI exposes
   **Stop usage when budget limit is reached**, enable it and verify that the
   saved scope is still the per-user cost-centre scope, not the shared scope.
5. Enable threshold alerts and approved recipients **if available**. Record
   unavailable alert controls rather than claiming notifications are configured.
6. Save, capture the ID, and inspect the inherited/effective budget for the
   standard test user. Do not proceed to consumption if this is unexplained.

Every eligible current/future member inherits the same **per-person** limit.
Two users at $2 each do not share a $2 allowance. This control covers included
and paid consumption. An explicit individual user budget can also be configured;
it **overrides** this inherited default, while independent spending limits
remain applicable. Existing cycle consumption may already leave little or no
headroom; do not assume a newly created budget starts its user's usage at zero.

### Optional mutation: per-user cost-centre REST body

> [!WARNING]
> This body can impose a real hard stop on every eligible member of the cost
> centre. Validate it against the current REST docs **and** the visible UI:
> API/UI capabilities and alert support may roll out independently. If the
> inherited scope is missing or rejected, stop; do not silently replace it
> with a shared budget, thousands of individual budgets, or an internal API.

For the same documented budget-creation endpoint, a candidate body is:

```json
{
  "budget_amount": 2,
  "prevent_further_usage": true,
  "budget_scope": "multi_user_cost_center",
  "budget_entity_name": "STANDARD_COST_CENTRE_UUID",
  "budget_type": "BundlePricing",
  "budget_product_sku": "ai_credits",
  "budget_alerting": {
    "will_alert": true,
    "alert_recipients": ["ALERT_RECIPIENT_LOGIN"]
  }
}
```

Only request alerts if supported for this scope in the current enterprise. If
the documented supported alternative is `will_alert: false` with an empty
recipient array, record that limitation explicitly. Do not weaken
`prevent_further_usage` to get a request accepted. Use the UI for this step if
anything about the schema or effective result is uncertain.

## 7. Inspect or configure a low enterprise default

Prefer **read-only inspection of an existing approved test default**.
`multi_user_customer` is a universal **per-user** bundled AI Credit budget,
not the shared enterprise `enterprise` spending budget.

1. In **Budgets and alerts**, locate the universal user budget and inspect its
   amount, consumed/effective states, product, alerts, and hard-stop behaviour.
2. Only in an isolated, explicitly authorised test setting, create one with
   **New budget** → **Bundled AI credits budget** → **Users**, leaving the
   individual-user and cost-centre selectors empty. Choose a low, positive,
   non-disruptive approved amount. A $0 user budget blocks immediately.
3. Confirm the saved scope is `multi_user_customer` and record its ID.
4. Explain: everyone with an eligible licence uses this default **unless** an
   individual or cost-centre user-level budget overrides it. It is not literally
   a selector excluding the two demo cohorts.

**Never lower, replace, or create a production-wide default merely for this
demonstration.** GB18030-Action's name does not establish isolation. When no
safe test default exists, show the concept with the illustrative values in
section 10 and mark enterprise-default live evidence **not exercised**.

Power users without a more specific user-level budget still inherit this hard
default, despite their shared alert-only budget. Inspect their headroom before
any task. Do not promise unlimited access or raise their default to force the
story. An individually approved test-user override can be discussed or inspected
in section 10; it is not a mandatory mutation.

## 8. Generate controlled AI Credit usage

Skip this section in comparison-only mode. Do not use the budget amount as a
target to spend.

1. Confirm both cohorts' membership, effective user budgets, paid-usage policy,
   applicable hard limits, existing cycle consumption, and approved activity
   window. Use test users with sufficient **verified** headroom.
2. In a disposable repository containing only synthetic/non-sensitive material,
   ask the power test user for **one** small normal Copilot task: explain a tiny
   function, generate a few tests for a pure helper, or review a small diff.
3. Stop the interaction after that bounded result. Do not enable autonomous
   loops, batch jobs, repeated retries, or background agents.
4. Repeat once with the standard test user. Do not deliberately reach either
   hard limit or shared alert threshold.
5. Record the activity below, then inspect usage. If reports lag, stop generating
   requests and schedule the approved follow-up; do not keep spending to make
   data appear.

| Actor alias | Expected cost centre | Model/surface | Start/end + timezone | Purpose | Evidence location/status |
| --- | --- | --- | --- | --- | --- |
| `POWER_TEST_USER` | `AI-DEMO-POWER-USERS` | `MODEL_AND_SURFACE` | `START` / `END` | One small explanation | `PRIVATE_EVIDENCE_REFERENCE` |
| `STANDARD_TEST_USER` | `AI-DEMO-STANDARD-USERS` | `MODEL_AND_SURFACE` | `START` / `END` | One tiny test-generation task | `PRIVATE_EVIDENCE_REFERENCE` |

Included usage, paid usage, the Copilot plan, model choice, surface, caching,
and reporting lag can affect the result. A served request need not add paid
spend to the shared budget. Do not promise an exact number of credits per
prompt or derive token-to-credit conversions from this exercise. A successful
small task does not prove hard-limit enforcement.

Stop before any unapproved charge or operational impact. If that cannot be
assured with current visibility, do not begin live usage.

## 9. View attribution and budget details

1. Open **Billing and licensing** → **Usage**. Select the recorded date/month,
   then group or filter by **Cost center** where available.
2. Inspect each demo cost centre. Keep the time range, timezone, product/SKU,
   and creation/membership timestamps with the evidence. For detailed exports,
   inspect `cost_center_name`; for supported summary/AI usage APIs, inspect
   `costCenter.id` and `costCenter.name`.
3. Open **Budgets and alerts**, find each captured budget ID, and inspect its
   amount, usage/`consumed_amount`, scope, members, status, alert settings, and
   effective-user-budget view where available. Do not treat absent fields as
   zero or a missing user row as proof of no licence.
4. Reconcile against the chosen user budget and independent hard controls.
   Universal per-user records can appear only after the user consumes credits
   in that cycle; licence inventory is a separate source.
5. Save redacted evidence using section 11 or UI-only screenshots/exports.

New cost centres should capture **future qualifying usage**. Historical usage
may remain assigned to its original cost centre or the enterprise. Reporting
delay is not proof of lost attribution, and an empty report is not success.
Unassigned usage may appear as **Enterprise Only** in the UI.

| Cohort/check | Expected evidence | Observed evidence | Outcome |
| --- | --- | --- | --- |
| Power membership | Correct team/direct user, active cost-centre UUID, no conflicting direct assignment | `CAPTURE_REFERENCE` | `PASS / FAIL / PENDING` |
| Power shared budget | `cost_center`, $10–$20, alerts on, stop off; selected user limit separately identified | `BUDGET_ID_AND_CAPTURE` | `PASS / FAIL / PENDING` |
| Standard membership/budget | Correct member; `multi_user_cost_center`, $2–$5 per user, hard stop; inherited ID effective unless explicit override | `BUDGET_ID_AND_CAPTURE` | `PASS / FAIL / PENDING` |
| Enterprise default | `multi_user_customer`; selected for users without more specific user budgets | `LIVE_OR_COMPARISON_EVIDENCE` | `PASS / NOT_EXERCISED / PENDING` |
| Future attribution | Each test actor's qualifying post-assignment usage under the expected cost centre | `TIME_RANGE_AND_REPORT` | `PASS / FAIL / PENDING` |
| Alerts | Saved 75%/90%/100% configuration; delivery evidenced only if actually observed | `REDACTED_MESSAGE_OR_NOT_TRIGGERED` | `OBSERVED / NOT_TRIGGERED / UNSUPPORTED` |
| Recovery | Starting configuration restored, demo resources detached/archived as approved | `ROLLBACK_REFERENCE` | `PASS / FAIL / PENDING` |

## 10. Demonstrate overlapping-budget precedence

Use configured values, dated evidence, and optional `user`-filtered effective
budget output. **Do not intentionally block production work.**

First select the user-level budget by specificity. Then compare remaining
headroom against independent **active hard** controls. Budgets overlap rather
than add together: raising one neither increases nor replenishes another.
An alert-only budget does not block at its target. Pool-phase and metered-phase
counters measure different things; do not sum them or subtract one from another.

The following numbers are illustrative, **not a request to change production**.
Where consumed values are available, headroom means the applicable amount less
its own consumed amount in the same billing cycle.

| Case | Compare | Expected explanation |
| --- | --- | --- |
| Enterprise default only | Universal user limit $1; that user's consumption $0.20 | Selected ULB has $0.80 remaining; not a shared $1 enterprise allowance |
| Default + power shared budget | Universal ULB has $0.80 remaining; power shared alert-only target $10 | The shared target does not override the ULB or create $10.80 of allowance |
| Default + standard per-user budget | Universal $1; standard `multi_user_cost_center` $2; user has consumed $0.50 | Cost-centre ULB overrides universal: selected ULB headroom is $1.50, not the minimum of both defaults and not $2.50 |
| Add shared cost-centre hard budget | Selected standard ULB has $1.50 remaining; a separately approved, already-existing shared hard budget has $0.40 remaining | In the metered phase the applicable hard budget can block after $0.40; do not create an extra hard budget just for the talk |
| Add explicit individual override | Standard inherited limit $2; explicit `user` limit $5; user has consumed $0.50 | Individual ULB wins with $4.50 remaining, but cannot override applicable shared/enterprise hard limits |
| Lower explicit override | Standard inherited limit $2; explicit `user` limit $1 already exhausted | User is blocked even if the cost centre has spare paid budget; raising only the shared budget does not help |
| Enterprise spending limit | Applicable enterprise hard spending budget has $0.25 left; selected ULB has $1.50 left | In the metered phase, the applicable enterprise control can block first; inspect cost-centre exclusion rather than assuming coverage |

Current docs distinguish an enterprise spending budget from the universal
user-level default. They also describe **cost centre exclusion**, which can
remove a cost centre's metered usage from the enterprise spending budget.
Inspect existing exclusions; do not enable one to bypass a demo failure.
Record relevant included-usage caps as a separate control too.

**Different team-wide amounts inside one cost centre require separate cost
centres today.** The inherited amount is one value per member of that cost
centre, not a different tier for each team. Explicit individual overrides are
documented exceptions, not team-tier budgets. This is why the demo uses two
cost centres.

If showing an already-approved individual override, identify its ID and any
expiry; after expiry/removal the user falls back to the inherited/default ULB.
Do not create an override solely to bypass an unexplained hard stop.

### Documentation boundaries to explain

The general scale tutorial says “most restrictive” across overlapping budgets;
the Copilot-specific guide explicitly says **most specific user-level budget
wins**. These describe different stages. The Copilot guide's simplified metered
routing sequence must also be read with its independent-headroom and
cost-centre-exclusion sections. Effective-budget output is useful evidence of
the selected ULB, **not proof that every policy and aggregate hard limit allows
a request**. If actual behaviour differs, stop and preserve evidence for Support.

The REST request documentation supports `BundlePricing`/`ai_credits` and
`multi_user_cost_center`, but some response-schema enum lists still omit
`BundlePricing`. Record the returned fields; do not switch to `SkuPricing` or
legacy premium requests merely to match an incomplete response schema.

## 11. Export and API validation

**Read-only by default.** All API requests in this section explicitly use GET.
They do not change budgets, teams, policies, or billing allocation. Local
evidence writes are optional. Run in a private, non-recorded terminal, not an
agent session that uploads raw outputs. UI-only execution remains sufficient.

Examples use **PowerShell 7** and GitHub CLI; no extra module is required.
Recheck [gh api](https://cli.github.com/manual/gh_api), the
[billing usage reference](https://docs.github.com/en/enterprise-cloud@latest/rest/billing/usage?apiVersion=2026-03-10),
and endpoint-specific token/role requirements before execution. Tutorials may
still show `2022-11-28`; these examples select **2026-03-10** deliberately.
The reporting tutorial documents classic PATs or an enterprise-installed
GitHub App with enterprise billing read permission, not fine-grained PATs for
usage reporting. A valid CLI login alone does not establish billing access.

### Initialise variables and verify authentication

Replace every uppercase placeholder privately. Record `gh --version` and
`$PSVersionTable.PSVersion` in the operator evidence.

```powershell
$ErrorActionPreference = 'Stop'
$ENTERPRISE = 'GB18030-Action'
$API_VERSION = '2026-03-10'
$POWER_USER = 'POWER_TEST_USERNAME'
$STANDARD_USER = 'STANDARD_TEST_USERNAME'
$POWER_CC_ID = 'POWER_COST_CENTRE_UUID'
$STANDARD_CC_ID = 'STANDARD_COST_CENTRE_UUID'
$POWER_BUDGET_ID = 'POWER_BUDGET_ID'
$STANDARD_BUDGET_ID = 'STANDARD_BUDGET_ID'
$DEFAULT_BUDGET_ID = 'DEFAULT_BUDGET_ID'
$YEAR = 'YYYY'
$MONTH = 'MM'
$EVIDENCE_DIR = 'C:\APPROVED-PRIVATE-STORAGE\demo-15'
$BillingBase = "enterprises/$ENTERPRISE/settings/billing"
$ApiHeaders = @('-H', 'Accept: application/vnd.github+json',
  '-H', "X-GitHub-Api-Version: $API_VERSION")

gh auth status --active --hostname github.com
if ($LASTEXITCODE -ne 0) { throw 'Authentication failed; stop before any API calls.' }
```

Use the existing approved credential store, or an approved process that injects
`GH_TOKEN` through a secret manager/environment without displaying it. Never use
`gh auth token`, `--show-token`, HTTP debug logging, token literals, or a command
that prints environment variables. `gh auth status` can reveal account names:
do not put its raw output into a public recording.

### List cost centres and inspect resources

```powershell
$raw = gh api --hostname github.com --method GET @ApiHeaders "$BillingBase/cost-centers"
if ($LASTEXITCODE -ne 0) { throw 'Cost-centre listing failed; preserve the error privately.' }
$costCentreInventory = $raw | ConvertFrom-Json
$demoCentres = @($costCentreInventory.costCenters | Where-Object {
  $_.name -in @('AI-DEMO-POWER-USERS', 'AI-DEMO-STANDARD-USERS')
})
$demoCentres | Select-Object id, name, state

$raw = gh api --hostname github.com --method GET @ApiHeaders `
  "$BillingBase/cost-centers" -f state=deleted
if ($LASTEXITCODE -ne 0) { throw 'Deleted cost-centre lookup failed.' }
$deletedCostCentres = $raw | ConvertFrom-Json
```

Use the unfiltered inventory and deleted view for collision checks. After
creation, confirm **exactly one active** result per demo name and record each
actual UUID; a missing/duplicate row is not acceptable. Do not save the entire
enterprise inventory to shared evidence. It can contain Azure subscription
identifiers and unrelated resources.

For each captured UUID, inspect resource pages privately:

```powershell
$COST_CENTRE_ID = $POWER_CC_ID
$PAGE = 1
$raw = gh api --hostname github.com --method GET @ApiHeaders `
  "$BillingBase/cost-centers/$COST_CENTRE_ID" -F "page=$PAGE" -F per_page=100
if ($LASTEXITCODE -ne 0) { throw 'Cost-centre resource lookup failed.' }
$costCentrePage = $raw | ConvertFrom-Json
```

Inspect `id`, `name`, `state`, `resources`, and `has_next_page`. Increment
`$PAGE` and repeat while `has_next_page` is true, retaining the pages in private
memory/evidence. Repeat for `$STANDARD_CC_ID`. Do not call the first page a
complete membership inventory. If pagination fields are absent or inconsistent,
use the current docs/UI rather than guessing. A team resource row is not an
expanded member list: reconcile it with the enterprise-team UI and resolved
cost-centre member view.

### Get all budgets, including pagination

Use this once for the overlap inventory. This bounded loop follows the
documented `has_next_page` response flag, rather than assuming `gh --paginate`
will follow body-only pagination. It stops visibly if completeness cannot be
established within 100 pages.

```powershell
$budgetPages = [System.Collections.Generic.List[object]]::new()
for ($page = 1; $page -le 100; $page++) {
  $raw = gh api --hostname github.com --method GET @ApiHeaders `
    "$BillingBase/budgets" -F "page=$page" -F per_page=100
  if ($LASTEXITCODE -ne 0) { throw "Budget page $page failed; inventory is incomplete." }
  $result = $raw | ConvertFrom-Json
  if ($null -eq $result.budgets -or $result.has_next_page -isnot [bool]) {
    throw 'Unexpected budget pagination schema; stop and use the current docs/UI.'
  }
  $budgetPages.Add($result)
  if (-not $result.has_next_page) { break }
  if ($page -eq 100) { throw 'Budget page limit reached; inventory is incomplete.' }
}
$allBudgets = @($budgetPages | ForEach-Object { $_.budgets })
```

Check returned `total_count` when present and investigate duplicate IDs or
concurrent changes. Keep unrelated budgets private; capture only relevant
controls in the redacted overlap worksheet.

The following are **optional narrower inspection alternatives**. They show the
documented scope filters; repeat pages as above if `has_next_page` is true:

```powershell
$raw = gh api --hostname github.com --method GET @ApiHeaders `
  "$BillingBase/budgets" -f scope=cost_center -F page=1 -F per_page=100
if ($LASTEXITCODE -ne 0) { throw 'Shared cost-centre budget lookup failed.' }
$sharedBudgetPage = $raw | ConvertFrom-Json

$raw = gh api --hostname github.com --method GET @ApiHeaders `
  "$BillingBase/budgets" -f scope=multi_user_cost_center -F page=1 -F per_page=100
if ($LASTEXITCODE -ne 0) { throw 'Cost-centre per-user budget lookup failed.' }
$inheritedBudgetPage = $raw | ConvertFrom-Json
```

A scope filter selects **all cost centres of that scope**, not just the demo.
Match the returned `budget_entity_name` to the captured UUID locally.

### Inspect a budget and optional user-specific effective details

```powershell
$BUDGET_ID = $STANDARD_BUDGET_ID
$raw = gh api --hostname github.com --method GET @ApiHeaders "$BillingBase/budgets/$BUDGET_ID"
if ($LASTEXITCODE -ne 0) { throw 'Budget detail lookup failed.' }
$budgetDetail = $raw | ConvertFrom-Json

$raw = gh api --hostname github.com --method GET @ApiHeaders `
  "$BillingBase/budgets" -f "user=$STANDARD_USER" -F page=1 -F per_page=100
if ($LASTEXITCODE -ne 0) { throw 'User-filtered budget lookup failed.' }
$userBudgetPage = $raw | ConvertFrom-Json
```

Repeat the ID lookup for power/default budgets that actually exist. Optionally
repeat the user-filtered list for `$POWER_USER`. The `user` query parameter is
documented on **Get all budgets**, not on **Get a budget by ID**. It filters
consumed-amount details; do not assume it removes unrelated budgets. Handle
pagination as above and inspect `effective_budget` only **when returned**.
Record `effective_budget.id`, `budget_amount`, and `consumed_amount`; absence
means unverified, not unlimited or zero. An explicit `user` override can explain
why the inherited budget is not selected.

### Query a specific month and cost centre

```powershell
$COST_CENTRE_ID = $POWER_CC_ID
$raw = gh api --hostname github.com --method GET @ApiHeaders `
  "$BillingBase/usage/summary" -f "year=$YEAR" -f "month=$MONTH" `
  -f "cost_center_id=$COST_CENTRE_ID"
if ($LASTEXITCODE -ne 0) { throw 'Monthly cost-centre usage lookup failed.' }
$usageSummary = $raw | ConvertFrom-Json

$raw = gh api --hostname github.com --method GET @ApiHeaders `
  "$BillingBase/ai_credit/usage" -f "year=$YEAR" -f "month=$MONTH" `
  -f "cost_center_id=$COST_CENTRE_ID" -f "user=$POWER_USER"
if ($LASTEXITCODE -ne 0) { throw 'AI Credit usage lookup failed.' }
$aiUsage = $raw | ConvertFrom-Json
```

Repeat with `$STANDARD_CC_ID` and `$STANDARD_USER`. Verify the latest API
version, supported parameters, and returned time period before execution.
The usage tutorial's statement that cost-centre filtering is summary-only is
narrower than the current REST reference, which documents it for AI Credit
usage too; the optional second call follows the **2026-03-10 REST reference**.
If unsupported in the target, use the UI/detailed usage report and mark the
API check unavailable.

The older `/usage` endpoint defaults to usage **without** a cost centre; it is
not interchangeable with `/usage/summary`, whose default covers all cost
centres. For this demo always supply `cost_center_id`. Check returned
`costCenter.id`/`name`, not just the request URL.

Inspect `grossQuantity`, `discountQuantity`, `netQuantity`, `grossAmount`,
`discountAmount`, `netAmount`, `unitType`, product, SKU, and model **when
returned**. Included consumption can have zero net billed amount. Do not
relabel gross consumption as incremental spend or general summary totals as
AI-only usage. UI/export attribution may use `cost_center_name` instead.

### Save redacted evidence locally

Retain baseline, changed, and restored captures separately. Raw responses stay
in approved private storage/memory; never pipe them into an issue, public gist,
chat prompt, or this repository. Build an **allowlisted** evidence object after
review rather than treating `ConvertTo-Json` as automatic redaction:

```powershell
$redactedEvidence = [ordered]@{
  feature_validation_date = '2026-09-14'
  api_version = $API_VERSION
  capture_time = 'YYYY-MM-DDTHH:MM:SS+TIMEZONE'
  cohort = 'STANDARD_TEST_USER'
  cost_centre = [ordered]@{
    name = 'AI-DEMO-STANDARD-USERS'
    id = 'STANDARD_COST_CENTRE_UUID'
    membership_evidence = 'REDACTED_CAPTURE_REFERENCE'
  }
  budget = [ordered]@{
    id = 'STANDARD_BUDGET_ID'
    budget_type = 'REPLACE_WITH_OBSERVED_VALUE'
    budget_scope = 'REPLACE_WITH_OBSERVED_VALUE'
    budget_amount = 'REPLACE_WITH_OBSERVED_VALUE'
    prevent_further_usage = 'REPLACE_WITH_OBSERVED_VALUE'
    budget_alerting = 'REDACTED_OBSERVED_SETTINGS'
    consumed_amount = 'OBSERVED_VALUE_OR_NOT_RETURNED'
    effective_budget = 'REDACTED_OBSERVED_FIELDS_OR_NOT_RETURNED'
  }
  usage_evidence = 'REDACTED_CAPTURE_REFERENCE_OR_PENDING'
  rollback_evidence = 'REDACTED_CAPTURE_REFERENCE_OR_PENDING'
}
if (-not (Test-Path -LiteralPath $EVIDENCE_DIR -PathType Container)) {
  throw 'Prepare an approved private evidence directory outside the repository.'
}
$EvidencePath = Join-Path $EVIDENCE_DIR 'standard-after.redacted.json'
if (Test-Path -LiteralPath $EvidencePath) { throw 'Preserve the existing evidence; choose a new filename.' }
$redactedEvidence | ConvertTo-Json -Depth 8 |
  Set-Content -LiteralPath $EvidencePath -Encoding utf8
```

This is a **template**, not collected evidence. Replace placeholders with
reviewed observations before saving; preserve numeric/boolean types where
returned. Store actual UUIDs/budget IDs and alias mappings in the access-controlled
operator pack; substitute placeholders in any public derivative. Remove
identities, alert-recipient logins/emails, Azure subscription IDs, unrelated
resources, private usage records, and sensitive screenshot/URL metadata.
Redacted API response copies should retain relevant field names and observed
values; label omissions, missing fields, and pending observations explicitly.

## 12. Cleanup and restoration

**UI changes — authorised rollback owner only.** Recovery restores controls,
not a pre-demo invoice. Consumption already incurred cannot be rolled back;
archived records and audit history can legitimately remain.

- [ ] **Stop all demo activity first**, including any in-flight interaction.
  Capture final budget IDs, consumption, alert state, and timestamps.
- [ ] Disable demo budgets only if a documented supported control exists;
  otherwise delete **only the recorded demo-created budgets** via
  **Budgets and alerts** → budget actions → **Delete**. Restore edited
  pre-existing test budgets instead of deleting them. Budgets come before
  resource removal so orphaned demo controls do not remain.
- [ ] Deleting a hard budget can remove spending protection. Confirm the
  restored baseline/fallback and keep test activity stopped throughout.
  Remove or restore any approved explicit test-user override as recorded.
- [ ] Remove the test teams/direct users from the two demo cost centres.
  Restore any intentionally changed pre-existing test assignment exactly;
  do not guess what the enterprise fallback should be.
- [ ] Archive/delete only demo-created cost centres after verifying no
  production resource, required billing identity, or dependent control is
  attached. The documented DELETE operation **archives** the cost centre;
  it can remain visible under **Deleted**.
- [ ] Remove test members from demo teams, then delete only teams created
  for this demo. For a pre-existing approved test team, restore its baseline
  membership instead. Do not remove accounts from the enterprise, revoke
  unrelated licences, or edit production IdP groups.
- [ ] Restore any intentionally changed isolated test enterprise default,
  including amount, flags, and recipients. If you created a test default
  where none existed, remove only that recorded default after reviewing the
  original fallback. Never “restore” a production default that was not changed.
- [ ] Rerun the section 11 read-only checks and compare membership, active/
  deleted state, budgets, policies, and test-user effective controls against
  the baseline. Record an audit-log reference where available, or a timestamped
  operator evidence note if the action is not exposed in the audit log.
- [ ] Assign follow-up for delayed usage/alerts, record final incremental
  spend when available, and securely retain/dispose of evidence under policy.

Deletion/removal does **not** retroactively change historical billing
attribution. Do not delete required historical evidence or retry an archive
operation because a deleted cost centre is still visible.

| Action | Owner | Trigger | Verification |
| --- | --- | --- | --- |
| Stop new test requests | `OPERATOR` | Planned end, unknown headroom, anomaly, or impact risk | Users confirm no ongoing demo activity; timestamp recorded |
| Restore/remove demo budgets and overrides | `BILLING_ROLLBACK_OWNER` | End of lab or unexpected effective limit | Recorded IDs reconciled; baseline hard controls restored |
| Detach/restore cost-centre resources | `BILLING_ROLLBACK_OWNER` | Budgets reconciled; activity stopped | Exact before/after resource and effective-membership comparison |
| Archive demo-only cost centres | `BILLING_ROLLBACK_OWNER` | No required identity/resource/control attached | Correct UUIDs archived; historical records retained |
| Restore/delete demo-only teams | `IDENTITY_OWNER` | Cost-centre attachments removed | Baseline membership, roles, licences, and access unchanged |
| Restore isolated test default | `BILLING_ROLLBACK_OWNER` | A recorded intentional default change | Original amount, scope, flags, recipients, and effective result |
| Reconcile and escalate | `EVIDENCE_OWNER` | Delayed reporting or unresolved inconsistency | Redacted case evidence, Support reference, explicit pending status |

## 13. Troubleshooting and known risks

For unexplained results: **stop new usage, preserve evidence, revert only the
demo changes, and use GitHub Support**. Do not attempt undocumented remediation,
delete unrelated resources, change feature flags, or bypass controls.

| Symptom/risk | Safe investigation | Stop/recovery boundary |
| --- | --- | --- |
| Reporting delay or empty data | Check creation/activity timestamps, time range, pool versus paid counters; arrange a later read-only check | Do not generate more usage to force a row; mark attribution pending |
| Unexpected blocking | Select the effective ULB first, then inspect applicable hard budgets, paid-usage policy, pool cap, and exclusion | Do not raise production limits; stop and restore demo changes |
| Direct versus indirect membership | Check direct assignment, enterprise teams, team creation order, and licence-granting organisation | Do not move users between centres until the prior allocation is understood |
| Stale/deleted/duplicate resources | Compare active/deleted views and resource pages with the captured baseline | Preserve IDs; use Support rather than bulk deletion or guessed repair APIs |
| API/UI rollout differences | Capture exact status/error and visible controls; compare current request docs | Prefer UI; no undocumented endpoint, scope substitution, or silent retry |
| Enterprise-team support differences | Confirm account type, permissions, IdP mode, and team/resource pickers | Use labelled direct-user fallback; do not alter enterprise identity configuration |
| Cost-centre ULB not effective | Inspect explicit `user` override/expiry, actual cost-centre allocation, current cycle consumption, and lazy user-state visibility | Do not call a shared budget equivalent; stop and escalate if unexplained |
| Qualifying usage appears unmapped / Enterprise Only | Check actor, licence source, assignment time, team propagation, and `costCenter` / `cost_center_name` | Do not re-emit charges or promise historical reallocation; keep timestamps for Support |
| Hard-limit test threatens developer work | Confirm account isolation and all affected members before any change | No deliberate live exhaustion; recover via the authorised baseline |
| No alert delivered | Verify saved settings, recipients, actual threshold crossing, and delivery delay; user-scope support differs | Do not spend to trigger email or claim configured means delivered |
| 401/403/404/422 or incomplete pagination | Record status, endpoint, API version, and non-sensitive request metadata privately; check role/token type and docs | Do not print tokens or auto-broaden permissions; UI fallback or Support |

When an anomaly persists, acceptance is **blocked**, not passed with a warning.
Support evidence must be redacted and shared through an approved private route,
never a public issue containing enterprise billing data.

## 14. Evidence pack and acceptance criteria

Keep one **redacted, access-controlled operator pack**, outside the repository:

- Before/after/restored screenshots, capture timestamps, API version and actual
  CLI/browser/surface versions, and source-review date.
- Cost-centre UUIDs and budget IDs, with a separate private alias mapping.
- Redacted API responses/exports retaining the relevant configuration,
  `consumed_amount`, effective-budget fields, and attribution evidence.
- Test-user cohort mapping, team IDs/slugs, membership/licence-source evidence,
  and the bounded activity ledger without sensitive prompt content.
- Completed expected/observed table, precedence explanation, and the approved
  spend/activity limit versus final observed incremental spend.
- Alert delivery evidence with identities redacted **if delivered**. Otherwise
  record `not triggered`, `unsupported`, or `pending`, with a follow-up owner.
- Rollback confirmation, starting-state comparison, audit-log/evidence note,
  remaining historical charges/records, and unresolved Support references.

| Acceptance criterion | Required observation |
| --- | --- |
| Correct resources | Exactly the intended test team/direct users in each active cost centre; no unintended reassignment/access change |
| Power shared alert-only budget | Correct UUID, `BundlePricing`, `ai_credits`, `cost_center`, approved $10–$20, alerts enabled, `prevent_further_usage: false` |
| Standard inherited hard per-user budget | Correct UUID, `multi_user_cost_center`, approved $2–$5 per person, hard stop, effective inherited ID for the unoverridden test user |
| Enterprise default understood | `multi_user_customer` distinguished from enterprise spending; specificity and independent headroom explained using live or explicitly illustrative evidence |
| Future usage attributed | Qualifying post-assignment activity appears against each expected cost centre; zero net billed spend is explained if included usage covered it |
| Alerts reported honestly | Saved thresholds/recipients evidenced; delivery status recorded without claiming an unobserved email or creating spend to obtain one |
| Starting state restored | Demo budgets/attachments/teams reconciled; changed test default restored; no unrelated configuration altered |

**Completion labels:** a full live lab requires resolved membership, budget,
future-attribution, and restoration evidence. If attribution/reporting is still
pending, leave live acceptance pending and name the follow-up owner. A
comparison-only session can meet the teaching outcomes but must be labelled
**comparison-only; live enforcement/attribution not exercised**. Alert
configuration and hard-stop configuration are not proof of delivery or a
threshold-crossing enforcement test. Never manufacture either to claim a pass.

## References

Official public documentation reviewed **14 September 2026**. Retrieval date is
not a release date; revisit these rolling pages before execution.

| Source | Used for |
| --- | --- |
| [Controlling and tracking costs at scale](https://docs.github.com/en/enterprise-cloud@latest/billing/tutorials/control-costs-at-scale) | UI cost-centre creation, team assignment, bundled budget workflow, alerts, overlap |
| [Budgets for usage-based billing](https://docs.github.com/en/enterprise-cloud@latest/copilot/concepts/billing/budgets-for-usage-based-billing) | ULB specificity, pool/metered phases, hard stops, headroom, exclusions; URL may redirect to the current billing-and-usage section |
| [Cost center allocation for different products](https://docs.github.com/en/enterprise-cloud@latest/billing/reference/cost-center-allocation) | Direct/team/organisation precedence, future attribution, deletion history |
| [Cost centres REST API — 2026-03-10](https://docs.github.com/en/enterprise-cloud@latest/rest/billing/cost-centers?apiVersion=2026-03-10) | Documented CRUD/resource paths, states, UUIDs, pagination |
| [Budgets REST API — 2026-03-10](https://docs.github.com/en/enterprise-cloud@latest/rest/billing/budgets?apiVersion=2026-03-10) | Request fields, scopes, alert schema, user filtering, effective-budget and pagination fields |
| [Teams in an enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-fundamentals/teams-in-an-enterprise) | Enterprise versus organisation teams, account-type and IdP-sync differences |
| [Creating enterprise teams](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/create-enterprise-teams) | People/Enterprise teams UI, member addition, access/licensing side effects |
| [Automating usage reporting](https://docs.github.com/en/enterprise-cloud@latest/billing/tutorials/automate-usage-reporting) | Reporting roles/token types, summary interpretation, safe reporting workflow |
| [Setting up budgets](https://docs.github.com/en/enterprise-cloud@latest/billing/how-tos/set-up-budgets) | Users/cost-centre selector, alerts, individual overrides, edit/delete cautions |
| [Billing usage REST API — 2026-03-10](https://docs.github.com/en/enterprise-cloud@latest/rest/billing/usage?apiVersion=2026-03-10) | Monthly summary and AI Credit usage endpoints, cost-centre/user filters, returned fields |
| [GitHub CLI: gh api](https://cli.github.com/manual/gh_api) | Explicit GET with fields, JSON request files, nested fields, pagination |
| [GitHub CLI: gh auth status](https://cli.github.com/manual/gh_auth_status) | Authentication checks without exposing tokens |
