# Harness Engineering Strategy

How we constrain and verify work from AI coding assistants, coding agents, and manual contributors in this repository.

This document is **project-agnostic** — it applies to any product built on this template. Product intent lives in [vision](../vision.md) (customize that template per project).

Harness engineering means **feedforward**: load context and constraints *before* editing, then verify *after* — not only testing at the end.

## Harness components

| Component | Purpose | Sources in this repo |
|-----------|---------|----------------------|
| **Context** | Product intent, scope, conventions | [vision](../vision.md), GitHub issues, [roadmap](../roadmap.md) |
| **Tools** | Edit, test, lint, PR | Git, Docker Compose, `scripts/test.sh`, CI workflows |
| **Constraints** | Scope boundaries, security, style | Issue out-of-scope, [AI coding rules](ai-coding-rules.md), [branching strategy](../branching-strategy.md) |
| **Verification** | Prove correctness before merge | Local commands below, CI on PR |
| **Skills** | Repeatable workflows | [.skills/issue-author.md](../../.skills/issue-author.md), [.skills/issue-implementation.md](../../.skills/issue-implementation.md), [.skills/pr-review-resolution.md](../../.skills/pr-review-resolution.md) |

## Supported workflows

All are optional; the same harness applies:

| Workflow | How to use the harness |
|----------|------------------------|
| **IDE-based assistant** | Open repo; attach or reference `docs/vision.md`, `docs/branching-strategy.md`, `docs/ai-workflow/ai-coding-rules.md` before edits |
| **CLI-based assistant** | Pass issue URL and doc paths in the initial prompt; follow `.skills/issue-implementation.md` |
| **GitHub-integrated agent** | Issue body + linked docs as context; branch from suggested name |
| **Manual human development** | Read the same docs; run the same verification commands |

**Cursor** may be used as an IDE-based assistant example; it is not required.

## Session startup (before editing)

1. Read the GitHub issue (full body: scope, out-of-scope, acceptance criteria, harness, testing)
2. Load:
   - [docs/vision.md](../vision.md) — product context (customized per project)
   - [docs/branching-strategy.md](../branching-strategy.md)
   - [docs/ai-workflow/ai-coding-rules.md](ai-coding-rules.md)
3. For implementation: follow [.skills/issue-implementation.md](../../.skills/issue-implementation.md)
4. For new issues: follow [.skills/issue-author.md](../../.skills/issue-author.md)
5. For PR review feedback: follow [.skills/pr-review-resolution.md](../../.skills/pr-review-resolution.md)
6. Confirm branch and allowed paths

## Post-edit verification

Run commands relevant to the change:

| Change type | Verification |
|-------------|--------------|
| **Docs / skills only** | Review markdown; check relative links; `git diff` scope under `docs/` and `.skills/` |
| **Backend** | `backend/scripts/lint.sh`; tests via [development.md](../../development.md) or `scripts/test.sh` |
| **Frontend** | Biome lint; unit tests; Playwright when UI flows change |
| **Full stack** | `scripts/test.sh` or `scripts/test-local.sh` |

### CI as final harness

GitHub Actions on PR (`test-backend`, `playwright`, `test-docker-compose`, etc.) are authoritative. Local passes do not replace CI green.

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
| Disabling hooks or CI to "land faster" | Harness bypass |
| Product-specific copy in harness docs | Breaks reuse; put product detail in `docs/vision.md` |

## Logging

Log significant agent sessions per [prompt-log.md](prompt-log.md) — especially foundation work, new patterns, and failed experiments worth avoiding later.

## Related

- [AI coding rules](ai-coding-rules.md)
- [Prompt log](prompt-log.md)
- [Vision](../vision.md)
- [Branching strategy](../branching-strategy.md)
