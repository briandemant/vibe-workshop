# Stage 06 - Interactive `/create-issue` Command

## Goal

Add a project-local `/create-issue` slash command that collaborates with the user to shape an issue, confirms final intent, and creates a labeled GitHub issue.

## Context

- Related files: `.opencode/command/create-issue.md`, `.opencode/skill/create-command/SKILL.md`
- Stage requirement highlights:
  - Command starts by asking for a brief task/bug explanation.
  - Command spars with the user, gives useful pushback, and clarifies scope.
  - Sparring explicitly checks whether tests should be added.
  - Sparring explicitly checks whether documentation needs updates.
  - Command asks for agreement before creating the issue.
  - Command creates a GitHub issue using one label: `feature`, `spike`, or `bug`.

## Approach

Create a focused command prompt that enforces a conversational flow: gather context, refine with pushback, confirm scope and label, then execute `gh issue create` and report the URL. Keep behavior deterministic by requiring explicit user confirmation before issue creation.

## Steps

- [ ] Create `.opencode/command/create-issue.md` with required frontmatter and task prompt.
- [ ] Define interaction flow in the prompt:
  - [ ] Ask for a brief problem/request summary.
  - [ ] Ask clarifying questions and provide useful pushback when scope is vague.
  - [ ] Ask whether tests are needed, and capture expected test coverage.
  - [ ] Ask whether documentation updates are needed.
  - [ ] Propose issue title/body/label and ask for explicit agreement.
- [ ] Implement issue creation behavior using `gh issue create` after confirmation.
- [ ] Restrict labels to one of `feature`, `spike`, `bug` and confirm the selected label with the user.
- [ ] Ensure final output includes created issue URL and short recap.
- [ ] Run verification:
  - [ ] Dry-run command interaction with a sample feature request.
  - [ ] Dry-run command interaction with a sample bug report.

## Out of Scope

- Automatically creating missing labels in GitHub
- Bulk issue creation from files or plans
- Auto-assignment, milestones, or project board automation

## Open Questions

- Should `$ARGUMENTS` pre-seed the initial summary when provided, or should the command always start by asking from scratch?
