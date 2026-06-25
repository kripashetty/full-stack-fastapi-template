# Engineering Design Review Tracker — Roadmap

See [vision](vision.md) for product goals and [branching strategy](branching-strategy.md) for how we ship.

Integration branch: **`develop/design-review-assistant`**

## Now

Project foundation and engineering workflow integration before product development.

| Item | Status | Tracking |
|------|--------|----------|
| Product vision | In progress | [docs/vision.md](vision.md) |
| Roadmap | In progress | This document |
| Developer onboarding | In progress | [docs/ai-workflow/developer-onboarding.md](ai-workflow/developer-onboarding.md) |
| Quality gates (pre-commit, CI) | In progress | [.pre-commit-config.yaml](../.pre-commit-config.yaml), [.github/workflows/ci.yml](../.github/workflows/ci.yml) |
| PR template | In progress | [.github/pull_request_template.md](../.github/pull_request_template.md) |
| Harness strategy updates | In progress | [docs/ai-workflow/harness-strategy.md](ai-workflow/harness-strategy.md) |
| Project foundation | Open | [Issue #3](https://github.com/kripashetty/full-stack-fastapi-template/issues/3) |

**Exit criteria for Now:** Vision and roadmap customized; developer onboarding documents all lifecycle workflows; pre-commit and CI configured; PR template in place; no product code added.

## Next

Core domain and review workflow MVP.

| Item | Notes |
|------|-------|
| Design review domain model | Review entity, status enum, ownership, timestamps |
| Backend API | CRUD endpoints for reviews; auth integration |
| Frontend review list & detail | Replace demo items with review tracking UI |
| Basic review lifecycle | Draft → in review → approved / rejected transitions |

## Later

Polish, scale, and optional enhancements.

| Item | Notes |
|------|-------|
| Review comments & threads | Structured feedback on reviews |
| Notifications | Email or in-app alerts for assignments and status changes |
| Reporting | Pipeline metrics, time-in-state, reviewer load |
| External doc linking | Attach links to design docs, RFCs, diagrams |

## Completed

| Item | Completed | PR / notes |
|------|-----------|------------|
| Template workflow skills | 2026-06-24 | [Issue #1](https://github.com/kripashetty/full-stack-fastapi-template/issues/1) — `.skills/issue-author.md`, `.skills/issue-implementation.md`, `.skills/pr-review-resolution.md` |

---

When closing roadmap items, move rows from **Now** / **Next** / **Later** to **Completed** with date and link.
