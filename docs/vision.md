# Engineering Design Review Assistant — Product Vision

## Purpose

This repository is a fork of the [Full Stack FastAPI Template](https://github.com/fastapi/full-stack-fastapi-template), repurposed to build an **Engineering Design Review Assistant**: a web application that helps engineering teams submit, route, review, and track design documents through a structured review workflow.

The upstream template provides authentication, user management, a React frontend, and a FastAPI backend. We extend that foundation with domain-specific workflows for design reviews rather than replacing the stack.

## Problem

Engineering design reviews are often fragmented across email threads, ad hoc documents, and informal checklists. Reviewers lack a single place to see submission status, feedback history, and approval state. Submitters repeat context on every review cycle.

## Goals

1. **Centralize design review requests** — Engineers submit designs with metadata (title, domain, reviewers) in one system.
2. **Structured review workflow** — Clear states (draft → submitted → in review → approved / changes requested) with audit history.
3. **Actionable feedback** — Reviewers leave threaded comments tied to design versions.
4. **Visibility** — Dashboards for submitters and reviewers to see queue status and deadlines.
5. **AI-assisted development** — Build and evolve the product using documented, agent-agnostic workflows ([AI coding rules](ai-workflow/ai-coding-rules.md), [harness strategy](ai-workflow/harness-strategy.md)).

## Non-goals (initial phases)

- Replacing formal compliance or regulatory sign-off systems
- Real-time collaborative document editing (Google Docs–style)
- Generic project management (Jira/Linear replacement)
- Multi-tenant SaaS billing or org administration beyond basic user roles
- LLM-generated review verdicts without human reviewer accountability

## Target users

| User | Needs |
|------|-------|
| **Design submitter** | Submit a design package, track review status, respond to feedback |
| **Reviewer** | See assigned reviews, leave structured feedback, approve or request changes |
| **Review coordinator / tech lead** | Assign reviewers, monitor queue health, enforce review policies |
| **Maintainer** | Ship features safely with documented branching and harness practices |

## Success criteria

| Criterion | Measure |
|-----------|---------|
| End-to-end submission | A submitter can create a design review request and assign reviewers |
| Review loop | A reviewer can comment and change request status; submitter sees updates |
| Traceability | Status transitions and comments are persisted and queryable |
| Safe delivery | Changes merge via PR with CI green; docs and skills stay agent-agnostic |
| Learning outcomes | Prompt and harness experiments are logged in [prompt-log.md](ai-workflow/prompt-log.md) |

## Principles

1. **Trunk-based delivery** — Small PRs to `main`; see [branching strategy](branching-strategy.md).
2. **Harness before heroics** — Load vision, rules, and verification steps before coding; see [harness strategy](ai-workflow/harness-strategy.md).
3. **Human ownership** — AI coding assistants and coding agents accelerate work; humans own merges and production behavior.
4. **Minimal diffs** — Prefer focused changes that match existing FastAPI / React patterns in this template.
5. **Document the system** — Issues authored via [.skills/issue-author.md](../.skills/issue-author.md); implementation via [.skills/issue-implementation.md](../.skills/issue-implementation.md).

## Related documents

- [Roadmap](roadmap.md) — phased delivery plan
- [Branching strategy](branching-strategy.md) — git workflow
- [AI workflow](ai-workflow/ai-coding-rules.md) — contributor and agent rules
