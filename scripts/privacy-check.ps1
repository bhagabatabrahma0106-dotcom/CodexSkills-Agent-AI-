$ErrorActionPreference = "Stop"

$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$self = (Resolve-Path $MyInvocation.MyCommand.Path).Path
$patterns = @(
  "sk-proj-",
  "sk-",
  "OPENAI_API_KEY=",
  "Authorization: Bearer",
  "api_key:",
  "apikey:",
  "api-key:",
  "access_token:",
  "refresh_token:",
  "BEGIN OPENSSH PRIVATE KEY",
  "BEGIN RSA PRIVATE KEY",
  "C:\\Users\\",
  "\\Clients\\"
)

$files = Get-ChildItem $root -Recurse -File -Force |
  Where-Object {
    $_.FullName -notmatch "\\.git\\" -and
    $_.FullName -ne $self -and
    $_.Extension -notin @(".png", ".jpg", ".jpeg", ".gif", ".mp4", ".mov", ".webp")
  }

$envFiles = Get-ChildItem $root -Recurse -File -Force -Include ".env", ".env.*" |
  Where-Object { $_.FullName -notmatch "\\.git\\" }

$findings = foreach ($pattern in $patterns) {
  $matches = $files | Select-String -Pattern $pattern -SimpleMatch -ErrorAction SilentlyContinue
  foreach ($match in $matches) {
    [PSCustomObject]@{
      Pattern = $pattern
      Path = $match.Path.Substring($root.Length + 1)
      Line = $match.LineNumber
      Text = $match.Line.Trim()
    }
  }
}

foreach ($envFile in $envFiles) {
  [PSCustomObject]@{
    Pattern = "env-file"
    Path = $envFile.FullName.Substring($root.Length + 1)
    Line = 0
    Text = "Environment file should not be shared"
  }
}

if ($findings) {
  $findings | Format-Table -AutoSize
  throw "Potential private data found. Review findings before sharing."
}

Write-Host "Privacy check passed. No obvious secrets or local user paths found."
