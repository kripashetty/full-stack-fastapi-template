# Prompt Log (Template)

> **Use this file** to record significant AI-assisted and harness-engineering sessions. The logging process is project-agnostic; entries describe work on *your* product (see [vision](../vision.md)).

## When to log

| Event | Log? |
|-------|------|
| Foundation / milestone issues | Yes |
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

### YYYY-MM-DD — <example: project foundation>

- **Issue / PR:** _[#N or link]_
- **Tool:** _[e.g. coding agent, CLI-based assistant, manual]_
- **Objective:** _[e.g. Establish docs/ and .skills/ before feature work]_
- **Context loaded:** _[e.g. issue body, .skills/issue-implementation.md]_
- **Prompt summary:** _[Paraphrase; no secrets]_
- **Outcome:** _[Shipped / partial / abandoned]_
- **Verification:** _[e.g. link check, git diff scope, test commands]_
- **Lessons:** _[What to repeat or avoid]_

## Related

- [Harness strategy](harness-strategy.md)
- [AI coding rules](ai-coding-rules.md)
- [Issue implementation skill](../../.skills/issue-implementation.md)
