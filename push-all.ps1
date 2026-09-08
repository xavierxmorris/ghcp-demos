#requires -Version 5.1
<#
.SYNOPSIS
  Publishes independent demos, enforcing per-entry private visibility.
.NOTES
  Requires authenticated gh and git. Review staged content and account first.
  repos.txt supports name|description[|public or private].
  Private entries cannot be recreated publicly or pushed to a public target.
#>
[CmdletBinding()]
param(
  [string]$ReposFile = "repos.txt",
  [switch]$Private
)

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot
if ($env:GH_HOST -and $env:GH_HOST -ne "github.com") {
  throw "This inventory publishes to github.com; a different GH_HOST is not accepted."
}
foreach ($tool in @("gh", "git")) {
  if (-not (Get-Command $tool -ErrorAction SilentlyContinue)) { throw "$tool is required." }
}

function Invoke-Gh {
  param([string[]]$Arguments)
  & gh @Arguments
  if ($LASTEXITCODE -ne 0) { throw "gh failed with exit $LASTEXITCODE. Publication stopped." }
}

function Invoke-Git {
  param([string[]]$Arguments)
  & git @Arguments
  if ($LASTEXITCODE -ne 0) { throw "git failed with exit $LASTEXITCODE. Publication stopped." }
}

Invoke-Gh -Arguments @("auth", "status")
$user = (Invoke-Gh -Arguments @("api", "user", "--jq", ".login")).Trim()
if ($user -notmatch '^[A-Za-z0-9][A-Za-z0-9-]*$') { throw "Invalid authenticated GitHub account." }

$knownRepos = @{}
$metadata = Invoke-Gh -Arguments @(
  "api", "--paginate", "user/repos?affiliation=owner&per_page=100",
  "--jq", '.[] | [.full_name, .visibility] | @tsv'
)
foreach ($entry in @($metadata)) {
  if ([string]::IsNullOrWhiteSpace($entry)) { continue }
  $fields = $entry -split "`t"
  if ($fields.Count -ne 2 -or $fields[1].ToUpperInvariant() -notin @("PRIVATE", "PUBLIC")) {
    throw "Cannot establish owned-repository visibility. Publication stopped."
  }
  $knownRepos[$fields[0]] = $fields[1]
}

foreach ($raw in Get-Content -LiteralPath $ReposFile) {
  $line = $raw.Trim()
  if (-not $line -or $line.StartsWith("#")) { continue }
  $parts = $line -split "\|"
  if ($parts.Count -notin @(2, 3) -or -not $parts[1].Trim()) {
    throw "Expected name|description[|public or private]."
  }
  $repo = $parts[0].Trim()
  $desc = $parts[1].Trim()
  $declared = if ($parts.Count -eq 3) { $parts[2].Trim() } else { "" }
  if ($parts.Count -eq 3 -and $declared -cnotin @("public", "private")) {
    throw "Visibility must be public or private."
  }
  if ($repo -notmatch '^ghcp-demos$|^ghcp-demo-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*$') {
    throw "Invalid repository name in publishing inventory."
  }
  $requiredPrivate = $declared -ceq "private"
  $visibility = if ($Private -or $requiredPrivate) { "--private" } else { "--public" }
  $target = "$user/$repo"
  $repoPath = if ($repo -eq "ghcp-demos") { $PSScriptRoot } else { Join-Path $PSScriptRoot $repo }
  if (-not (Test-Path -LiteralPath $repoPath -PathType Container)) {
    Write-Warning "Missing folder, not published: $repo"
    continue
  }

  if (-not $knownRepos.ContainsKey($target)) {
    Write-Host "Creating $target $visibility (no content pushed yet)..."
    Invoke-Gh -Arguments @("repo", "create", $target, $visibility, "--description", $desc)
  }
  $actualVisibility = (Invoke-Gh -Arguments @("repo", "view", $target, "--json", "visibility", "--jq", ".visibility")).Trim()
  if ($requiredPrivate -and $actualVisibility -cne "PRIVATE") {
    throw "Refusing to publish private inventory entry $target to a non-private target."
  }
  if ($actualVisibility -cnotin @("PRIVATE", "PUBLIC")) { throw "Unexpected target visibility." }

  Push-Location $repoPath
  try {
    if (-not (Test-Path -LiteralPath ".git")) {
      Invoke-Git -Arguments @("init", "-q", "-b", "main")
      Invoke-Git -Arguments @("add", ".")
      Invoke-Git -Arguments @(
        "-c", "user.email=copilot@users.noreply.github.com",
        "-c", "user.name=GitHub Copilot Demo Bootstrapper",
        "commit", "-q", "-m", "Initial commit", "-m",
        "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
      )
    }
    $remotes = @(Invoke-Git -Arguments @("remote"))
    if ($remotes -notcontains "origin") {
      Invoke-Git -Arguments @("remote", "add", "origin", "https://github.com/$target.git")
    }
    $pushUrls = @(Invoke-Git -Arguments @("remote", "get-url", "--push", "--all", "origin"))
    $allowed = @(
      "https://github.com/$target.git", "https://github.com/$target",
      "git@github.com:$target.git", "ssh://git@github.com/$target.git"
    )
    if ($pushUrls.Count -ne 1 -or $pushUrls[0] -notin $allowed) {
      throw "Origin push URL does not match the visibility-checked target $target."
    }
    Write-Host "Pushing $target ($actualVisibility)..."
    Invoke-Git -Arguments @("push", "-u", "origin", "main")
  } finally {
    Pop-Location
  }
}

Write-Host "`nDone. Missing folders, if reported, were not published."
