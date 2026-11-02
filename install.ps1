$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$skillsSource = Join-Path $repoRoot "skills"
$skillsTarget = Join-Path $env:USERPROFILE ".codex\skills"

if (-not (Test-Path $skillsSource)) {
  throw "Could not find skills folder at $skillsSource"
}

New-Item -ItemType Directory -Force $skillsTarget | Out-Null
Copy-Item (Join-Path $skillsSource "*") $skillsTarget -Recurse -Force

Write-Host "Installed Codex Social AI Team skills to $skillsTarget"
Write-Host "Restart Codex before using the skills."

