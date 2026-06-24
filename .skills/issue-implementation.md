# Issue Implementation

Implement a GitHub issue using this repository's engineering workflow.

## Objective

Deliver a focused, reviewable change that satisfies the issue's acceptance criteria and definition of done. Work in small, verifiable steps: understand → plan → implement → verify → document → open PR.

## Inputs

| Input | Required | Source |
|-------|----------|--------|
| GitHub issue | Yes | Issue number, URL, or pasted body |
| Acceptance criteria | Yes | From issue body |
| Harness requirements | Yes | From issue body and `docs/ai-workflow/harness-strategy.md` |
| Testing requirements | Yes | From issue body |
| Suggested branch name | Recommended | From issue body or `docs/branching-strategy.md` |
| Suggested PR title | Recommended | From issue body |

## Preconditions

Complete these checks before editing files:

1. **Read the full issue** — Problem, scope, out-of-scope, acceptance criteria, definition of done, harness, and testing sections.
2. **Load harness context** — At minimum:
   - `docs/vision.md`
   - `docs/branching-strategy.md`
   - `docs/ai-workflow/ai-coding-rules.md`
   - `docs/ai-workflow/harness-strategy.md`
3. **Confirm branch** — Create or checkout the suggested branch from the issue (or derive one per branching strategy).
4. **Confirm scope boundaries** — Note which directories and files are allowed. Stop if the issue asks for out-of-scope changes; request clarification or a new issue instead.
5. **Identify verification commands** — Determine which lint, test, and build commands apply to the touched areas.

## Planning workflow

1. **Summarize the task** — One paragraph: what will change and what will not.
2. **List deliverables** — Map each scope item to files or behaviors you will touch.
3. **Trace acceptance criteria** — For each criterion, note how you will prove it (test, manual step, diff inspection).
4. **Estimate diff size** — Prefer a PR reviewable in one sitting. Split work into follow-up issues if needed.
5. **State risks** — Migrations, breaking API changes, security-sensitive areas, or missing test coverage.
6. **Get alignment when ambiguous** — Ask the issue author or maintainer before implementing uncertain scope.

Present the plan to the human owner when:

- The issue spans multiple subsystems
- Requirements conflict with repository docs
- A design decision is not specified in the issue or `docs/`

## Implementation workflow

1. **Branch** — `git checkout -b <branch>` per issue suggestion or branching strategy.
2. **Minimal diffs** — Change only what the issue requires. Match existing code style and patterns.
3. **No secrets** — Never commit credentials, `.env` values, or tokens. Use environment variables and `.env.example` patterns.
4. **Incremental commits** — Commit logical units of work; avoid one giant commit unless the change is trivial.
5. **Respect out-of-scope** — Do not expand into refactors, unrelated fixes, or tool-specific config unless the issue includes them.
6. **Update generated artifacts** — When API contracts change, regenerate clients per project scripts (e.g. OpenAPI client generation).
7. **Self-review the diff** — Read `git diff` as if reviewing someone else's PR.

### Implementation principles

- Reuse existing abstractions; do not reimplement parallel patterns.
- Prefer focused changes over drive-by cleanup.
- Add comments only for non-obvious business or technical rationale.
- Keep error handling proportional to real failure modes.

## Testing workflow

Follow the issue's **Testing requirements** section first, then repository defaults.

### Typical verification by area

| Area | Commands / actions |
|------|-------------------|
| Backend | Project lint/format scripts; `backend` test suite |
| Frontend | `frontend` lint; unit tests; Playwright when UI behavior changes |
| Docs / skills | Markdown review; internal link check; `git diff` scope check |
| Full stack | `scripts/test.sh` or `scripts/test-local.sh` when both sides change |

### Testing checklist

- [ ] Run applicable automated tests and fix failures introduced by your change
- [ ] Perform manual steps listed in the issue
- [ ] Confirm acceptance criteria one-by-one
- [ ] Confirm `git diff` stays within allowed paths
- [ ] Re-run verification after addressing review feedback

## Documentation requirements

Update documentation when the change affects:

- Public API behavior or contracts
- Environment variables or deployment steps
- Contributor workflow or conventions
- Product scope reflected in `docs/vision.md` or `docs/roadmap.md`

For docs-only or skills-only issues:

- Use product-specific language from [docs/vision.md](../docs/vision.md) — not generic template copy in feature code or customized vision/roadmap
- Cross-link related docs and `.skills/` files
- Keep agent-agnostic terminology (no required vendor or IDE)

## Harness checks

Run harness checks **before** opening a PR and **after** each significant edit batch.

### Pre-merge harness checklist

- [ ] Issue acceptance criteria satisfied
- [ ] Issue definition of done satisfied
- [ ] `docs/ai-workflow/ai-coding-rules.md` pre-merge checklist completed
- [ ] Verification commands pass (lint, test, build as applicable)
- [ ] No files outside issue scope in the diff
- [ ] Prompt and outcome logged in `docs/ai-workflow/prompt-log.md` when the issue or harness strategy requires it
- [ ] CI is expected to pass on the PR (CI is the final harness for merged work)

### Feedforward reminder

Harness engineering means loading context and constraints **before** editing, not only running tests at the end. If verification fails, fix and re-run; do not open a PR with known failing checks unless the issue explicitly documents why.

## Output requirements

The implementation is complete when all of the following exist:

| Output | Requirement |
|--------|-------------|
| Code / docs changes | On the feature branch; minimal, focused diff |
| Passing verification | Issue-specified tests and harness commands |
| Git history | Clear commits with meaningful messages |
| Pull request | Opened against `main` (or per branching strategy) with complete summary |
| Issue linkage | PR description references the issue (`Fixes #N` or `Closes #N` when appropriate) |

Do not merge unless repository rules allow and required reviews are complete.

## Commit message guidance

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<optional scope>): <imperative summary>

<optional body — why, not just what>
```

| Type | Use for |
|------|---------|
| `feat` | New capability |
| `fix` | Bug fix |
| `docs` | Documentation or skills |
| `chore` | Maintenance, tooling |
| `test` | Tests only |
| `refactor` | Behavior-preserving refactor |

**Good examples:**

```
docs: add harness strategy for agent-agnostic workflows

feat(api): add resource creation endpoint

fix(auth): reject expired tokens in refresh flow
```

**Avoid:**

- `update stuff`, `fix bug`, `WIP`
- Committing secrets or generated local artifacts not tracked by the repo

Only commit when the user or issue workflow explicitly requests it. When committing, prefer focused commits over a single unrelated batch.

## PR summary guidance

Use this PR body template:

```markdown
## Summary

- [Bullet 1: primary outcome]
- [Bullet 2: notable constraint or decision]
- [Bullet 3: testing performed]

## Test plan

- [ ] [Verification step 1]
- [ ] [Verification step 2]

## Issue

Fixes #<issue-number>
```

### PR summary rules

- Lead with **why** and **outcome**, not a file list
- State what was intentionally **not** changed (when scope confusion is likely)
- Include commands run and their result (pass/fail)
- For docs/skills PRs, note agent-agnostic compliance and link check results
- Use the issue's **Suggested PR title** when provided

### Review readiness

- PR should be reviewable in one sitting when possible
- Respond to review comments with fixes or documented rationale; follow [pr-review-resolution.md](pr-review-resolution.md)
- Re-run harness checks after each revision

## Completion checklist

- [ ] All acceptance criteria met
- [ ] Definition of done met
- [ ] Harness checks pass
- [ ] PR opened with summary and test plan
- [ ] Issue linked from PR
- [ ] Prompt log updated if required
