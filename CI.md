# CI maintenance

The index and every numbered demo are independent repositories. Index CI does
not clone the child repositories, publish changes, or access private demos 09 and 14.
Each demo's `.github/workflows/ci.yml` owns its own baseline.

| Repository | Gate and intentional limits |
| --- | --- |
| Index | Inventory/README/facilitator consistency, mocked publisher privacy/error-path contracts, publisher syntax, and agentic source/lock consistency |
| 00 | Both replay asset sets and JavaScript syntax; not browser acceptance |
| 01 | Module syntax/exports and page imports; not completed helper exercises |
| 02 | Pytest with `--starter-baseline`: two named, exception-specific strict expected failures; normal pytest remains the exercise gate |
| 03 | Locked install and `npm run check` for source-only TypeScript; API behavior and the production-build exercise remain unfinished |
| 04 | Stdlib CLI regression tests on the shipped CSV normalizer; no Copilot/GitHub credentials |
| 05 | Existing implemented billing tests; tax remains an exercise |
| 06 | Strict backend starter baseline and locked frontend production build; review requests are separate, opt-in and non-gating |
| 07 | Offline domain and CI-contract tests, manifest/model/dataset validation; deployment requires the same revision to pass and uses environment-bound OIDC |
| 08 | Local links and sourced evidence structure; not external availability or current platform truth |
| 09 | Private offline replay, complete response/exit/deadline checks and negative fixtures; no payload logs, uploads or live Figma calls |
| 10 | Fresh Edge acceptance for both BRD versions plus test-pack integrity; historical results are not fresh CI evidence |
| 11 | Windows/Linux pipeline tests, explicit Python 3.10 compatibility, complete sample artifacts and reason-specific drift rejection |
| 12 | Both build paths, signed 64-bit ABI, maintained-C contracts/sanitizers, and complete generated evidence |
| 13 | Original COBOL replay, Node/Java/.NET comparisons, and source-to-port evidence; not full mainframe or tax-system parity |
| 14 | Python 3.11/3.14 on Windows/Linux: synthetic triage, policy/advisory/immutable-artifact boundaries, mocked read-only live runner, full reference integrity, and zero default customer drafts; no source/model/workflow execution |

## Shared policy

The refreshed workflows use read-only contents permissions, non-persisted
checkout credentials, job deadlines, and branch-scoped cancellation for ordinary
CI. Deployment does not cancel an in-progress provisioning operation. Artifacts
have seven-day retention. No workshop is completed just to obtain a green badge;
no generic `continue-on-error` or empty-test success flag hides failures.

Dependabot proposes grouped weekly action updates and monthly dependency updates
where manifests exist. Dependency changes still need review; starter coverage is
not an application-level compatibility guarantee. Demos 03 and 06 intentionally
exclude automatic major npm updates. Demo 03's older application dependencies
can still have advisories; CI-tooling maintenance does not claim to complete an
application security audit or migrate its Express/UUID teaching contracts.

The npm projects set `omit-lockfile-registry-resolved=true` in `.npmrc`.
Locks retain exact versions and integrity hashes without embedding an author's
corporate package-mirror URLs. `npm ci` uses the runner's configured registry;
local installations can continue using an approved mirror without changing
global settings or disabling TLS verification. See the
[npm configuration reference](https://docs.npmjs.com/cli/v11/using-npm/config#omit-lockfile-registry-resolved).

## Generated activity report

Edit `.github/workflows/daily-activity-report.md`, not its `.lock.yml`.
Regenerate with the version and runtime revision used by index CI:

```shell
gh aw compile daily-activity-report --no-check-update --action-mode release --action-tag 8e30bcd8897f5047051fa3971188e1dd4cdb23cf
```

This command requires **gh-aw v0.88.2**. Its runtime fixes the cached Copilot
installation's missing canonical executable path, which previously produced
`spawn /usr/local/bin/copilot ENOENT`. The Copilot engine is pinned to **1.0.80**,
within that release's compatibility window. Dependabot excludes the generated
lock; a compiler/runtime upgrade must regenerate it and update the CI binary
checksum together. Regeneration runs without invoking a model or publishing a
report.

Commit `.github/aw/actions-lock.json` alongside the generated workflow. It
preserves the compiler's action-pin metadata so a clean hosted runner and a
local compiler use the same version annotations, rather than producing
comment-only lock drift. See the official
[compilation-process reference](https://github.github.io/gh-aw/reference/compilation-process/).

## Version sources

Reviewed **7 September 2026** using official releases, not guessed action tags:

| Tool | Release date | Source |
| --- | --- | --- |
| checkout 7.0.1 | 20 July 2026 | [Release](https://github.com/actions/checkout/releases/tag/v7.0.1) |
| setup-node 7.0.0 | 14 July 2026 | [Release](https://github.com/actions/setup-node/releases/tag/v7.0.0) |
| setup-python 7.0.0 | 20 July 2026 | [Release](https://github.com/actions/setup-python/releases/tag/v7.0.0) |
| upload-artifact 7.0.1 | 10 April 2026 | [Release](https://github.com/actions/upload-artifact/releases/tag/v7.0.1) |
| gh-aw 0.88.2 | 3 September 2026 | [Release](https://github.com/github/gh-aw/releases/tag/v0.88.2) |
| Azure Developer CLI 1.33.0 | 3 September 2026 | [Release](https://github.com/Azure/azure-dev/releases/tag/azure-dev-cli_1.33.0) |
| Azure/setup-azd 2.4.0 | 6 August 2026 | [Release](https://github.com/Azure/setup-azd/releases/tag/v2.4.0) |
| Azure/login 3.0.2 | 26 August 2026 | [Release](https://github.com/Azure/login/releases/tag/v3.0.2) |

See GitHub's [secure-use reference](https://docs.github.com/en/actions/reference/security/secure-use)
for action pinning and permission boundaries, and the
[agentic workflow authoring guide](https://github.github.io/gh-aw/setup/creating-workflows/)
for the source/compiler contract.
