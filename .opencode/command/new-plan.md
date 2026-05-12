---
description: Create a new plan file from plans/TEMPLATE.md.
agent: build
---

Create a new plan document using `plans/TEMPLATE.md` as the structure.

- Treat `$ARGUMENTS` as the plan title.
- Generate a kebab-case slug from the title.
- Create the file at `plans/<slug>.md`.
- Set the first heading to the original title.
- Keep the rest of the template sections intact.

If `$ARGUMENTS` is empty, ask for a title and stop.
