# Branching Strategy

Git workflow for this repository: **`main` holds the template baseline**, **`develop` integrates product work**, and **tags on `develop` mark deployable releases**.

## Branches

| Branch | Role |
|--------|------|
| **`main`** | Stable template baseline. Tracks upstream template fixes and shared scaffolding. Not used for day-to-day feature work or deployment. |
| **`develop`** | Integration branch for active product development. Feature branches merge here. Tags on `develop` identify what gets deployed. |
| **`feature/`**, **`fix/`**, **`chore/`** | Short-lived branches cut from `develop`; merged back via pull request. |

## Branch naming

| Prefix | Use | Example |
|--------|-----|---------|
| `feature/` | New capability or docs milestone | `feature/project-setup` |
| `fix/` | Bug fix | `fix/auth-redirect` |
| `chore/` | Tooling, deps, non-user-facing maintenance | `chore/sync-upstream` |

Use lowercase kebab-case after the prefix. Match the **Suggested branch name** on GitHub issues when provided.

## Feature workflow

1. Sync `develop`: `git checkout develop && git pull`
2. Create branch: `git checkout -b feature/<name>`
3. Implement per issue scope; follow [AI coding rules](ai-workflow/ai-coding-rules.md)
4. Run verification (see [harness strategy](ai-workflow/harness-strategy.md))
5. Push and open PR to **`develop`**
6. Address review via [.skills/pr-review-resolution.md](../.skills/pr-review-resolution.md); ensure CI passes
7. Merge (squash or merge commit per repo settings)
8. Delete branch after merge

## Deployment tags

Deploy from annotated tags on **`develop`**, not from `main`.

1. Ensure `develop` is green in CI and contains the changes you want to ship.
2. Create an annotated tag on the commit to deploy:

   ```bash
   git checkout develop && git pull
   git tag -a v0.1.0 -m "Release v0.1.0"
   git push origin v0.1.0
   ```

3. Point your deployment pipeline (or manual deploy) at that tag.
4. Use [Semantic Versioning](https://semver.org/) for tag names (`vMAJOR.MINOR.PATCH`).

Tag only commits that have passed review and CI on `develop`. Do not move or force-update release tags once deployed.

## Pull request expectations

- **Target branch:** `develop` (not `main`)
- **Title:** Conventional Commits style, e.g. `feat(api): add resource endpoint`
- **Description:** Summary, test plan, `Fixes #<issue>` when applicable — see [.skills/issue-implementation.md](../.skills/issue-implementation.md)
- **Scope:** One issue or tightly related change set
- **Checks:** Backend tests, frontend lint/tests, Playwright when UI changes — CI is the final harness
- **Docs:** Update `docs/vision.md` or `docs/roadmap.md` for product changes; harness docs only when workflow changes

## Hotfix process

1. Branch from `develop`: `fix/<short-description>`
2. Minimal fix only; no drive-by refactors
3. Fast PR to **`develop`** with explicit test plan
4. After merge, tag a new patch release on `develop` (e.g. `v0.1.1`) and deploy from that tag

If production is running an older tag and you must patch without taking other `develop` changes, branch from that tag, open PR back to `develop`, then tag the resulting commit.

## Keeping `main` in sync

Use `main` to absorb upstream template updates, then bring them into product work on `develop`.

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

Then merge `main` into `develop`:

```bash
git checkout develop
git merge main
# Resolve conflicts; run full test harness
git push origin develop
```

- Sync on a schedule or when you need upstream security/template fixes.
- Prefer selective merges over blind bulk merges when the fork has diverged on product code.
- Document significant syncs in PR description.

### Bootstrapping `develop`

When starting a new product from this template:

```bash
git checkout main
git pull
git checkout -b develop
git push -u origin develop
```

All feature work branches from `develop` after that.

## Related

- [Vision](vision.md)
- [Roadmap](roadmap.md)
- [Issue implementation skill](../.skills/issue-implementation.md)
- [PR review resolution skill](../.skills/pr-review-resolution.md)
