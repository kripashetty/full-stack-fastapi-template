# Branching Strategy

Trunk-based workflow for the Engineering Design Review Assistant fork.

## Trunk

- **`main`** is the integration branch and deployable trunk.
- Feature work merges via pull request; avoid long-lived branches.
- Keep PRs small enough to review in one sitting when possible.

## Branch naming

| Prefix | Use | Example |
|--------|-----|---------|
| `feature/` | New capability or docs milestone | `feature/project-setup` |
| `fix/` | Bug fix | `fix/review-status-transition` |
| `chore/` | Tooling, deps, non-user-facing maintenance | `chore/sync-upstream` |

Use lowercase kebab-case after the prefix. Match the **Suggested branch name** on GitHub issues when provided.

## Workflow

1. Sync `main`: `git checkout main && git pull`
2. Create branch: `git checkout -b feature/<name>`
3. Implement per issue scope; follow [AI coding rules](ai-workflow/ai-coding-rules.md)
4. Run verification (see [harness strategy](ai-workflow/harness-strategy.md))
5. Push and open PR to `main`
6. Address review; ensure CI passes
7. Merge (squash or merge commit per repo settings)
8. Delete branch after merge

## Pull request expectations

- **Title:** Conventional Commits style, e.g. `feat(reviews): add submission API`
- **Description:** Summary, test plan, `Fixes #<issue>` when applicable — see [.skills/issue-implementation.md](../.skills/issue-implementation.md)
- **Scope:** One issue or tightly related change set
- **Checks:** Backend tests, frontend lint/tests, Playwright when UI changes — CI is the final harness
- **Docs:** Update `docs/` when behavior or workflow changes

## Hotfix process

1. Branch from `main`: `fix/<short-description>`
2. Minimal fix only; no drive-by refactors
3. Fast PR with explicit test plan
4. Merge to `main` first; backport only if you maintain release branches (not required initially)

## Upstream sync (optional)

This fork tracks [fastapi/full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template).

```bash
git remote add upstream https://github.com/fastapi/full-stack-fastapi-template.git  # once
git fetch upstream
git checkout main
git merge upstream/master   # or upstream/main — match upstream default
# Resolve conflicts; run full test harness
```

- Sync on a schedule or when you need upstream security/template fixes.
- Prefer selective merges over blind bulk merges when the fork has diverged on product code.
- Document significant syncs in PR description.

## Related

- [Vision](vision.md)
- [Roadmap](roadmap.md)
- [Issue implementation skill](../.skills/issue-implementation.md)
