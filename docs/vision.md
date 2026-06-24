# Product Vision (Template)

> **Customize this file** when starting a new product on this template. Replace bracketed placeholders with project-specific content. Keep harness docs (`docs/ai-workflow/`, `.skills/`) project-agnostic — product intent lives here.

## Purpose

This repository is based on the [Full Stack FastAPI Template](https://github.com/fastapi/full-stack-fastapi-template). It provides authentication, user management, a React frontend, and a FastAPI backend.

**[Product name]:** _[One-line description of what you are building]_

**[How you use the template]:** _[e.g. extend the stack with domain workflows, replace demo features, etc.]_

## Problem

_[What pain, gap, or opportunity does this product address? Who feels it today?]_

## Goals

1. **[Goal 1]** — _[Measurable outcome]_
2. **[Goal 2]** — _[Measurable outcome]_
3. **[Goal 3]** — _[Measurable outcome]_
4. **AI-assisted development** — Build and evolve the product using documented, agent-agnostic workflows ([AI coding rules](ai-workflow/ai-coding-rules.md), [harness strategy](ai-workflow/harness-strategy.md)).

## Non-goals (initial phases)

- _[Explicit exclusion 1]_
- _[Explicit exclusion 2]_
- _[Explicit exclusion 3]_

## Target users

| User | Needs |
|------|-------|
| **[Primary user]** | _[What they need from the product]_ |
| **[Secondary user]** | _[What they need from the product]_ |
| **Maintainer** | Ship features safely with documented branching and harness practices |

## Success criteria

| Criterion | Measure |
|-----------|---------|
| _[Criterion 1]_ | _[How you will know it is met]_ |
| _[Criterion 2]_ | _[How you will know it is met]_ |
| Safe delivery | Changes merge via PR with CI green; docs and skills stay agent-agnostic |
| Learning outcomes | Significant agent sessions logged in [prompt-log.md](ai-workflow/prompt-log.md) |

## Principles

1. **Trunk-based delivery** — Small PRs to `main`; see [branching strategy](branching-strategy.md).
2. **Harness before heroics** — Load vision, rules, and verification steps before coding; see [harness strategy](ai-workflow/harness-strategy.md).
3. **Human ownership** — AI coding assistants and coding agents accelerate work; humans own merges and production behavior.
4. **Minimal diffs** — Prefer focused changes that match existing FastAPI / React patterns in this template.
5. **Document the system** — Issues via [.skills/issue-author.md](../.skills/issue-author.md); implementation via [.skills/issue-implementation.md](../.skills/issue-implementation.md).

## Related documents

- [Roadmap](roadmap.md) — phased delivery plan
- [Branching strategy](branching-strategy.md) — git workflow
- [AI workflow](ai-workflow/ai-coding-rules.md) — contributor and agent rules
