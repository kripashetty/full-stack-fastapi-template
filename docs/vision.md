# Engineering Design Review Tracker — Product Vision

## Purpose

**Engineering Design Review Tracker:** A web application that helps engineering teams plan, track, and complete design reviews with clear status, ownership, and audit history.

**How we use the template:** Extend the [Full Stack FastAPI Template](https://github.com/fastapi/full-stack-fastapi-template) with domain workflows for design review lifecycle management — replacing demo features with review tracking, while keeping the FastAPI + React + PostgreSQL stack.

## Problem

Engineering design reviews often happen across scattered documents, chat threads, and ad hoc spreadsheets. Reviewers lack a single source of truth for review status, required approvals, and decision history. Teams lose visibility into what is blocked, who owns the next action, and whether a design is approved to proceed.

## Goals

1. **Centralized review tracking** — Teams can create, assign, and track design reviews through defined lifecycle states.
2. **Clear accountability** — Each review has visible owners, reviewers, and status transitions with timestamps.
3. **Actionable visibility** — Dashboards and lists show what needs attention without digging through email or docs.
4. **AI-assisted development** — Build and evolve the product using documented, agent-agnostic workflows ([AI coding rules](ai-workflow/ai-coding-rules.md), [harness strategy](ai-workflow/harness-strategy.md)).

## Non-goals (initial phases)

- Automated AI review of design documents or LLM-generated feedback
- Full document authoring or diagram editing inside the app (linking to external docs is sufficient initially)
- Enterprise SSO, advanced RBAC, or multi-tenant isolation beyond basic auth
- Real-time collaborative editing of review content

## Target users

| User | Needs |
|------|-------|
| **Design author** | Submit designs for review, track status, respond to feedback, know when approved |
| **Reviewer** | See assigned reviews, record decisions, leave structured feedback |
| **Engineering lead** | Monitor review pipeline health, unblock stalled reviews, enforce process |
| **Maintainer** | Ship features safely with documented branching and harness practices |

## Success criteria

| Criterion | Measure |
|-----------|---------|
| Review lifecycle | A design review can move from draft → in review → approved/rejected with audit trail |
| Team adoption | Primary users complete a full review cycle without workarounds outside the app |
| Safe delivery | Changes merge via PR with CI green; docs and skills stay agent-agnostic |
| Learning outcomes | Significant agent sessions logged in [prompt-log.md](ai-workflow/prompt-log.md) |

## Principles

1. **Develop-based delivery** — Small PRs to `develop/design-review-assistant`; deploy from tags on the integration branch; see [branching strategy](branching-strategy.md).
2. **Harness before heroics** — Load vision, rules, and verification steps before coding; see [harness strategy](ai-workflow/harness-strategy.md).
3. **Human ownership** — AI coding assistants and coding agents accelerate work; humans own merges and production behavior.
4. **Minimal diffs** — Prefer focused changes that match existing FastAPI / React patterns in this template.
5. **Document the system** — Issues via [.skills/issue-author.md](../.skills/issue-author.md); implementation via [.skills/issue-implementation.md](../.skills/issue-implementation.md).

## Related documents

- [Roadmap](roadmap.md) — phased delivery plan
- [Branching strategy](branching-strategy.md) — git workflow
- [Developer onboarding](ai-workflow/developer-onboarding.md) — lifecycle workflows
- [AI workflow](ai-workflow/ai-coding-rules.md) — contributor and agent rules
