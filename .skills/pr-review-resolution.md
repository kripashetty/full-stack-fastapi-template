# PR Review Resolution

Address pull request review feedback and return the branch to merge-ready state.

## Objective

Resolve unresolved review comments with minimal, focused changes. Produce a clear comment-by-comment resolution summary so reviewers can re-approve without re-discovering context.

## Inputs

| Input | Required | Source |
|-------|----------|--------|
| Pull request | Yes | PR number, URL, title, description, linked issue |
| Review comments | Yes | Inline review threads, general PR comments, bot findings (CI, lint, security) |
| Repository state | Yes | Branch checked out, latest remote fetched, current `git diff` |
| Original issue | Recommended | Linked `Fixes #N` issue for scope boundaries |
| Harness context | Recommended | `docs/ai-workflow/ai-coding-rules.md`, `docs/ai-workflow/harness-strategy.md` |

## Preconditions

Before resolving comments:

1. **Checkout the PR branch** — `git fetch origin && git checkout <branch>`
2. **Sync with base if needed** — Rebase or merge `main` when the PR is behind and conflicts block review
3. **Read the full PR** — Description, test plan, and linked issue (if any)
4. **Load review context** — All open/unresolved threads; distinguish **must-fix** from **nit** / **optional**
5. **Confirm scope** — Fixes should address review feedback; do not expand into unrelated features

## Process

### 1. Collect unresolved comments

Gather every item that still needs action:

| Source | Include |
|--------|---------|
| Inline review threads | Unresolved conversations on specific lines |
| General PR comments | Top-level feedback not tied to a line |
| Bot / CI checks | Failing workflows, lint, type errors, test failures |
| Requested changes | Reviews explicitly marked "Changes requested" |

For each item, capture:

- Comment ID or permalink (when available)
- Author and severity (blocker, suggestion, question)
- File and line reference
- Whether the thread is marked resolved

Skip threads already resolved unless the fix was incomplete.

### 2. Group related comments

Cluster comments that share a root cause or touch the same area:

| Group type | Example |
|------------|---------|
| **Same file / concern** | Three nits in `crud.py` about error handling |
| **Same theme** | Missing tests for a new endpoint |
| **Duplicate** | Same CI failure reported in multiple comments |
| **Conflict** | Two reviewers disagree — flag for human decision |

Grouped work reduces churn and helps produce one fix per theme instead of scattered edits.

### 3. Explain requested changes

Before editing, write a short plan (for yourself or the PR author):

```markdown
## Review resolution plan

### Group: [theme]

**Comments:** [links or IDs]
**Reviewer intent:** [plain-language summary]
**Proposed fix:** [what will change]
**Tests:** [new/updated tests or N/A]
**Out of scope:** [what you will NOT do in this pass]
```

**When to ask instead of implement:**

- Comment conflicts with linked issue scope
- Suggestion requires architectural decision not documented in `docs/`
- Fix would substantially expand PR beyond original intent
- Security or behavior change needs explicit human approval

### 4. Implement fixes

Apply changes per [AI coding rules](../docs/ai-workflow/ai-coding-rules.md):

- **One theme at a time** — Complete a group, verify, then move on
- **Minimal diffs** — Address the comment; avoid drive-by refactors
- **Match patterns** — Follow existing conventions in touched files
- **Resolve questions in thread** — Reply on the PR when clarification is part of the fix
- **Do not resolve threads prematurely** — Mark resolved only after the fix is pushed

For nit-only comments: fix if trivial; otherwise reply with rationale or offer a follow-up issue.

### 5. Add or update tests

When review feedback implies behavior change or missing coverage:

| Area | Action |
|------|--------|
| Backend logic | Add/update tests under `backend/tests/` |
| API contracts | Update route tests; regenerate OpenAPI client if response shape changes |
| Frontend behavior | Update unit tests; Playwright when user flows change |
| Docs / skills only | Update manual verification steps; link check if paths changed |

If a comment requests tests you believe are unnecessary, reply explaining why — do not silently skip.

### 6. Verify no regressions

Run verification for all touched areas (see [harness strategy](../docs/ai-workflow/harness-strategy.md)):

| Change type | Verification |
|-------------|--------------|
| Backend | `backend/scripts/lint.sh`; backend test suite |
| Frontend | Biome lint; unit tests; Playwright when UI changes |
| Docs / skills | Markdown review; relative link check; `git diff` scope |
| Full stack | `scripts/test.sh` or `scripts/test-local.sh` |

**Checklist:**

- [ ] All previously passing tests still pass
- [ ] New tests cover the reviewed behavior
- [ ] CI checks expected to pass on push
- [ ] `git diff` contains only changes required by review (no unrelated files)
- [ ] No secrets or credentials introduced

Re-run verification after each significant fix batch.

### 7. Summarize resolutions

Produce the output below before requesting re-review. Post the summary as a PR comment or include it in the final reply to reviewers.

## Output

### Files changed

List paths modified in this resolution pass:

```markdown
## Files changed

- `path/to/file.py` — [one-line reason]
- `path/to/test.py` — [one-line reason]
```

### Tests run

Document what was executed and the result:

```markdown
## Tests run

| Command | Result |
|---------|--------|
| `backend/scripts/lint.sh` | pass / fail |
| `backend` test suite | pass / fail / N/A |
| Playwright (if UI) | pass / fail / N/A |
| Manual: [step] | pass / fail |
```

### Comment-by-comment resolution summary

Use this table for every unresolved comment addressed (or explicitly deferred):

```markdown
## Resolution summary

| # | Comment | Resolution | Status |
|---|---------|------------|--------|
| 1 | [Quote or paraphrase] — @reviewer, `file:line` | [What you did, or why deferred] | Fixed / Deferred / Won't fix (with reason) |
| 2 | … | … | … |
```

**Status values:**

- **Fixed** — Change pushed; thread can be resolved
- **Deferred** — Valid but out of scope; follow-up issue linked
- **Won't fix** — Disagree with rationale documented for reviewer
- **Needs author** — Blocked on human decision; question posted in thread

### Optional: commit and push guidance

```
fix(reviews): address PR feedback on [short topic]

- [bullet: what changed]
- [bullet: tests added/updated]
```

Push to the PR branch; do not force-push to shared branches unless coordinated. Request re-review when all **must-fix** items are **Fixed** or explicitly agreed **Won't fix**.

## Anti-patterns

| Anti-pattern | Instead |
|--------------|---------|
| Fix comments without reading linked issue | Confirm fixes stay within original PR scope |
| Giant refactor while addressing nits | Minimal change per comment group |
| Resolve GitHub threads before pushing | Push first, then resolve when CI is green |
| Ignore bot failures | Treat CI failures as review comments |
| Batch reply without per-comment mapping | Use the resolution summary table |

## Related

- [Issue implementation](issue-implementation.md) — original PR workflow
- [AI coding rules](../docs/ai-workflow/ai-coding-rules.md) — diff and review standards
- [Harness strategy](../docs/ai-workflow/harness-strategy.md) — verification commands
- [Branching strategy](../docs/branching-strategy.md) — branch and PR conventions
