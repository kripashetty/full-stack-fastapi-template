# Issue Author

Create consistently structured GitHub issues for this repository.

## Objective

Produce a complete, reviewable GitHub issue that gives human contributors and coding agents enough context to plan, implement, verify, and merge work without ambiguity. Every issue should encode product intent, scope boundaries, acceptance criteria, and harness expectations **before** implementation begins.

## Inputs

Gather or infer the following before drafting:

| Input | Required | Notes |
|-------|----------|-------|
| Problem or opportunity | Yes | What is broken, missing, or worth building? |
| User story | Yes | Who benefits and what outcome do they get? |
| Business value | Recommended | Why now? What risk or velocity impact? |
| In-scope deliverables | Yes | Concrete paths, artifacts, or behaviors |
| Out-of-scope items | Yes | Explicit exclusions to prevent scope creep |
| Harness context | Recommended | Which docs should implementers load first? |
| Issue type | Recommended | `feature`, `fix`, `chore`, `docs`, etc. |

Load repository context when available:

- `docs/vision.md` — product goals and non-goals
- `docs/roadmap.md` — phase and priority
- `docs/branching-strategy.md` — branch and PR conventions
- `docs/ai-workflow/harness-strategy.md` — verification and agent workflow
- `docs/ai-workflow/ai-coding-rules.md` — editing and review rules

## Process

1. **Clarify intent** — Restate the problem in one paragraph. If intent is unclear, ask questions before writing the issue.
2. **Define scope** — List deliverables with paths or observable outcomes. Pair every scope item with at least one acceptance criterion.
3. **Draw boundaries** — Document out-of-scope work explicitly, especially adjacent features that might be mistaken as in scope.
4. **Specify verification** — Add harness/evaluation requirements and test requirements so implementers know how success is judged.
5. **Add workflow hints** — Suggest branch name and PR title to reduce friction at implementation time.
6. **Review for agent-agnostic language** — No single vendor or tool should be required to act on the issue.
7. **Publish** — Create or update the GitHub issue. Link related roadmap items or parent issues when applicable.

## Required sections

Use this section order in every issue body:

```markdown
## Problem statement

## User story

## Business value

## Scope

## Out of scope

## Acceptance criteria

## Definition of done

## Harness / evaluation requirements

## Testing requirements

## Suggested branch name

## Suggested PR title
```

### Section guidance

| Section | Purpose |
|---------|---------|
| **Problem statement** | Current pain, gap, or opportunity. Tie to product vision when relevant. |
| **User story** | `As a … I want … so that …` |
| **Business value** | Bullet list of alignment, velocity, risk, or learning outcomes |
| **Scope** | Table or bullet list of deliverables with paths |
| **Out of scope** | What this issue explicitly does **not** include |
| **Acceptance criteria** | Checklist of verifiable conditions for merge |
| **Definition of done** | Broader completion signals beyond individual criteria |
| **Harness / evaluation requirements** | Context to load, commands to run, logging expectations |
| **Testing requirements** | Automated and manual verification steps |
| **Suggested branch name** | Per `docs/branching-strategy.md` |
| **Suggested PR title** | Conventional, scannable title for the implementing PR |

## Acceptance criteria generation

Write acceptance criteria that are **specific, testable, and bounded**.

### Rules

- Use checkbox format: `- [ ] …`
- One criterion per observable outcome; avoid bundling unrelated checks
- Include file paths, commands, or behaviors where possible
- Cover happy path and important guardrails (e.g. "no changes under `backend/`")
- Group related criteria under subheadings when the issue has multiple deliverable areas

### Template

```markdown
## Acceptance criteria

### [Deliverable area]

- [ ] [Artifact or behavior] — [how to verify]
- [ ] [Artifact or behavior] — [how to verify]

### Repository constraints

- [ ] PR diff contains only files under [allowed paths]
- [ ] No secrets, credentials, or environment-specific values committed
```

### Anti-patterns

- Vague criteria: "works correctly", "is well documented"
- Missing verification method: "add tests" without naming what tests must prove
- Criteria that duplicate the entire scope section without adding verifiability

## Test requirements

Distinguish automated tests from manual verification.

```markdown
## Testing requirements

- Automated: [test commands, suites, or "none — docs-only"]
- Manual:
  - [ ] [Step a human or agent performs]
  - [ ] [Expected result]
```

Align test requirements with the repository stack:

- Backend: `backend` test suite per project scripts
- Frontend: unit/Playwright tests when UI changes
- Docs/skills only: link checking, markdown review, `git diff` scope check

## Harness / evaluation requirements

Feedforward guidance implementers must follow **before and after** editing.

Include:

1. **Context to load** — Which `docs/` and `.skills/` files to read first
2. **Pre-edit checks** — Confirm issue scope, branch, and out-of-scope boundaries
3. **Post-edit verification** — Commands or manual steps (lint, test, diff review)
4. **Logging** — Whether to append to `docs/ai-workflow/prompt-log.md`
5. **Review bar** — PR size, single-sitting review, harness doc compliance

Example:

```markdown
## Harness / evaluation requirements

- Load `docs/vision.md`, `docs/branching-strategy.md`, and `docs/ai-workflow/ai-coding-rules.md` before editing
- Follow `.skills/issue-implementation.md` when implementing this issue
- After changes: run [verification commands] and confirm `git diff` scope
- Log prompt and outcome in `docs/ai-workflow/prompt-log.md`
```

## Suggested branch naming

Follow `docs/branching-strategy.md`. Default patterns:

| Type | Pattern | Example |
|------|---------|---------|
| Feature | `feature/<short-description>` | `feature/user-onboarding` |
| Fix | `fix/<short-description>` | `fix/token-refresh` |
| Chore / docs | `chore/<short-description>` | `chore/project-setup` |

Use lowercase kebab-case. Keep names short but recognizable in `git branch` output.

## Suggested PR title generation

Use [Conventional Commits](https://www.conventionalcommits.org/) style:

```
<type>(<optional scope>): <imperative summary>
```

| Type | When |
|------|------|
| `feat` | New user-facing capability |
| `fix` | Bug fix |
| `docs` | Documentation or skills only |
| `chore` | Tooling, config, non-user-facing maintenance |
| `refactor` | Behavior-preserving code change |
| `test` | Test-only changes |

**Examples:**

- `docs: establish project foundation and harness templates`
- `feat(api): add resource upload endpoint`
- `fix(auth): handle expired refresh tokens`

The PR title should match the issue outcome, not the issue number alone.

## Quality checklist

Before publishing, confirm:

- [ ] Problem, scope, and out-of-scope are aligned
- [ ] Every scope item maps to at least one acceptance criterion
- [ ] Harness and testing requirements are actionable without a specific AI product
- [ ] Branch name and PR title follow repository conventions
- [ ] Language is agent-agnostic (no required vendor or IDE)
