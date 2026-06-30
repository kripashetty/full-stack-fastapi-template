# Developer Onboarding

How to work on the **Engineering Design Review Tracker** using this repository's documented workflows, skills, and quality gates.

Integration branch: **`develop/design-review-assistant`**. Product intent lives in [vision](../vision.md) and [roadmap](../roadmap.md).

## Prerequisites

1. Clone the repository and read [vision](../vision.md), [roadmap](../roadmap.md), and [branching strategy](../branching-strategy.md).
2. Set up the development environment per [development.md](../../development.md).
3. Install pre-commit hooks (see [Quality gates](#quality-gates) below).

## Development lifecycle

Each stage maps to a skill or doc. Load the referenced file before starting that stage.

| Stage | Skill / doc | Outcome |
|-------|-------------|---------|
| Issue creation | [.skills/issue-author.md](../../.skills/issue-author.md) | Structured GitHub issue with scope, acceptance criteria, harness |
| Branch creation | [branching strategy](../branching-strategy.md) | Feature branch from integration branch |
| Implementation | [.skills/issue-implementation.md](../../.skills/issue-implementation.md) | Focused diff satisfying acceptance criteria |
| Pre-PR readiness | [.skills/pre-pr-readiness.md](../../.skills/pre-pr-readiness.md) | Readiness report before commit / PR |
| PR review | [.skills/pr-review-resolution.md](../../.skills/pr-review-resolution.md) | Address feedback; return to merge-ready |
| Merge | [branching strategy](../branching-strategy.md) | Squash/merge to integration branch after local verification |

---

## 1. Issue creation workflow

**Skill:** [.skills/issue-author.md](../../.skills/issue-author.md)

1. Gather problem, user story, scope, and out-of-scope boundaries.
2. Load [vision](../vision.md), [roadmap](../roadmap.md), [harness strategy](harness-strategy.md).
3. Write the issue with required sections: problem statement, scope, acceptance criteria, harness, testing, suggested branch and PR title.
4. Publish the GitHub issue; link roadmap items when applicable.

---

## 2. Branch creation workflow

**Doc:** [branching strategy](../branching-strategy.md)

1. Sync the integration branch:
   ```bash
   git checkout develop/design-review-assistant && git pull
   ```
2. Create a feature branch using the issue's suggested name or `feature/<short-description>`:
   ```bash
   git checkout -b feature/<name>
   ```
3. Confirm you are on the correct branch before editing (`git branch --show-current`).

---

## 3. Agent implementation workflow

**Skill:** [.skills/issue-implementation.md](../../.skills/issue-implementation.md)

1. Read the full GitHub issue (scope, out-of-scope, acceptance criteria, harness, testing).
2. Load [vision](../vision.md), [branching strategy](../branching-strategy.md), [AI coding rules](ai-coding-rules.md), [harness strategy](harness-strategy.md).
3. Plan deliverables → implement minimal diff → run verification → update docs if needed.
4. Log significant sessions in [prompt-log.md](prompt-log.md) when required.
5. Do **not** expand beyond issue scope.

---

## 4. Pre-PR readiness workflow

**Skill:** [.skills/pre-pr-readiness.md](../../.skills/pre-pr-readiness.md)

Run **before** committing or opening a PR:

1. Scope check — `git diff` and `git status` match issue boundaries.
2. Acceptance criteria — verify each criterion with evidence.
3. Automated checks — pre-commit, tests per issue testing requirements.
4. Migration validation — N/A when no migrations; full checklist when schema changes.
5. Workflow improvement recommendations — note harness or doc improvements discovered during work.
6. **Human approval checkpoint** — present readiness report; wait for owner approval before commit/PR.

---

## 5. PR review workflow

**Skill:** [.skills/pr-review-resolution.md](../../.skills/pr-review-resolution.md)

After opening a PR:

1. Collect unresolved review comments (inline, general, CI failures).
2. Group related feedback; plan minimal fixes.
3. Implement fixes; add/update tests when behavior changes.
4. Re-run verification; produce comment-by-comment resolution summary.
5. Request re-review when must-fix items are addressed.

Use [.github/pull_request_template.md](../../.github/pull_request_template.md) when opening PRs.

---

## 6. Merge workflow

**Doc:** [branching strategy](../branching-strategy.md)

1. PR targets **`develop/design-review-assistant`** (not `main`).
2. Local verification complete (see [Verification](#verification-ci-temporarily-disabled)).
3. Required human reviews complete.
4. Merge (squash or merge commit per repo settings).
5. Delete the feature branch after merge.
6. Update [roadmap](../roadmap.md) — move completed items to **Completed** with date and PR link.

Deploy from annotated tags on the integration branch per branching strategy.

---

## Quality gates

### Pre-commit

Configuration: [`.pre-commit-config.yaml`](../../.pre-commit-config.yaml)

Hooks include:

| Hook | Purpose |
|------|---------|
| `local-ruff-check` | Python linting (Ruff) |
| `local-ruff-format` | Python formatting (Ruff) |
| `check-yaml`, `check-toml`, `trailing-whitespace`, etc. | Repository hygiene |
| `typos` | Common typo detection |

#### Installation

From the repository root (requires [uv](https://docs.astral.sh/uv/) and project dependencies):

```bash
uv run prek install -f
```

This installs the hook at `.git/hooks/pre-commit`. Hooks run automatically on `git commit`.

#### Manual usage

Run all hooks against the entire repository:

```bash
uv run prek run --all-files
```

Run hooks only on staged files:

```bash
uv run prek run
```

If hooks modify files, stage the fixes and commit again.

See [development.md](../../development.md) for additional pre-commit details.

### Verification (CI temporarily disabled)

GitHub Actions CI workflows are **temporarily disabled**. Run verification locally before opening or merging a PR:

| Check | Command |
|-------|---------|
| Lint & format | `cd backend && uv run ruff check --force-exclude . && uv run ruff format --check --force-exclude .` |
| Pre-commit | `uv run prek run --all-files` (from repo root) |
| Backend tests | `bash ./scripts/test.sh` |
| Design tests only | `docker compose exec backend bash scripts/tests-start.sh tests/api/routes/test_designs.py -v` |

Re-enable CI by restoring workflows under `.github/workflows/` when the pipeline is ready.

---

## Related

- [Vision](../vision.md) — product goals
- [Roadmap](../roadmap.md) — phased plan
- [Harness strategy](harness-strategy.md) — verification and agent/human responsibilities
- [AI coding rules](ai-coding-rules.md) — editing conventions
- [Prompt log](prompt-log.md) — session logging
