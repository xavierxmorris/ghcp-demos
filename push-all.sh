#!/usr/bin/env bash
# Publish independent demos, enforcing name|description[|public or private].
# --private changes default creation visibility; explicit private entries always stay private.

set -euo pipefail
cd "$(dirname "$0")"

VIS="--public"
if [[ $# -gt 1 || ( $# -eq 1 && "$1" != "--private" ) ]]; then
  echo "Usage: ./push-all.sh [--private]" >&2
  exit 2
fi
if [[ "${1:-}" == "--private" ]]; then VIS="--private"; fi
if [[ "${GH_HOST:-github.com}" != "github.com" ]]; then
  echo "This inventory publishes to github.com; a different GH_HOST is not accepted." >&2
  exit 1
fi

command -v gh >/dev/null 2>&1 || { echo "gh CLI not found." >&2; exit 1; }
command -v git >/dev/null 2>&1 || { echo "git not found." >&2; exit 1; }
gh auth status
owner="$(gh api user --jq .login)"
if [[ ! "$owner" =~ ^[A-Za-z0-9][A-Za-z0-9-]*$ ]]; then
  echo "Invalid authenticated GitHub account." >&2
  exit 1
fi
# A failed metadata request is not evidence that a repository is absent.
metadata="$(gh api --paginate 'user/repos?affiliation=owner&per_page=100' \
  --jq '.[] | [.full_name, .visibility] | @tsv')"
while IFS=$'\t' read -r full_name repo_visibility extra; do
  [[ -z "$full_name" && -z "${repo_visibility:-}" && -z "${extra:-}" ]] && continue
  if [[ -n "${extra:-}" || ( "$repo_visibility" != "PRIVATE" && "$repo_visibility" != "PUBLIC" && "$repo_visibility" != "private" && "$repo_visibility" != "public" ) ]]; then
    echo "Cannot establish owned-repository visibility. Publication stopped." >&2
    exit 1
  fi
done <<< "$metadata"

trim() {
  local value="$1"
  value="${value#"${value%%[![:space:]]*}"}"
  value="${value%"${value##*[![:space:]]}"}"
  printf '%s' "$value"
}

while IFS= read -r line || [[ -n "$line" ]]; do
  line="$(trim "$line")"
  [[ -z "$line" || "$line" == \#* ]] && continue
  pipes="${line//[!|]/}"
  if [[ ${#pipes} -lt 1 || ${#pipes} -gt 2 ]]; then
    echo "Expected name|description[|public or private]." >&2
    exit 2
  fi
  IFS='|' read -r repo desc declared <<< "$line"
  repo="$(trim "$repo")"
  desc="$(trim "${desc:-}")"
  declared="$(trim "${declared:-}")"
  if [[ -z "$desc" || ( ${#pipes} -eq 2 && "$declared" != "public" && "$declared" != "private" ) ]]; then
    echo "A description and valid public/private visibility are required." >&2
    exit 2
  fi
  if [[ "$repo" != "ghcp-demos" && ! "$repo" =~ ^ghcp-demo-[0-9]{2}-[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
    echo "Invalid repository name in publishing inventory." >&2
    exit 2
  fi
  if [[ "$repo" == "ghcp-demos" ]]; then
    repo_path="."
  else
    repo_path="$repo"
    [[ ! -d "$repo_path" ]] && { echo "Missing folder, not published: $repo"; continue; }
  fi
  visibility="$VIS"
  if [[ "$declared" == "private" ]]; then visibility="--private"; fi
  target="$owner/$repo"
  known="$(printf '%s\n' "$metadata" | awk -F '\t' -v target="$target" '$1 == target { print $2 }')"
  if [[ -z "$known" ]]; then
    echo "Creating $target $visibility (no content pushed yet)..."
    gh repo create "$target" "$visibility" --description "$desc"
  fi
  actual="$(gh repo view "$target" --json visibility --jq .visibility)"
  if [[ "$declared" == "private" && "$actual" != "PRIVATE" ]]; then
    echo "Refusing to publish private inventory entry $target to a non-private target." >&2
    exit 1
  fi
  if [[ "$actual" != "PRIVATE" && "$actual" != "PUBLIC" ]]; then
    echo "Unexpected target visibility." >&2
    exit 1
  fi

  pushd "$repo_path" >/dev/null
  if [[ ! -e .git ]]; then
    git init -q -b main
    git add .
    git -c user.email="copilot@users.noreply.github.com" \
        -c user.name="GitHub Copilot Demo Bootstrapper" \
        commit -q -m "Initial commit" -m \
        "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
  fi
  remotes="$(git remote)"
  if ! printf '%s\n' "$remotes" | grep -qx origin; then
    git remote add origin "https://github.com/$target.git"
  fi
  push_url="$(git remote get-url --push --all origin)"
  case "$push_url" in
    "https://github.com/$target.git"|"https://github.com/$target"|"git@github.com:$target.git"|"ssh://git@github.com/$target.git") ;;
    *) echo "Origin push URL does not match the visibility-checked target $target." >&2; exit 1 ;;
  esac
  echo "Pushing $target ($actual)..."
  git push -u origin main
  popd >/dev/null
done < repos.txt

echo
echo "Done. Missing folders, if reported, were not published."
