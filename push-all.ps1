#requires -Version 5.1
<#
.SYNOPSIS
  Publishes each demo subfolder as its own public GitHub repo under the
  authenticated `gh` user.

.NOTES
  Requires: gh CLI authenticated (`gh auth login`) AND git installed.
  Idempotent: skips repos that already exist on GitHub.
#>

param(
  [string]$ReposFile = "repos.txt",
  [switch]$Private
)

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
  throw "gh CLI not found. Install from https://cli.github.com/"
}

# Confirm auth
gh auth status 1>$null 2>$null
if ($LASTEXITCODE -ne 0) {
  throw "Not authenticated. Run: gh auth login"
}

$visibility = if ($Private) { "--private" } else { "--public" }

Get-Content $ReposFile | ForEach-Object {
  $line = $_.Trim()
  if (-not $line -or $line.StartsWith("#")) { return }

  $parts = $line -split "\|", 2
  $repo  = $parts[0].Trim()
  $desc  = if ($parts.Count -gt 1) { $parts[1].Trim() } else { "" }

  # Special case: the index repo "ghcp-demos" lives at the script's own folder.
  if ($repo -eq "ghcp-demos") {
    $repoPath = $PSScriptRoot
  } else {
    $repoPath = Join-Path $PSScriptRoot $repo
    if (-not (Test-Path $repoPath)) { Write-Warning "Missing folder: $repo"; return }
  }

  Push-Location $repoPath
  try {
    if (-not (Test-Path ".git")) {
      git init -q -b main
      git add .
      git -c user.email="copilot@users.noreply.github.com" `
          -c user.name="GitHub Copilot Demo Bootstrapper" `
          commit -q -m "Initial commit"
    }

    # Create remote repo (skip if exists)
    $exists = gh repo view "$repo" 2>$null
    if ($LASTEXITCODE -ne 0) {
      Write-Host "Creating $repo on GitHub..."
      gh repo create $repo $visibility --description $desc --source=. --remote=origin --push
    } else {
      Write-Host "$repo already exists on GitHub — pushing latest commits."
      if (-not (git remote | Select-String -Quiet "^origin$")) {
        $user = gh api user --jq .login
        git remote add origin "https://github.com/$user/$repo.git"
      }
      git push -u origin main
    }
  } finally {
    Pop-Location
  }
}

Write-Host "`nDone."
