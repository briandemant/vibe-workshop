---
description: Collaboratively refine and create a labeled GitHub issue.
agent: build
---

Create a GitHub issue through an interactive conversation.

1. Start by gathering a brief summary:
   - If `$ARGUMENTS` is non-empty, treat it as the initial summary and confirm it with the user.
   - If `$ARGUMENTS` is empty, ask the user for a brief explanation of the task or bug.
2. Spar with the user to refine the issue:
   - Ask clarifying questions.
   - Give useful pushback when scope is vague, too broad, or missing constraints.
   - Ask whether tests are needed and what test coverage is expected.
   - Ask whether documentation needs to be updated.
3. Propose a draft issue with:
   - A concise title.
   - A single label: `feature`, `spike`, or `bug`.
   - A body that starts with this template core:

```md
**In order** to <outcome>
**We need to** <change>

<details>

**Acceptance Criteria:**

<acceptance criteria>

**Documentation:**

<documentation updates>

**Testing:**

<testing approach>
```

   - Keep `In order` and `We need to` always.
   - Include `Acceptance Criteria`, `Documentation`, and `Testing` only when relevant.
   - If a section is not relevant, omit the section entirely (do not leave placeholders like `N/A`).

4. Ask for explicit agreement before creating anything:
   - Example: "Do we agree on this issue draft and label?"
   - If the user does not agree, revise and ask again.
5. Only after agreement, create the issue with `gh issue create`:
   - Use the agreed title.
   - Use exactly one agreed label from `feature`, `spike`, `bug`.
   - Use the agreed body with only relevant sections.
6. Report the result:
   - Return issue number and URL.
   - Include a short recap of the confirmed label, testing notes, and documentation notes.

Important guardrails:

- Never create the issue before explicit user agreement.
- Never use a label outside `feature`, `spike`, `bug`.
- If label selection is ambiguous, ask the user to choose.
