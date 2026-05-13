#!/usr/bin/env bash

set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  link_branch_to_issue.sh --issue <number|issue-url> [--branch <name> ...] [--repo <owner/name>] [--remote <name>]

Examples:
  link_branch_to_issue.sh --issue 1 --branch stage-07
  link_branch_to_issue.sh --issue https://github.com/owner/repo/issues/12 --branch stage-07 --branch stage-07-solution
  link_branch_to_issue.sh --issue 1

Notes:
  - If no --branch is provided, the current branch is used.
  - Branches must already exist on the remote.
  - Linking uses a temporary remote rename workflow:
    <branch> -> <branch>-tmp-<random> -> create linked <branch> -> delete temp.
EOF
}

is_branch_linked() {
  local issue_number="$1"
  local repo="$2"
  local branch="$3"
  local listed
  listed="$(gh issue develop --list "$issue_number" --repo "$repo" 2>/dev/null || true)"

  while IFS=$'\t' read -r linked_branch _; do
    if [[ "$linked_branch" == "$branch" ]]; then
      return 0
    fi
  done <<< "$listed"

  return 1
}

remote_branch_exists() {
  local remote="$1"
  local branch="$2"
  local line
  line="$(git ls-remote "$remote" "refs/heads/$branch" || true)"
  [[ -n "$line" ]]
}

build_tmp_branch_name() {
  local branch="$1"
  local candidate

  while true; do
    candidate="${branch}-tmp-${RANDOM}${RANDOM}"
    if [[ ${#candidate} -gt 255 ]]; then
      candidate="${branch:0:220}-tmp-${RANDOM}${RANDOM}"
    fi
    if ! remote_branch_exists "$REMOTE" "$candidate"; then
      printf '%s\n' "$candidate"
      return
    fi
  done
}

die() {
  printf 'Error: %s\n' "$1" >&2
  exit "${2:-1}"
}

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || die "Missing required command: $1" 2
}

parse_issue_number() {
  local raw="$1"
  if [[ "$raw" =~ ^[0-9]+$ ]]; then
    printf '%s\n' "$raw"
    return
  fi

  if [[ "$raw" =~ /issues/([0-9]+)/?$ ]]; then
    printf '%s\n' "${BASH_REMATCH[1]}"
    return
  fi

  die "--issue must be an issue number or issue URL" 1
}

require_cmd git
require_cmd gh

ISSUE_RAW=""
REPO=""
REMOTE="origin"
BRANCHES=()

while (($# > 0)); do
  case "$1" in
    --issue)
      [[ $# -ge 2 ]] || die "--issue requires a value" 1
      ISSUE_RAW="$2"
      shift 2
      ;;
    --branch)
      [[ $# -ge 2 ]] || die "--branch requires a value" 1
      BRANCHES+=("$2")
      shift 2
      ;;
    --repo)
      [[ $# -ge 2 ]] || die "--repo requires a value" 1
      REPO="$2"
      shift 2
      ;;
    --remote)
      [[ $# -ge 2 ]] || die "--remote requires a value" 1
      REMOTE="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      die "Unknown argument: $1" 1
      ;;
  esac
done

[[ -n "$ISSUE_RAW" ]] || die "--issue is required" 1

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  die "Must be run inside a git repository" 2
fi

gh auth status >/dev/null 2>&1 || die "gh is not authenticated; run: gh auth login" 2

if [[ -z "$REPO" ]]; then
  REPO="$(gh repo view --json nameWithOwner --jq '.nameWithOwner')"
fi

if [[ ${#BRANCHES[@]} -eq 0 ]]; then
  BRANCHES+=("$(git rev-parse --abbrev-ref HEAD)")
fi

ISSUE_NUMBER="$(parse_issue_number "$ISSUE_RAW")"

ISSUE_STATE="$(gh issue view "$ISSUE_NUMBER" --repo "$REPO" --json state --jq '.state' 2>/dev/null || true)"
[[ -n "$ISSUE_STATE" ]] || die "Issue #$ISSUE_NUMBER not found in $REPO" 2
if [[ "$ISSUE_STATE" != "OPEN" ]]; then
  die "Issue #$ISSUE_NUMBER is $ISSUE_STATE; only OPEN issues are supported" 2
fi

for branch in "${BRANCHES[@]}"; do
  [[ -n "$branch" ]] || die "Branch name cannot be empty" 1

  if is_branch_linked "$ISSUE_NUMBER" "$REPO" "$branch"; then
    printf 'Already linked: %s\n' "$branch"
    continue
  fi

  REMOTE_REF="refs/heads/$branch"
  SHA_LINE="$(git ls-remote "$REMOTE" "$REMOTE_REF" || true)"
  [[ -n "$SHA_LINE" ]] || die "Branch '$branch' was not found on remote '$REMOTE'" 2
  SHA="${SHA_LINE%%[[:space:]]*}"

  TMP_BRANCH="$(build_tmp_branch_name "$branch")"
  printf 'Applying rename workflow for %s (%s)\n' "$branch" "$TMP_BRANCH"

  git push "$REMOTE" "$SHA:refs/heads/$TMP_BRANCH" >/dev/null

  if ! git push "$REMOTE" ":refs/heads/$branch" >/dev/null; then
    git push "$REMOTE" ":refs/heads/$TMP_BRANCH" >/dev/null || true
    die "Failed to remove original remote branch '$branch'" 3
  fi

  if ! gh issue develop "$ISSUE_NUMBER" --repo "$REPO" --name "$branch" --base "$TMP_BRANCH" >/dev/null; then
    git push "$REMOTE" "$SHA:refs/heads/$branch" >/dev/null || true
    git push "$REMOTE" ":refs/heads/$TMP_BRANCH" >/dev/null || true
    die "Failed to create issue-linked branch '$branch' from '$TMP_BRANCH'" 3
  fi

  if ! is_branch_linked "$ISSUE_NUMBER" "$REPO" "$branch"; then
    git push "$REMOTE" "$SHA:refs/heads/$branch" >/dev/null || true
    git push "$REMOTE" ":refs/heads/$TMP_BRANCH" >/dev/null || true
    die "GitHub did not link '$branch' after rename workflow" 3
  fi

  git push "$REMOTE" ":refs/heads/$TMP_BRANCH" >/dev/null || true
  printf 'Linked via rename workflow: %s\n' "$branch"
done

printf '\nLinked branches for issue #%s:\n' "$ISSUE_NUMBER"
gh issue develop --list "$ISSUE_NUMBER" --repo "$REPO"
