# Prompt Log

Audit trail for significant AI-assisted and harness-engineering sessions on the Engineering Design Review Assistant.

## When to log

| Event | Log? |
|-------|------|
| Foundation / milestone issues (e.g. Issue #1) | Yes |
| New reusable pattern documented in `docs/` or `.skills/` | Yes |
| Failed agent approach worth avoiding later | Yes |
| Routine one-line fixes | No |
| Security-sensitive debugging | Redact secrets; log approach only |

## How to log

Append a new entry at the **top** of the **Log** section (newest first). Use the template below. Do not include API keys, tokens, or `.env` contents.

## Entry template

```markdown
### YYYY-MM-DD — <short title>

- **Issue / PR:** #N or link
- **Tool:** IDE-based assistant | CLI-based assistant | manual (+ optional product name as example)
- **Objective:** One sentence
- **Context loaded:** List docs/skills read
- **Prompt summary:** What was asked (paraphrase; no secrets)
- **Outcome:** Shipped / partial / abandoned
- **Verification:** Commands run or manual checks
- **Lessons:** What to repeat or avoid
```

## Log

### 2026-06-23 — Project foundation (Issue #1)

- **Issue / PR:** [Issue #1](https://github.com/kripashetty/full-stack-fastapi-template/issues/1)
- **Tool:** Coding agent (agentic workflow)
- **Objective:** Establish `docs/` foundation and `.skills/` reusable workflows before application code changes.
- **Context loaded:** Issue #1 body, `.skills/issue-author.md`, `.skills/issue-implementation.md`, upstream CONTRIBUTING.md
- **Prompt summary:** Implement Issue #1 per repository workflow — vision, roadmap, branching, AI rules, harness strategy, prompt log, and agent-agnostic skills; docs/skills only.
- **Outcome:** Shipped (pending PR)
- **Verification:** Manual review of markdown; `git diff` scoped to `docs/` and `.skills/`; link paths checked against file layout
- **Lessons:** Centralizing issue author/implementation in `.skills/` keeps CLI and IDE agents aligned without tool-specific config.

## Related

- [Harness strategy](harness-strategy.md)
- [AI coding rules](ai-coding-rules.md)
- [Issue implementation skill](../../.skills/issue-implementation.md)
