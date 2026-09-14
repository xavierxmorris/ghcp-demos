# Demo 16: cost centres and AI Credit budgets

> **Operator-led billing demo — real spend and real enforcement**
>
> Use only authorised, non-production test identities in the `GB18030-Action`
> enterprise. AI Credit use is real billable consumption, reporting can lag, and
> a hard limit can interrupt work. Never use stafftools, manual charge generators,
> private internal endpoints, or synthetic production billing-emission tools.

Feature validation date: **14 September 2026**. GitHub billing features and UI
labels can change. Validate the current UI and linked REST documentation before
the session; where API and UI capabilities differ, prefer the UI.

This is a facilitator/operator exercise, not a coding exercise. It uses
placeholders throughout and requires no separate repository.

## Learning outcomes and presenter story

By the end, participants can:

- map authorised test cohorts to cost centres through enterprise teams, with a
  direct-user fallback;
- distinguish a shared cost-centre budget from an inherited per-user budget;
- explain how enterprise, cost-centre, and explicit user budgets overlap;
- validate future usage attribution and effective controls without promising an
  exact credit cost for a prompt; and
- preserve evidence and restore the starting state.

### Business story

| Cost centre | Cohort | Budget | Behaviour |
| --- | --- | ---: | --- |
| `AI-DEMO-POWER-USERS` | Enterprise team | `$10–$20` | Alert at 75%, 90%, and 100%; do not stop usage |
| `AI-DEMO-STANDARD-USERS` | Enterprise team | `$2–$5 per user` | Stop usage at the effective limit |
| Enterprise default | Everyone else | Low test amount | Demonstrate overlapping-budget precedence |

Power users need visibility without immediate blocking. Standard users inherit
the same predictable per-person hard limit. A low, non-disruptive enterprise
default shows that applicable budgets overlap rather than add together.

In this story, “everyone else” means the universal fallback for users without a
more specific user-level budget. Technically, a `multi_user_customer` budget
applies to every Copilot-licensed user. The standard cohort's more-specific
cost-centre user-level budget replaces it; the power cohort's shared cost-centre
spending limit does not. Account for the universal limit when predicting the
power users' effective control.

Different amounts for groups inside one cost centre require separate cost
centres today. The two cost centres are therefore part of the control design,
not merely reporting labels.

### 10–15 minute presenter track

| Time | Show | Learning-loop prompt |
| ---: | --- | --- |
| 0–2 min | Starting-state evidence and the two cohorts | **Predict:** which control should apply to each test user? |
| 2–5 min | Enterprise teams and cost-centre membership | **Observe:** are direct and inherited resources represented as expected? |
| 5–8 min | Shared alert-only and inherited per-user budgets | **Explain:** why does one amount cover a group while the other applies to each person? |
| 8–11 min | Usage, budget details, and effective-budget evidence | **Challenge:** which overlapping control has least remaining headroom? |
| 11–15 min | Read-only API evidence and rollback | **Recover:** do restored settings and membership match the baseline? |

Use previously captured, redacted evidence if reporting has not caught up. Label
replay evidence as replay rather than implying that it is a live result.

### 45–60 minute operator lab

1. Complete the safety and starting-state checks (10 minutes).
2. Create or verify the two enterprise teams and cost centres (10 minutes).
3. Configure the shared, inherited, and safe default controls (10 minutes).
4. Run bounded Copilot activity with one authorised user per cohort (5 minutes).
5. Compare predicted and observed attribution and effective controls (10 minutes).
6. Export redacted evidence, challenge precedence, and roll back (10–15 minutes).

At each stage use **predict → observe → explain → challenge → recover**. Do not
manufacture a hard-limit event merely to make the demonstration look complete.

## Placeholders and local evidence

Set placeholders in a private shell. Do not paste a token into this file or a
command line. `gh` should use its credential store.

```bash
export ENTERPRISE="GB18030-Action"
export POWER_TEAM_SLUG="<POWER_ENTERPRISE_TEAM_SLUG>"
export STANDARD_TEAM_SLUG="<STANDARD_ENTERPRISE_TEAM_SLUG>"
export POWER_TEAM_ID="<POWER_ENTERPRISE_TEAM_ID>"
export STANDARD_TEAM_ID="<STANDARD_ENTERPRISE_TEAM_ID>"
export POWER_USER="<AUTHORISED_POWER_TEST_USERNAME>"
export STANDARD_USER="<AUTHORISED_STANDARD_TEST_USERNAME>"
export POWER_COST_CENTER_ID="<POWER_COST_CENTRE_UUID>"
export STANDARD_COST_CENTER_ID="<STANDARD_COST_CENTRE_UUID>"
export POWER_BUDGET_ID="<POWER_BUDGET_ID>"
export STANDARD_BUDGET_ID="<STANDARD_BUDGET_ID>"
export DEFAULT_BUDGET_ID="<TEST_DEFAULT_BUDGET_ID>"
export USAGE_YEAR="<YYYY>"
export USAGE_MONTH="<1-12_NO_LEADING_ZERO>"
export ALERT_RECIPIENT="<AUTHORISED_ALERT_RECIPIENT>"
export EVIDENCE_DIR="$HOME/ghcp-demo-16-evidence-<SESSION_ID>"
umask 077
mkdir -p "$EVIDENCE_DIR"
gh auth status
```

The team slug/ID and default-budget ID are evidence placeholders even though the
examples below do not mutate enterprise teams or the universal default.

Keep the evidence directory outside this public repository, restrict access,
and follow the enterprise retention policy. Never echo authentication
environment variables or run commands that print credentials.

## 1. Pre-demo safety and starting-state checks

The facilitator and named rollback owner must complete and sign off this list:

- [ ] Confirm enterprise-owner or billing-manager access in `GB18030-Action`.
- [ ] Confirm authorised test accounts and named rollback owners.
- [ ] Confirm each test user has the appropriate Copilot access and is not a
      production-critical identity.
- [ ] Capture existing enterprise teams, cost centres, budgets, policies, and
      relevant Usage/AI usage report state before making changes.
- [ ] Capture shared-pool state, each cost centre's **AI credit pool enabled**
      state, and the enterprise/organisation **AI credit paid usage** policy.
- [ ] Confirm every power-cohort test user has an applicable universal or
      individual user-level hard limit and the shared pool is not near
      exhaustion. Otherwise create an approved small individual test-user
      budget or use evidence-only mode.
- [ ] Search for `AI-DEMO-POWER-USERS` and `AI-DEMO-STANDARD-USERS`, including
      archived, stale, or duplicate resources; resolve name collisions rather
      than reusing an ambiguous resource.
- [ ] Review enterprise, organisation, repository, cost-centre, universal
      (`multi_user_customer`), and explicit user budgets that could overlap.
- [ ] Record the maximum approved real spend, approved `$10–$20` and `$2–$5`
      values, and alert recipients.
- [ ] Identify the universal enterprise default and confirm it will not be
      changed unless the entire enterprise is an authorised disposable sandbox.
- [ ] Record reporting time zone, current billing period, and the expected
      reporting lag communicated for the session.
- [ ] Agree stop conditions: unexpected charge, unexpected blocking, wrong
      attribution, production identity/resource, missing baseline, ambiguous
      effective budget, or spend approaching the approved maximum.

**Stop means stop:** preserve screenshots and read-only responses, cease test
activity, and let the rollback owner restore the demo. If the state remains
unclear, contact GitHub Support; do not attempt undocumented remediation.

AI Credit activity is real billable activity. Use normal test-user Copilot
features only. Included usage, paid usage, selected models, surfaces, plans, and
reporting delay all affect the eventual report.

### Starting-state record

| Item | Before value/evidence | Owner | Restore target |
| --- | --- | --- | --- |
| Test users and Copilot access | `<REDACTED_REFERENCE>` | `<OWNER>` | Original access |
| Enterprise teams/membership | `<SCREENSHOT_OR_EXPORT>` | `<OWNER>` | Original membership |
| Cost centres/resources/UUIDs | `<SCREENSHOT_OR_EXPORT>` | `<OWNER>` | Original resources |
| Budgets and effective controls | `<SCREENSHOT_OR_EXPORT>` | `<OWNER>` | Original amounts/states |
| Enterprise policies/default | `<SCREENSHOT_OR_EXPORT>` | `<OWNER>` | Original policy/default |
| Shared pool/included-usage controls | `<SCREENSHOT_OR_EXPORT>` | `<OWNER>` | Original pool settings |
| Usage/report state and time | `<REDACTED_REFERENCE>` | `<OWNER>` | Evidence only |

## 2. Create two enterprise teams or test cohorts

Enterprise teams keep cost-centre assignment current as authorised members join
or leave the team.

1. In the enterprise, open **People** → **Enterprise teams**.
2. Select **Create enterprise team**.
3. Create `AI-DEMO-POWER-USERS`; record its displayed ID/slug and creation time.
4. Use **Add members** to add only authorised power-user test identities.
5. Repeat for `AI-DEMO-STANDARD-USERS` and authorised standard test identities.
6. Verify membership in the UI and capture a redacted screenshot.

Do not create or call an undocumented enterprise-team REST endpoint.

**Direct-user fallback:** enterprise-team availability and management differ by
enterprise type and policy. If enterprise teams are unavailable, do not bypass
that control. Assign the authorised test users directly when creating each cost
centre, record that the fallback was used, and omit team lifecycle claims from
the observed result.

## 3. Create the two cost centres

1. Open **Billing and licensing** → **Cost centres**.
2. Select **New cost center** (preserve the exact UI spelling shown by GitHub).
3. Name it `AI-DEMO-POWER-USERS`.
4. Under **Resources**, add the matching enterprise team, or the authorised
   direct users if using the fallback.
5. Create the cost centre and record its returned UUID as
   `POWER_COST_CENTER_ID`.
6. Repeat for `AI-DEMO-STANDARD-USERS` and record
   `STANDARD_COST_CENTER_ID`.
7. Reopen each cost centre and verify its resource membership.

Membership assigned through an enterprise team follows team changes. For
licensed-product allocation, a direct user assignment takes precedence over
team- or organisation-derived assignment. If different enterprise teams place a
user in different cost centres, the cost centre associated with the team created
first applies. Review direct and inherited membership before selecting test
users or predicting attribution; preferably use test users with no existing
cost-centre assignment. Do not assume similarly named resources are equivalent.

### Optional mutation: cost-centre REST examples

> **Warning:** the following commands change enterprise billing configuration.
> Prefer the UI. Run them only with explicit approval, after validating the
> [current cost-centres REST documentation](https://docs.github.com/en/enterprise-cloud@latest/rest/billing/cost-centers?apiVersion=2026-03-10),
> and never as part of an unattended demo.

Listing is read-only:

```bash
gh api \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  "/enterprises/$ENTERPRISE/settings/billing/cost-centers"
```

Creating an empty cost centre and then adding a direct user are mutations:

```bash
creation="$(
  jq -n --arg name "AI-DEMO-POWER-USERS" '{name: $name}' |
  gh api --method POST \
    -H "Accept: application/vnd.github+json" \
    -H "X-GitHub-Api-Version: 2026-03-10" \
    "/enterprises/$ENTERPRISE/settings/billing/cost-centers" \
    --input -
)"
POWER_COST_CENTER_ID="$(jq -er '.id' <<<"$creation")"
unset creation
```

Compare `POWER_COST_CENTER_ID` with the UI and record it in the evidence pack.
Only after that verification, run the separate direct-user mutation:

```bash
jq -n --arg user "$POWER_USER" \
  '{users: [$user]}' |
gh api --method POST \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  "/enterprises/$ENTERPRISE/settings/billing/cost-centers/$POWER_COST_CENTER_ID/resource" \
  --input -
```

Verify and record `POWER_COST_CENTER_ID` before adding the user. Do not substitute
an enterprise team into the direct-user fallback command.

## 4. Create the power-user shared budget

1. Open **Billing and licensing** → **Budgets and alerts**.
2. Select **New budget**.
3. Set **Budget type** to **Bundled AI credits budget**.
4. Scope the budget to the `AI-DEMO-POWER-USERS` cost centre.
5. Enter a whole-dollar amount from **$10–$20**, as pre-approved.
6. Enable threshold alerts at **75%**, **90%**, and **100%** and select only the
   authorised alert recipients.
7. Leave **Stop usage when budget limit is reached** disabled.
8. Create the budget and record its budget ID.

This is one shared cost-centre budget, not `$10–$20` per user. With the stop
disabled, it tracks metered charges and sends threshold alerts after the
enterprise shared pool is exhausted; it does not cap charges or limit how much
the cohort draws from the shared pool.

### Optional mutation: power-user budget REST example

> **Warning:** this request creates a live budget. Validate the
> [current budgets REST schema](https://docs.github.com/en/enterprise-cloud@latest/rest/billing/budgets?apiVersion=2026-03-10)
> immediately before execution. The UI is the preferred path, and documented
> response enums may lag request capabilities.

```bash
export POWER_BUDGET_AMOUNT="<WHOLE_USD_10_TO_20>"
jq -n \
  --arg entity "$POWER_COST_CENTER_ID" \
  --arg recipient "$ALERT_RECIPIENT" \
  --argjson amount "$POWER_BUDGET_AMOUNT" \
  '{
    budget_amount: $amount,
    prevent_further_usage: false,
    budget_scope: "cost_center",
    budget_entity_name: $entity,
    budget_type: "BundlePricing",
    budget_product_sku: "ai_credits",
    budget_alerting: {
      will_alert: true,
      alert_recipients: [$recipient]
    }
  }' |
gh api --method POST \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  "/enterprises/$ENTERPRISE/settings/billing/budgets" \
  --input -
```

The documented alert setting enables GitHub's supported threshold notifications;
confirm the displayed 75%, 90%, and 100% behaviour in the current UI rather than
inventing a threshold-array field.

## 5. Create the inherited standard-user budget

1. Select **New budget** in **Budgets and alerts**.
2. Choose the current **Users**, cost-centre-per-user, or equivalent UI scope for
   bundled AI Credits.
3. Select `AI-DEMO-STANDARD-USERS`.
4. Enter the approved **$2–$5 per user** amount.
5. Confirm that the user-level budget is an inherent hard stop. If the current
   UI displays **Stop usage when budget limit is reached**, leave it enabled;
   do not switch to a shared cost-centre budget merely to find that control.
6. Enable threshold alerts if the current UI makes them available for this
   budget type.
7. Create the budget, record its ID, and inspect its member/effective-user view.

Every eligible cost-centre member inherits the same per-person limit. This is
not a shared `$2–$5` pool. A separately configured explicit user budget may also
overlap and take precedence.

### Optional mutation: inherited budget REST body

> **Warning:** API and UI capabilities may roll out independently. Validate this
> body against the current REST docs and UI before use. Prefer UI creation.

```json
{
  "budget_amount": 3,
  "prevent_further_usage": true,
  "budget_scope": "multi_user_cost_center",
  "budget_entity_name": "<STANDARD_COST_CENTRE_UUID>",
  "budget_type": "BundlePricing",
  "budget_product_sku": "ai_credits",
  "budget_alerting": {
    "will_alert": true,
    "alert_recipients": ["<AUTHORISED_ALERT_RECIPIENT>"]
  }
}
```

Use an approved whole-dollar value from `$2–$5`; do not copy the example value
without approval.

## 6. Configure or identify a low enterprise default

Identify the applicable `multi_user_customer` bundled AI Credit budget used as
the fallback for everyone without a more-specific user-level budget. This is a
universal per-user budget: it applies enterprise-wide and always hard-stops each
user at their effective limit.

**Do not lower, replace, or repurpose a production enterprise default merely for
this demonstration.** Prefer an existing approved default and demonstrate
precedence from redacted configuration/effective-budget evidence or a
facilitator diagram. Create a low test default only if the entire enterprise is
an authorised disposable sandbox, every affected Copilot user is in scope, and
the amount is approved as non-disruptive. Record its budget ID and amount.

1. In **Budgets and alerts**, identify the bundled AI Credits budget with the
   universal **Users** scope (`multi_user_customer` in REST).
2. Record its amount, effective user state, and hard-stop behaviour.
3. Only under the disposable-enterprise condition above, select **New budget**,
   choose **Bundled AI credits budget**, choose the universal **Users** scope,
   and enter the approved low test amount.
4. Confirm the per-user hard stop, create the budget, and record its ID. If any
   affected user is outside the authorisation, cancel instead.

## 7. Generate controlled AI Credit usage

Start with one authorised user in each cohort. In a disposable repository, ask
Copilot to perform one small, normal task, for example:

- explain a short non-sensitive function;
- generate a tiny unit test; or
- review a small disposable change.

Do not include sensitive prompt content or ask for wasteful repeated generation.
Do not promise an exact number of credits for a prompt.

The standard cohort's user-level budget counts consumption in both the included
pool and metered phases. The power cohort's shared cost-centre budget records
only metered charges after the pool is exhausted. A small task may therefore
leave the power budget at `$0` even after reporting catches up. Do not exhaust
the shared pool or force an alert for the demo; use clearly labelled, previously
captured redacted evidence when metered-phase or alert evidence is required.
If **AI credit paid usage** is disabled, usage stops at pool exhaustion
regardless of remaining metered budgets.

An enabled cost-centre included-usage control can also block the cohort or move
it to approved paid overage before the enterprise pool is exhausted. Do not
disable an existing production control for this demo. Include its state and
configured exhaustion behaviour in each prediction, or use evidence-only mode.

| Actor | Expected cost centre | Model/surface | Start/end (UTC) | Purpose | Evidence location |
| --- | --- | --- | --- | --- | --- |
| `<POWER_TEST_USER>` | `AI-DEMO-POWER-USERS` | `<MODEL/SURFACE>` | `<TIMES>` | `<BOUNDED_TASK>` | `<REDACTED_REFERENCE>` |
| `<STANDARD_TEST_USER>` | `AI-DEMO-STANDARD-USERS` | `<MODEL/SURFACE>` | `<TIMES>` | `<BOUNDED_TASK>` | `<REDACTED_REFERENCE>` |

Stop before an unapproved charge or operational impact. Included usage, paid
usage, reporting lag, plan differences, and selected models can change what and
when data appears.

## 8. View attribution and budget details

1. Open **Billing and licensing** → **Usage**.
2. Filter by cost centre where the current UI supports it.
3. Open **Budgets and alerts** and inspect each budget's usage, effective budget,
   members, status, stop-usage setting, and alert state.
4. Compare the observations with the prediction; do not reinterpret missing
   delayed data as zero usage.

A newly created cost centre should begin attributing future qualifying usage.
Historical usage may not be retroactively reassigned, and deleting a cost centre
does not rewrite historical billing attribution.

| Cohort | Expected evidence | Observed evidence | Result/follow-up |
| --- | --- | --- | --- |
| Power users | Correct cost centre; shared `$10–$20`; alerts on; stop off; `$0` metered spend is valid while the shared pool serves usage | `<OBSERVED>` | `<PASS/STOP/RECHECK>` |
| Standard users | Correct cost centre; inherited `$2–$5`; hard stop on | `<OBSERVED>` | `<PASS/STOP/RECHECK>` |
| Everyone else | Safe default remains applicable | `<OBSERVED>` | `<PASS/STOP/RECHECK>` |

## 9. Demonstrate overlapping-budget precedence

Budgets overlap; they do **not** sum. Apply two distinct rules:

1. **User-level budget specificity:** an explicit user budget replaces a
   cost-centre user-level budget, which replaces the universal
   `multi_user_customer` budget. User-level budgets are always hard stops.
2. **Independent user-level and metered spending controls:** after the shared
   pool is exhausted, the applicable control with the least remaining headroom
   blocks first. Raising a cost-centre or enterprise spending limit cannot
   unblock a user who has exhausted their user-level budget.

| Applicable controls | Safe prediction |
| --- | --- |
| Universal default only | The universal per-user hard limit applies |
| Universal default + power shared budget | The universal per-user limit still applies; the alert-only shared limit independently observes metered cohort spend |
| Universal default + shared + standard cost-centre per-user | The standard per-user budget replaces the universal default; the shared metered control remains independent |
| Universal default + shared + per-user + explicit user override | The explicit user budget replaces broader user-level budgets; the applicable metered spending limit remains independent |

For each test user, record the effective user-level budget, applicable metered
spending limit, consumption when returned, and remaining headroom. Challenge the
prediction by changing only a paper example, not a live production control. If
observed precedence differs, stop, preserve evidence, roll back, and contact
GitHub Support.

## 10. Export and API validation

These commands are read-only. Recheck the latest API version and endpoint
documentation before the session.

### Save redacted cost-centre and budget evidence

Reapply restrictive file permissions if this is a new shell. The cost-centre
export keeps only the two demo records and removes Azure subscription data and
non-demo resource names.

```bash
umask 077

gh api \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  "/enterprises/$ENTERPRISE/settings/billing/cost-centers" |
jq --arg power "$POWER_COST_CENTER_ID" \
   --arg standard "$STANDARD_COST_CENTER_ID" \
  '{
    costCenters: [
      .costCenters[]
      | select((.id | tostring) == $power or (.id | tostring) == $standard)
      | {
          id,
          name,
          state,
          ai_credit_pool_enabled,
          ai_credit_pool_state,
          resources: [
            .resources[]
            | {
                type,
                name: (
                  if .name == "AI-DEMO-POWER-USERS"
                     or .name == "AI-DEMO-STANDARD-USERS"
                  then .name
                  else "<redacted-resource>"
                  end
                )
              }
          ]
        }
    ]
  }' \
  > "$EVIDENCE_DIR/cost-centres.redacted.json"

# Get every page, but save only a scope/type inventory for unrelated budgets.
: > "$EVIDENCE_DIR/budgets-inventory.redacted.jsonl"
page=1
while :; do
  response="$(
    gh api \
      -H "Accept: application/vnd.github+json" \
      -H "X-GitHub-Api-Version: 2026-03-10" \
      "/enterprises/$ENTERPRISE/settings/billing/budgets?per_page=100&page=$page"
  )"
  jq --argjson page "$page" \
    '{
      page: $page,
      total_count,
      has_next_page,
      budgets: [
        .budgets[]
        | {budget_scope, budget_type, budget_product_sku}
      ]
    }' <<<"$response" >> "$EVIDENCE_DIR/budgets-inventory.redacted.jsonl"
  [[ "$(jq -r '.has_next_page // false' <<<"$response")" == "true" ]] || break
  page=$((page + 1))
done
unset response

# Exercise both documented scope filters and retain only known demo budget IDs.
for scope in cost_center multi_user_cost_center; do
  : > "$EVIDENCE_DIR/budgets-$scope.redacted.jsonl"
  page=1
  while :; do
    response="$(
      gh api \
        -H "Accept: application/vnd.github+json" \
        -H "X-GitHub-Api-Version: 2026-03-10" \
        "/enterprises/$ENTERPRISE/settings/billing/budgets?scope=$scope&per_page=100&page=$page"
    )"
    jq --arg power "$POWER_BUDGET_ID" \
       --arg standard "$STANDARD_BUDGET_ID" \
       --argjson page "$page" \
      '{
        page: $page,
        total_count,
        has_next_page,
        budgets: [
          .budgets[]
          | select(.id == $power or .id == $standard)
          | {
              id,
              budget_type,
              budget_amount,
              prevent_further_usage,
              budget_scope,
              budget_entity_name,
              budget_product_sku,
              consumed_amount,
              budget_alerting: {
                will_alert: .budget_alerting.will_alert,
                alert_recipients: (
                  .budget_alerting.alert_recipients
                  | map("<redacted-recipient>")
                )
              }
            }
        ]
      }' <<<"$response" >> "$EVIDENCE_DIR/budgets-$scope.redacted.jsonl"
    [[ "$(jq -r '.has_next_page // false' <<<"$response")" == "true" ]] || break
    page=$((page + 1))
  done
done
unset response
```

Inspect every file before sharing; cost-centre UUIDs and budget IDs may remain
only in the approved evidence pack. The inventory proves that every page was
read without retaining unrelated entities, amounts, recipients, or IDs.

Filter budget details by the standard test username to retrieve the documented
`effective_budget` summary:

```bash
umask 077
gh api \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  "/enterprises/$ENTERPRISE/settings/billing/budgets?user=$STANDARD_USER&per_page=100&page=1" |
jq --arg standard "$STANDARD_BUDGET_ID" \
  '{
    has_next_page,
    total_count,
    effective_budget,
    budgets: [
      .budgets[]
      | select((.id | tostring) == $standard)
      | {
          id,
          budget_type,
          budget_amount,
          prevent_further_usage,
          budget_scope,
          budget_product_sku,
          consumed_amount
        }
    ]
  }' \
  > "$EVIDENCE_DIR/standard-effective-budget.redacted.json"
```

Confirm `has_next_page` is false; if not, repeat with the next `page` value.
The separate `/{budget_id}/user-states` endpoint is documented specifically for
`multi_user_customer`; do not assume it supports `multi_user_cost_center`.

### Query usage for a month and cost centre

```bash
umask 077
gh api --paginate \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  "/enterprises/$ENTERPRISE/settings/billing/ai_credit/usage?year=$USAGE_YEAR&month=$USAGE_MONTH&cost_center_id=$POWER_COST_CENTER_ID" |
jq '{
  timePeriod,
  costCenter,
  usageItems: [
    .usageItems[]
    | {
        product,
        sku,
        model,
        unitType,
        pricePerUnit,
        grossQuantity,
        discountQuantity,
        netQuantity,
        grossAmount,
        discountAmount,
        netAmount
      }
  ]
}' \
  > "$EVIDENCE_DIR/power-usage.redacted.json"
```

Verify the latest API version and endpoint documentation first. Billing usage
permissions and authentication support can differ from other REST endpoints.

### Evidence checks

- [ ] Cost-centre name and UUID match the intended cohort.
- [ ] Resource membership shows the intended team or direct-user fallback.
- [ ] Budget type, scope, amount, alerting, and stop-usage flag match the plan.
- [ ] `consumed_amount` and effective-budget fields are recorded when returned.
- [ ] Every budgets response page was inspected and each final
      `has_next_page` value is false.
- [ ] Usage results carry the expected future cost-centre attribution.
- [ ] No tokens, credentials, private prompts, or unrelated usage records are in
      the saved evidence.

## 11. Cleanup and restoration

Cleanup is part of the demo, not an optional afterthought:

1. Record budget IDs and final redacted evidence, then disable or delete demo
   budgets first.
2. Remove authorised test users/teams from the demo cost centres.
3. Restore any captured prior direct cost-centre assignments and effective
   budgets displaced by the demo.
4. Archive/delete demo cost centres only after confirming that no required
   billing identity or production resource is attached.
5. Remove test users from demo enterprise teams and delete only teams created
   for this demo.
6. Restore any intentionally changed test-enterprise default and original
   Copilot access.
7. Re-run the read-only API checks and capture a redacted audit-log/evidence note.
8. Compare the final state to the starting-state record.

Deletion changes future control and attribution; it does not retroactively
change historical billing attribution.

| Action | Owner | Trigger | Verification |
| --- | --- | --- | --- |
| Stop activity and preserve evidence | `<FACILITATOR>` | Any stop condition | Timestamped evidence and no further test activity |
| Disable/delete demo budgets | `<BILLING_OWNER>` | Demo complete or unexpected enforcement | IDs absent/inactive; original budgets unchanged |
| Remove demo resources and restore prior assignments | `<BILLING_OWNER>` | Budgets removed | Membership and effective budgets match baseline |
| Archive/delete demo cost centres | `<BILLING_OWNER>` | No required resource attached | Read-only list and UI confirm state |
| Restore test default and Copilot access | `<BILLING_OWNER>` | Precedence segment complete | Access, amount, alerts, and stop state match baseline |
| Remove demo teams/members | `<ENTERPRISE_OWNER>` | Cost-centre cleanup complete | Team list/membership matches baseline |
| Escalate to GitHub Support | `<SUPPORT_OWNER>` | Attribution/enforcement remains unclear | Support case references preserved evidence |

## 12. Troubleshooting and known risks

| Symptom/risk | Safe response |
| --- | --- |
| Reporting delay | Stop generating usage, record the time window, preserve evidence, and recheck later |
| Unexpected blocking from overlap | Stop user activity; compare all applicable scopes and restore demo budgets |
| Direct versus indirect precedence differs from prediction | Preserve membership evidence, remove demo assignments, and seek support |
| Stale, deleted, or duplicate resource | Do not reuse or force-delete it; revert the demo and contact GitHub Support |
| API/UI rollout difference | Prefer the UI, record both views and versions, and do not invent a request field |
| Enterprise-team support differs by enterprise type | Use the documented direct-user fallback or stop the demo |
| Cost-centre user-level budget is not effective | Stop hard-limit testing, preserve user-state output, restore, and seek support |
| Attribution appears as unmapped or **Enterprise Only** | Stop generating usage, retain actor/time/cost-centre evidence, restore, and seek support |
| Hard-limit test affects real developer work | Stop immediately, restore the baseline, notify the rollback owner, and seek support if needed |

For every unresolved discrepancy: stop, preserve evidence, revert the demo, and
use GitHub Support. Do not use undocumented endpoints or internal tools.
A user blocked by a hard limit remains blocked until the next billing cycle or
an administrator increases the relevant budget; do not continue testing while
waiting for recovery.

## 13. Evidence pack and acceptance criteria

Store one redacted evidence bundle in the approved restricted location:

- before/after screenshots;
- cost-centre UUIDs and budget IDs;
- redacted API responses;
- test-user-to-cohort mapping;
- the expected/observed table;
- alert delivery evidence; and
- rollback confirmation and any support reference.

If no threshold is safely reached, use evidence of the configured recipients
and a previously captured, explicitly labelled approved alert; never force
billable usage merely to produce an email.

Do not include tokens, credentials, real names, private prompt content, unrelated
usage records, customer data, or Azure subscription IDs.

The demo is accepted only when:

- [ ] Each cost centre has the correct team or documented direct-user fallback.
- [ ] Power users have a shared `$10–$20` alert-only budget with 75%, 90%, and
      100% alerts and no hard stop.
- [ ] Standard users inherit the approved `$2–$5` per-user hard limit.
- [ ] Enterprise-default overlap and least-headroom precedence are understood
      and evidenced without a production outage.
- [ ] Qualifying future usage is attributed to the expected cost centre, or a
      reporting-delay follow-up is explicitly open.
- [ ] Read-only evidence confirms the intended type, scope, amount, alerts,
      stop-usage state, and effective budget when available.
- [ ] Cleanup restores the recorded starting state.

## References

- [Controlling costs at scale](https://docs.github.com/en/enterprise-cloud@latest/billing/tutorials/control-costs-at-scale)
- [Budgets for usage-based Copilot billing](https://docs.github.com/en/enterprise-cloud@latest/copilot/concepts/billing/budgets-for-usage-based-billing)
- [Cost-centre allocation](https://docs.github.com/en/enterprise-cloud@latest/billing/reference/cost-center-allocation)
- [Cost-centres REST API](https://docs.github.com/en/enterprise-cloud@latest/rest/billing/cost-centers?apiVersion=2026-03-10)
- [Budgets REST API](https://docs.github.com/en/enterprise-cloud@latest/rest/billing/budgets?apiVersion=2026-03-10)
- [Teams in an enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-fundamentals/teams-in-an-enterprise)
- [Creating enterprise teams](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/create-enterprise-teams)
- [Automating usage reporting](https://docs.github.com/en/enterprise-cloud@latest/billing/tutorials/automate-usage-reporting)
