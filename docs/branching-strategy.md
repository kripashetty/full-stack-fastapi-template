# Branching Strategy

Git workflow for this repository: **`main` holds the template baseline**, **`develop/design-review-assistant` integrates product work** for the Engineering Design Review Tracker, and **tags on the integration branch mark deployable releases**.

## Branches

| Branch | Role |
|--------|------|
| **`main`** | Stable template baseline. Tracks upstream template fixes and shared scaffolding. Not used for day-to-day feature work or deployment. |
| **`develop/design-review-assistant`** | Integration branch for the Engineering Design Review Tracker. Feature branches merge here. Tags on this branch identify what gets deployed. |
| **`feature/`**, **`fix/`**, **`chore/`** | Short-lived branches cut from the integration branch; merged back via pull request. |

## Branch naming

| Prefix | Use | Example |
|--------|-----|---------|
| `feature/` | New capability or docs milestone | `feature/project-setup` |
| `fix/` | Bug fix | `fix/auth-redirect` |
| `chore/` | Tooling, deps, non-user-facing maintenance | `chore/sync-upstream` |

Use lowercase kebab-case after the prefix. Match the **Suggested branch name** on GitHub issues when provided.

## Feature workflow

1. Sync integration branch: `git checkout develop/design-review-assistant && git pull`
2. Create branch: `git checkout -b feature/<name>`
3. Implement per issue scope; follow [AI coding rules](ai-workflow/ai-coding-rules.md)
4. Run [pre-PR readiness](../.skills/pre-pr-readiness.md) before commit; run verification (see [harness strategy](ai-workflow/harness-strategy.md))
5. Push and open PR to **`develop/design-review-assistant`**
6. Address review via [.skills/pr-review-resolution.md](../.skills/pr-review-resolution.md); ensure CI passes
7. Merge (squash or merge commit per repo settings) — **human approval required**
8. Delete branch after merge

## Deployment tags

Deploy from annotated tags on **`develop/design-review-assistant`**, not from `main`.

1. Ensure the integration branch is green in CI and contains the changes you want to ship.
2. Create an annotated tag on the commit to deploy:

   ```bash
   git checkout develop/design-review-assistant && git pull
   git tag -a v0.1.0 -m "Release v0.1.0"
   git push origin v0.1.0
   ```

3. Point your deployment pipeline (or manual deploy) at that tag.
4. Use [Semantic Versioning](https://semver.org/) for tag names (`vMAJOR.MINOR.PATCH`).

Tag only commits that have passed review and CI on the integration branch. Do not move or force-update release tags once deployed.

## Pull request expectations

- **Target branch:** `develop/design-review-assistant` (not `main`)
- **Title:** Conventional Commits style, e.g. `feat(api): add resource endpoint`
- **Description:** Use [.github/pull_request_template.md](../.github/pull_request_template.md); include `Fixes #<issue>` — see [.skills/issue-implementation.md](../.skills/issue-implementation.md)
- **Scope:** One issue or tightly related change set
- **Checks:** Backend tests, frontend lint/tests, Playwright when UI changes — CI is the final harness
- **Docs:** Update `docs/vision.md` or `docs/roadmap.md` for product changes; harness docs only when workflow changes

## Hotfix process

1. Branch from `develop/design-review-assistant`: `fix/<short-description>`
2. Minimal fix only; no drive-by refactors
3. Fast PR to **`develop/design-review-assistant`** with explicit test plan
4. After merge, tag a new patch release (e.g. `v0.1.1`) and deploy from that tag

If production is running an older tag and you must patch without taking other integration-branch changes, branch from that tag, open PR back to `develop/design-review-assistant`, then tag the resulting commit.

## Keeping `main` in sync

Use `main` to absorb upstream template updates, then bring them into product work on `develop/design-review-assistant`.

### Upstream sync (optional)

If this repo tracks [fastapi/full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template) or another upstream:

```bash
git remote add upstream <upstream-url>  # once
git fetch upstream
git checkout main
git merge upstream/<default-branch>
# Resolve conflicts; run full test harness
git push origin main
```

Then merge `main` into the integration branch:

```bash
git checkout develop/design-review-assistant
git merge main
# Resolve conflicts; run full test harness
git push origin develop/design-review-assistant
```

- Sync on a schedule or when you need upstream security/template fixes.
- Prefer selective merges over blind bulk merges when the fork has diverged on product code.
- Document significant syncs in PR description.

### Bootstrapping the integration branch

When starting a new product from this template:

```bash
git checkout main
git pull
git checkout -b develop/<product-name>
git push -u origin develop/<product-name>
```

All feature work branches from the integration branch after that. For this product: `develop/design-review-assistant`.

## Related

- [Vision](vision.md)
- [Roadmap](roadmap.md)
- [Developer onboarding](ai-workflow/developer-onboarding.md)
- [Issue implementation skill](../.skills/issue-implementation.md)
- [Pre-PR readiness skill](../.skills/pre-pr-readiness.md)
- [PR review resolution skill](../.skills/pr-review-resolution.md)
