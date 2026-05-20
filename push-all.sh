#!/usr/bin/env bash
# Publishes each demo subfolder as its own public GitHub repo under the
# authenticated `gh` user. Idempotent — re-runs only push new commits.
#
# Usage:
#   ./push-all.sh            # public repos
#   ./push-all.sh --private  # private repos

set -euo pipefail
cd "$(dirname "$0")"

VIS="--public"
[[ "${1:-}" == "--private" ]] && VIS="--private"

command -v gh >/dev/null 2>&1 || { echo "gh CLI not found." >&2; exit 1; }
gh auth status >/dev/null 2>&1 || { echo "Run 'gh auth login' first." >&2; exit 1; }

while IFS='|' read -r repo desc; do
  repo="$(echo "$repo" | xargs)"
  desc="$(echo "${desc:-}" | xargs)"
  [[ -z "$repo" || "$repo" == \#* ]] && continue

  # Special case: the index repo "ghcp-demos" is this script's own folder.
  if [[ "$repo" == "ghcp-demos" ]]; then
    repo_path="."
  else
    repo_path="$repo"
    [[ ! -d "$repo_path" ]] && { echo "Missing folder: $repo"; continue; }
  fi

  pushd "$repo_path" >/dev/null
  if [[ ! -d .git ]]; then
    git init -q -b main
    git add .
    git -c user.email="copilot@users.noreply.github.com" \
        -c user.name="GitHub Copilot Demo Bootstrapper" \
        commit -q -m "Initial commit"
  fi

  if gh repo view "$repo" >/dev/null 2>&1; then
    echo "$repo exists — pushing latest commits."
    git remote get-url origin >/dev/null 2>&1 || \
      git remote add origin "https://github.com/$(gh api user --jq .login)/$repo.git"
    git push -u origin main
  else
    echo "Creating $repo..."
    gh repo create "$repo" $VIS --description "$desc" --source=. --remote=origin --push
  fi
  popd >/dev/null
done < repos.txt

echo
echo "Done."
