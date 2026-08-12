---
emoji: 📊
description: Daily digest of recent repository activity — issues, pull requests, commits, releases, and CI health — published as a GitHub issue.
on:
  schedule: daily
  workflow_dispatch:
permissions:
  contents: read
  issues: read
  pull-requests: read
  actions: read
  copilot-requests: write
tools:
  github:
    mode: gh-proxy
    toolsets: [default]
safe-outputs:
  mentions: false
  allowed-github-references: []
  create-issue:
    title-prefix: "Daily Activity Report: "
    labels: [automated-report]
    close-older-issues: true
    max: 1
---

# Daily Repository Activity Report

## Task

Report on recent activity in `${{ github.repository }}` and publish the result as a GitHub issue using the `create-issue` safe output.

## Reporting Window

Use a fixed, closed window so runs are deterministic and comparable:

- **Window**: the last 24 full hours ending at workflow start (UTC).
- Derive `WINDOW_END` from the current UTC time at run start and `WINDOW_START` as `WINDOW_END - 24h`.
- Record both timestamps in ISO 8601 (`YYYY-MM-DDTHH:MM:SSZ`) and state them explicitly in the report.
- Only count events whose timestamp falls inside the window. Items merely *updated* outside the window must be excluded.

## Data To Gather

Use `gh` commands for all GitHub reads. Request JSON and filter locally rather than paging through large HTML responses.

```bash
gh issue list --repo "$GITHUB_REPOSITORY" --state all --limit 100 \
  --json number,title,state,author,createdAt,updatedAt,closedAt,labels,url \
  --search "updated:>=$WINDOW_START"

gh pr list --repo "$GITHUB_REPOSITORY" --state all --limit 100 \
  --json number,title,state,author,createdAt,updatedAt,closedAt,mergedAt,isDraft,labels,additions,deletions,url \
  --search "updated:>=$WINDOW_START"

gh api "repos/$GITHUB_REPOSITORY/commits?since=$WINDOW_START&until=$WINDOW_END" --paginate

gh api "repos/$GITHUB_REPOSITORY/releases?per_page=10"

gh run list --repo "$GITHUB_REPOSITORY" --limit 50 \
  --json name,displayTitle,conclusion,status,event,headBranch,createdAt,url
```

Cover these dimensions:

1. **Issues** — opened, closed, and reopened in the window.
2. **Pull requests** — opened, merged, closed without merge, and moved out of draft.
3. **Code** — commits landed on the default branch, with contributing authors and the areas or top-level directories touched.
4. **Releases** — releases or tags published in the window.
5. **CI health** — workflow runs that completed in the window, with pass/fail counts and any repeatedly failing workflow.

## Grouping and Deduplication

- **Primary grouping**: activity type (issues, pull requests, code, releases, CI).
- **Secondary grouping**: author, and — where the repository has multiple top-level project directories — the directory each change touched.
- **Deduplication key**: `daily-activity:${{ github.repository }}:<WINDOW_END date as YYYY-MM-DD>`. Include this key once, verbatim, in the issue body so repeat runs for the same day are identifiable.
- If labels, milestones, or other classification metadata are missing or inconsistent, group by the next-best available dimension and put unclassified items in an explicit **Unclassified** bucket. Never invent a classification.

## Report Format

- Set the issue title to the window end date in `YYYY-MM-DD` form. The `Daily Activity Report: ` prefix is added automatically.
- Use GitHub-flavored markdown. Start headings at `###` and use `####` for subsections. Never use `#` or `##`.
- Keep the summary, counts, and anything needing attention visible. Wrap per-item breakdowns and long lists in `<details><summary>...</summary>` blocks.
- Use `> [!NOTE]`, `> [!WARNING]`, and `> [!CAUTION]` alerts instead of emoji severity markers.
- Reference issues and pull requests as markdown links with the full URL and **no bare `#N` tokens** — for example `[Issue 123 — Fix parser crash](https://github.com/OWNER/REPO/issues/123)` or `[PR 456 — Add retry logic](https://github.com/OWNER/REPO/pull/456)`.
- Format workflow run references as `[§12345](https://github.com/OWNER/REPO/actions/runs/12345)` and include at most three under a final `**References:**` line.
- Do not add footer attribution; it is appended automatically.

Suggested structure:

```markdown
### Summary
Window: <WINDOW_START> to <WINDOW_END> (UTC)

- Issues: X opened, Y closed
- Pull requests: X opened, Y merged, Z closed unmerged
- Commits to default branch: N by M authors
- CI: P passed, F failed

### Needs Attention
[Only include when something is genuinely actionable — failing CI, stalled PRs, spike in new bugs.]

<details>
<summary>Issue activity</summary>
...
</details>

<details>
<summary>Pull request activity</summary>
...
</details>

<details>
<summary>Code and releases</summary>
...
</details>

<details>
<summary>CI health</summary>
...
</details>

### Context
Dedup key: daily-activity:OWNER/REPO:YYYY-MM-DD
```

## Safe Outputs

- Publish exactly one issue with `create-issue`. The body must be substantive (at least 20 characters, well under 65000) — never placeholder text.
- Yesterday's report is closed automatically by `close-older-issues`; do not attempt to close or comment on it yourself.
- Call `noop` with the evaluated window when the window contains no qualifying activity, for example:
  `noop("No repository activity in last 24 full hours (<WINDOW_START> to <WINDOW_END>)")`
- Missing metadata alone is never a reason to skip the report — only a genuinely empty window is.
