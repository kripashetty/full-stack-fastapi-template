# Harness Engineering Strategy

How we constrain and verify work from AI coding assistants, coding agents, and manual contributors in this repository.

Product intent for the Engineering Design Review Tracker lives in [vision](../vision.md). This document defines **how** work is verified — it stays reusable across products built on this template.

Harness engineering means **feedforward**: load context and constraints *before* editing, then verify *after* — not only testing at the end.

## Harness components

| Component | Purpose | Sources in this repo |
|-----------|---------|----------------------|
| **Context** | Product intent, scope, conventions | [vision](../vision.md), GitHub issues, [roadmap](../roadmap.md) |
| **Tools** | Edit, test, lint, PR | Git, Docker Compose, `scripts/test.sh`, CI workflows |
| **Constraints** | Scope boundaries, security, style | Issue out-of-scope, [AI coding rules](ai-coding-rules.md), [branching strategy](../branching-strategy.md) |
| **Verification** | Prove correctness before merge | Local commands below, [CI on PR](#ci-as-final-harness) |
| **Skills** | Repeatable workflows | [.skills/issue-author.md](../../.skills/issue-author.md), [.skills/issue-implementation.md](../../.skills/issue-implementation.md), [.skills/pre-pr-readiness.md](../../.skills/pre-pr-readiness.md), [.skills/pr-review-resolution.md](../../.skills/pr-review-resolution.md) |

## Supported workflows

All are optional; the same harness applies:

| Workflow | How to use the harness |
|----------|------------------------|
| **IDE-based assistant** | Open repo; attach or reference `docs/vision.md`, [developer onboarding](developer-onboarding.md), `docs/ai-workflow/ai-coding-rules.md` before edits |
| **CLI-based assistant** | Pass issue URL and doc paths in the initial prompt; follow `.skills/issue-implementation.md` |
| **GitHub-integrated agent** | Issue body + linked docs as context; branch from suggested name |
| **Manual human development** | Read the same docs; run the same verification commands |

**Cursor** may be used as an IDE-based assistant example; it is not required.

See [developer onboarding](developer-onboarding.md) for the full lifecycle from issue creation through merge.

## Session startup (before editing)

1. Read the GitHub issue (full body: scope, out-of-scope, acceptance criteria, harness, testing)
2. Load:
   - [docs/vision.md](../vision.md) — product context
   - [docs/branching-strategy.md](../branching-strategy.md)
   - [docs/ai-workflow/ai-coding-rules.md](ai-coding-rules.md)
3. For implementation: follow [.skills/issue-implementation.md](../../.skills/issue-implementation.md)
4. For new issues: follow [.skills/issue-author.md](../../.skills/issue-author.md)
5. Before commit/PR: follow [.skills/pre-pr-readiness.md](../../.skills/pre-pr-readiness.md)
6. For PR review feedback: follow [.skills/pr-review-resolution.md](../../.skills/pr-review-resolution.md)
7. Confirm branch and allowed paths

## Acceptance criteria verification

Every issue defines acceptance criteria in checkbox form. Verification is **explicit and evidenced**:

1. Copy each criterion from the issue into a table (see [pre-pr-readiness skill](../../.skills/pre-pr-readiness.md)).
2. Mark **pass**, **fail**, or **N/A** with evidence (file path, command output, manual check).
3. All criteria must pass (or N/A with documented rationale) before opening a PR.
4. PR descriptions must include an **Acceptance Criteria Verification** section (see [.github/pull_request_template.md](../../.github/pull_request_template.md)).

Agents produce the verification table; **humans confirm** it is accurate before merge.

## Migration validation expectations

When a PR touches database schema or Alembic migrations:

| Check | Required when |
|-------|---------------|
| `alembic upgrade head` applies cleanly | New or modified migrations |
| Downgrade path documented or tested | Destructive or data-affecting changes |
| Migration noted in PR **Migration Validation** section | Any migration file in diff |

When **no migrations** are in scope, mark **N/A — no migration changes** in the PR template. Do not skip the section — explicit N/A prevents assumptions.

## Workflow improvement recommendation process

Contributors and agents should capture harness improvements discovered during implementation:

1. Note friction points (missing docs, unclear skills, CI gaps, repeated manual steps).
2. Add bullets to the PR **Workflow Improvement Recommendations** section.
3. Trivial doc fixes can ship in the same PR; larger changes get a follow-up GitHub issue.
4. Significant patterns worth reusing → update `docs/` or `.skills/` in a focused follow-up PR.

Recommendations are **optional but encouraged** — they feed forward into better agent and human workflows.

## Human approval checkpoints

| Checkpoint | Human responsibility | Agent may |
|------------|---------------------|-----------|
| Issue scope interpretation | Approve plan when ambiguous | Propose plan; ask before expanding scope |
| Pre-PR readiness report | Review and approve before commit/PR | Produce report per pre-pr-readiness skill |
| Commit / push / open PR | Explicit approval when workflow requires it | Prepare changes locally; wait for approval |
| Merge to integration branch | Approve after review + CI green | Never merge without authorization |
| Production / deployment | Own release decisions | Document deploy steps only |

**Default rule:** Agents accelerate editing and verification; humans own commits, merges, and production behavior.

## Agent responsibilities vs human responsibilities

| Area | Agent / assistant | Human |
|------|-------------------|-------|
| Read issue, docs, skills | Yes | Yes (same harness) |
| Implement scoped changes | Yes | Yes |
| Run lint, tests, pre-commit | Yes | Yes |
| Produce acceptance criteria evidence | Yes | Review for accuracy |
| Commit, push, open PR | Only when explicitly authorized | Default owner |
| Resolve ambiguous requirements | Ask | Decide |
| Security / credential handling | Never put secrets in prompts or commits | Audit diffs |
| Merge | No | Yes |
| Update roadmap **Completed** section | Propose | Confirm and merge |

## Post-edit verification

Run commands relevant to the change:

### Verification harness (CI temporarily disabled)

GitHub Actions CI is **temporarily disabled**. Until workflows are restored, **local verification is required** before merge:

| Change type | Verification |
|-------------|--------------|
| **Docs / skills only** | Review markdown; check relative links; `git diff` scope under `docs/`, `.skills/`, `.github/` |
| **Backend** | `backend/scripts/lint.sh`; tests via [development.md](../../development.md) or `scripts/test.sh` |
| **Frontend** | Biome lint; unit tests; Playwright when UI flows change |
| **Full stack** | `scripts/test.sh` or `scripts/test-local.sh` |
| **All changes** | `uv run prek run --all-files` before PR |

## Optional assistant configuration

Tool-specific config (e.g. editor rules directories) is **optional** and not required to contribute. This repository's harness is defined by version-controlled `docs/` and `.skills/` — any assistant that can read files and run shell commands can participate.

## Task sizing

- Prefer issues and PRs reviewable in one sitting
- Split large features: domain model → API → UI → polish
- Each issue should ship a smallest complete vertical slice when possible

## Anti-patterns

| Anti-pattern | Why it fails |
|--------------|--------------|
| Edit without reading issue out-of-scope | Scope creep, rejected PRs |
| Skip verification because "docs only" | Broken links, wrong paths, inconsistent terminology |
| Vendor-specific prompts only in chat | Knowledge not reusable; use `.skills/` and `docs/` |
| Giant agent diffs without human review | Security and quality risk |
| Secrets in prompts or commits | Credential exposure |
| Disabling hooks or CI to “land faster” | Harness bypass |
| Product-specific copy in harness docs | Breaks reuse; put product detail in `docs/vision.md` |
| Commit or open PR without pre-PR readiness | Missing acceptance criteria evidence |

## Logging

Log significant agent sessions per [prompt-log.md](prompt-log.md) — especially foundation work, new patterns, and failed experiments worth avoiding later.

## Related

- [Developer onboarding](developer-onboarding.md) — full lifecycle workflows
- [AI coding rules](ai-coding-rules.md)
- [Prompt log](prompt-log.md)
- [Vision](../vision.md)
- [Branching strategy](../branching-strategy.md)
