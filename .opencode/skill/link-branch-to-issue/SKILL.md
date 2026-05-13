---
name: link-branch-to-issue
description: Link one or more existing remote branches to a GitHub issue.
allowed-tools:
  - bash
  - read
---

# link-branch-to-issue

Use this skill when you need to associate existing development branches with a GitHub issue.

## When to use

- The issue already exists and work is being done on one or more branches.
- You need the issue's Development section to show those branches.
- You want an idempotent command that skips branches already linked.

## Workflow

1. Confirm the target issue number and branch names with the user.
2. Run:

   `./.opencode/skill/link-branch-to-issue/link_branch_to_issue.sh --issue <issue-number> --branch <branch-name>`

   You can repeat `--branch` to link multiple branches in one invocation.

3. If no branch is provided, the script links the current git branch.
4. Share the final linked-branch list from the script output.

## Constraints

- The script only links existing remote branches; it does not create branches.
- The script does not auto-push local branches.
- The script requires `gh` authentication and repo access.
- Use this workflow instead of manual GraphQL calls.
