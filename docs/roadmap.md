# Roadmap — Engineering Design Review Assistant

Phased plan for this fork. Update issue/PR links as work completes.

See [vision](vision.md) for product goals and [branching strategy](branching-strategy.md) for how we ship.

## Now

Foundation and engineering system (no application feature code yet).

| Item | Status | Tracking |
|------|--------|----------|
| Product vision | In progress | [docs/vision.md](vision.md) |
| Roadmap | In progress | This document |
| Branching strategy | In progress | [docs/branching-strategy.md](branching-strategy.md) |
| AI workflow docs | In progress | [docs/ai-workflow/](ai-workflow/ai-coding-rules.md) |
| Reusable agent skills | In progress | [.skills/](../.skills/issue-author.md) |
| Foundation issue | Open | [Issue #1](https://github.com/kripashetty/full-stack-fastapi-template/issues/1) |

**Exit criteria for Now:** All Issue #1 acceptance criteria met; contributors can author and implement issues using `.skills/` without tool-specific setup.

## Next

Core domain and review workflow MVP.

| Item | Notes |
|------|-------|
| Domain model | Design review entity, status enum, relationships to users |
| API — design reviews | CRUD + status transitions (FastAPI) |
| Frontend — submission flow | Create and list design review requests |
| Frontend — reviewer queue | Assigned reviews, comment thread (basic) |
| Database migrations | Alembic migrations for new tables |
| Tests | API and Playwright coverage for happy paths |

## Later

Polish, intelligence, and scale.

| Item | Notes |
|------|-------|
| Notifications | Email on assignment and status change (extend existing mail stack) |
| Design attachments | File upload and versioning |
| Review templates | Checklists per design type (API, infra, security) |
| Analytics | Time-in-review, reviewer load |
| Optional LLM assist | Summarize threads or suggest checklist items — human-in-the-loop only |
| Upstream sync | Selective merges from `fastapi/full-stack-fastapi-template` |

## Completed

| Item | Completed | PR / notes |
|------|-----------|------------|
| Fork from Full Stack FastAPI Template | — | Upstream baseline on `main` |

---

When closing roadmap items, move rows from **Now** / **Next** / **Later** to **Completed** with date and link.
