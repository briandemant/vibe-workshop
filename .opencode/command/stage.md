---
description: Create the next workshop stage branch from current HEAD and push it.
agent: build
---

Create the next workshop stage branch.

1. Run `git rev-parse --abbrev-ref HEAD` to detect the current branch.
2. Determine the target stage branch name:
   - If `$ARGUMENTS` is provided, treat it as an explicit stage value and normalize it to `stage-NN`.
     - Examples: `05` -> `stage-05`, `stage-7` -> `stage-07`, `stage-12` -> `stage-12`.
   - If `$ARGUMENTS` is empty and current branch is `main`, target is `stage-01`.
   - If `$ARGUMENTS` is empty and current branch matches `stage-NN`, target is the next number with two-digit zero padding.
   - Otherwise, ask the user which stage name to create and stop.
3. Run `git status --porcelain`.
   - If output is not empty, ask the user if the current changes should be committed before branching.
   - If yes, ask for a commit message (default suggestion: `Complete <current-branch>`), then run `git add -A` and `git commit -m "<message>"`.
   - If no, stop and let the user decide how to proceed.
4. Create and switch to the branch from current HEAD with `git checkout -b <target-branch>`.
5. Push and set upstream with `git push -u origin <target-branch>`.
6. Report the created branch name and upstream tracking branch.
