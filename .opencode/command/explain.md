---
description: Plan the current stage with the user, update WORKSHOP.md, write STAGE.md, and create a solution branch.
agent: build
---

Plan the current workshop stage with the user and produce student-facing stage materials.

1. Run `git rev-parse --abbrev-ref HEAD` to detect the current branch (`<stage-branch>`).
2. If `<stage-branch>` does not match `stage-NN`, ask the user whether to continue anyway or stop.
3. Use `$ARGUMENTS` (if provided) as a topic seed for planning.
4. Plan interactively with the user until they confirm the stage write-up is complete.
   - Keep it student-facing.
   - No solution spoilers.
   - This is freeform; do not force a rigid template.
5. Run `git status --porcelain`.
   - If there are unrelated working tree changes, ask how to proceed and stop if unclear.
6. Capture two outputs from the planning chat:
   - A short stage title for the workshop index.
   - The full student-facing `STAGE.md` content.
7. Update `WORKSHOP.md` on `main`:
   - `git checkout main`
   - Ensure there is a `## Stages` section.
   - Insert or update one line for this stage in ascending stage order:
     - `- **<stage-branch>**: <stage-title>`
   - If the stage already exists, replace its line in place.
   - `git add WORKSHOP.md`
   - `git commit -m "Update workshop index for <stage-branch>"`
   - `git push origin main`
8. Return to the stage branch and rebase:
   - `git checkout <stage-branch>`
   - `git rebase main`
   - If conflicts occur, stop and ask the user to resolve them.
9. Write `STAGE.md` at the repo root using the agreed student-facing content.
   - Do not read existing `STAGE.md`.
   - Overwrite `STAGE.md`.
10. Commit and publish stage content:
   - `git add STAGE.md`
   - `git commit -m "Update STAGE.md for <stage-branch>"`
   - `git push --force-with-lease origin <stage-branch>`
11. Create the solution branch from the rebased and committed stage branch:
   - Target name: `<stage-branch>-solution`
   - If it already exists locally or on `origin`, stop and report.
   - `git checkout -b <stage-branch>-solution`
   - `git push -u origin <stage-branch>-solution`
12. Report clearly:
   - `WORKSHOP.md` updated on `main`.
   - `STAGE.md` updated on `<stage-branch>`.
   - `<stage-branch>-solution` created and pushed.
