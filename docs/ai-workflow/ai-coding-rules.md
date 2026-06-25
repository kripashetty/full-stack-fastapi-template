# AI Coding Rules

Agent-agnostic rules for humans, AI coding assistants, and coding agents working in this repository.

**Terminology** (used across `docs/ai-workflow/` and `.skills/`):

| Term | Meaning |
|------|---------|
| **AI coding assistant** | Inline or chat assistance in an editor |
| **Coding agent** | Autonomous or semi-autonomous multi-step editing |
| **IDE-based assistant** | e.g. GitHub Copilot, Cursor (example only) |
| **CLI-based assistant** | e.g. Claude Code, Codex-style agents |
| **Agentic coding workflow** | Plan → edit → verify loops with any supported tool |
| **Manual human development** | No agent required; same rules and CI harness apply |

No single vendor is required. Supported workflows include IDE-based assistants, CLI-based assistants, GitHub-integrated agents, and manual development.

## Human ownership

- Humans own merges, production behavior, and security decisions.
- Review every agent-produced diff before commit or PR — do not blindly accept large changes.
- If agent effort to produce a PR exceeds human effort to review it, split the task or reduce scope (see upstream [CONTRIBUTING.md](../../CONTRIBUTING.md) spirit).
- Meaningful judgment and context must remain in the loop; agents accelerate, they do not replace accountability.

## Prompt hygiene

- **No secrets in prompts** — Never paste `.env` values, API keys, tokens, or production credentials into chats or logs.
- **Minimal context** — Provide issue scope, relevant file paths, and error messages; avoid dumping entire repositories.
- **Reference docs** — Point agents at [vision](../vision.md), [branching strategy](../branching-strategy.md), and this file instead of repeating rules ad hoc.
- **Log significant sessions** — Per [prompt-log.md](prompt-log.md) when experimenting or completing milestone work.

## Scope and diffs

- **Stay within issue scope** — Respect out-of-scope sections on GitHub issues.
- **Minimal diffs** — Change only what the issue requires; match existing patterns in `backend/` and `frontend/`.
- **No unrelated refactors** — Fix the requested behavior; defer cleanup to separate issues.
- **Respect issue path constraints** — e.g. docs-only issues stay under `docs/` and `.skills/` unless the issue says otherwise.

## Stack-specific conventions

### Backend (`backend/`)

- FastAPI routes under `app/api/routes/`; register in `app/api/main.py`
- SQLModel models in `app/models.py`; Alembic migrations for schema changes
- Business logic in `app/crud.py` or dedicated modules — keep routes thin
- Tests under `backend/tests/`; run via Docker or local scripts per [development.md](../../development.md)
- Format/lint: `backend/scripts/format.sh`, `backend/scripts/lint.sh`

### Frontend (`frontend/`)

- React + TanStack Router; routes under `src/routes/`
- UI components under `src/components/`; shared UI in `src/components/ui/`
- API client generated from OpenAPI — regenerate after API contract changes (`scripts/generate-client.sh`)
- Biome for lint/format; Playwright for E2E when UI behavior changes

### Documentation and skills

- **Product-specific content** belongs in [vision](../vision.md) and [roadmap](../roadmap.md) — customize those templates for your product.
- **Harness content** (`docs/ai-workflow/`, `.skills/`) stays project-agnostic and reusable as a base template.
- Cross-link vision, roadmap, [harness strategy](harness-strategy.md), and [.skills/](../../.skills/issue-implementation.md).
- Agent-agnostic wording; optional tool names as examples only.

## Agentic workflow

1. Read the GitHub issue and [.skills/issue-implementation.md](../../.skills/issue-implementation.md)
2. Load [vision](../vision.md), [branching strategy](../branching-strategy.md), this file
3. Plan → implement smallest complete change → verify → PR
4. Log outcome in [prompt-log.md](prompt-log.md) when required by the issue
5. For review feedback: follow [.skills/pr-review-resolution.md](../../.skills/pr-review-resolution.md)

## Pre-merge review checklist

- [ ] Diff matches issue scope; no unrelated files
- [ ] No secrets or credentials in code, commits, or docs
- [ ] Tests and lint pass for touched areas (or N/A for docs-only with manual verification)
- [ ] API changes reflected in client generation when applicable
- [ ] Docs updated if behavior or workflow changed
- [ ] PR title and description follow [branching strategy](../branching-strategy.md) and issue guidance
- [ ] CI expected green on merge

## Related

- [Harness strategy](harness-strategy.md)
- [Prompt log](prompt-log.md)
- [Issue author skill](../../.skills/issue-author.md)
- [Issue implementation skill](../../.skills/issue-implementation.md)
- [PR review resolution skill](../../.skills/pr-review-resolution.md)
