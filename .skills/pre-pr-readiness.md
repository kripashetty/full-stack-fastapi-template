# Pre-PR Readiness

Verify a branch is ready to open or update a pull request — before commit or push.

## Objective

Produce a structured readiness report that proves the issue acceptance criteria are met, verification commands pass, and the diff stays within scope. Human owners review this output before approving commits or opening PRs.

## Inputs

| Input | Required | Source |
|-------|----------|--------|
| GitHub issue | Yes | Linked issue with acceptance criteria and testing requirements |
| Working branch | Yes | Feature branch with uncommitted or committed changes |
| Harness context | Yes | `docs/ai-workflow/harness-strategy.md`, `docs/ai-workflow/ai-coding-rules.md` |
| Diff | Yes | `git diff` and `git status` |

## Preconditions

1. **Read the full issue** — Scope, out-of-scope, acceptance criteria, definition of done, harness, testing.
2. **Load context** — [vision](../docs/vision.md), [branching strategy](../docs/branching-strategy.md), [harness strategy](../docs/ai-workflow/harness-strategy.md).
3. **Confirm branch** — On the issue's suggested branch (or documented alternative).
4. **Do not commit or open PR** until the human owner reviews the readiness output (when the workflow requires it).

## Process

### 1. Scope check

Inspect `git diff` and `git status`:

- [ ] Changed files match issue scope
- [ ] No files in out-of-scope paths (e.g. product code when issue is docs-only)
- [ ] No secrets, credentials, or `.env` values in the diff
- [ ] No unrelated drive-by changes

### 2. Acceptance criteria verification

For each acceptance criterion in the issue, record:

```markdown
| Criterion | Status | Evidence |
|-----------|--------|----------|
| [criterion text] | pass / fail / N/A | [file path, command output, or manual check] |
```

All criteria must be **pass** or explicitly **N/A with rationale** before PR readiness.

### 3. Automated verification

Run commands from the issue's **Testing requirements** and harness strategy:

| Check | Typical command |
|-------|-----------------|
| Pre-commit | `uv run prek run --all-files` (from repo root) |
| Ruff lint | Included in pre-commit (`local-ruff-check`) |
| Ruff format | Included in pre-commit (`local-ruff-format`) |
| Backend tests | `scripts/test.sh` or backend test suite when backend changed |
| Docs / skills | Markdown review; relative link check |

Record pass/fail for each command run.

### 4. Migration validation

When the issue or diff touches database migrations:

- [ ] Migration applies cleanly (`alembic upgrade head`)
- [ ] Rollback path documented or tested if required by issue
- [ ] No destructive changes without explicit issue approval

For issues with **no migrations** (e.g. foundation docs), mark **N/A — no migration changes in diff**.

### 5. Documentation and cross-links

- [ ] New or updated docs cross-link related `docs/` and `.skills/` files
- [ ] Product-specific language in `docs/vision.md` / `docs/roadmap.md` when applicable
- [ ] [prompt-log.md](../docs/ai-workflow/prompt-log.md) updated when harness strategy requires it

### 6. Workflow improvement recommendations

Append suggestions for improving docs, skills, CI, or harness based on this implementation:

```markdown
## Workflow improvement recommendations

- [Recommendation 1 — what and why]
- [Recommendation 2 — optional follow-up issue if large]
```

### 7. Human approval checkpoint

**Stop here.** Present the readiness report to the human owner.

- Human reviews acceptance criteria table, command results, and diff scope
- Human approves commit and PR opening — or requests fixes
- Agents do **not** commit, push, or open PRs without explicit human approval when this workflow is invoked

## Output format

```markdown
# Pre-PR Readiness Report

**Issue:** #N — [title]
**Branch:** [branch name]
**Date:** YYYY-MM-DD

## Scope check

- [ ] pass / fail — [notes]

## Acceptance criteria

| Criterion | Status | Evidence |
|-----------|--------|----------|
| … | … | … |

## Commands run

| Command | Result |
|---------|--------|
| … | pass / fail |

## Migration validation

[N/A or checklist results]

## Files changed

- `path` — reason

## Workflow improvement recommendations

- …

## Ready for commit / PR?

**No** — awaiting human review of this report.
```

## Related

- [Issue implementation](issue-implementation.md) — full implementation workflow
- [Harness strategy](../docs/ai-workflow/harness-strategy.md) — verification expectations
- [Developer onboarding](../docs/ai-workflow/developer-onboarding.md) — lifecycle overview
- [PR review resolution](pr-review-resolution.md) — after PR is opened
