[CmdletBinding()]
param(
  [ValidateSet('claude','codex','kimi','generic')]
  [string]$Agent = 'generic',
  [string]$Dest,
  [string]$Ref = 'v0.4.0',
  [switch]$Force,
  [switch]$DryRun,
  [switch]$Doctor
)

$Repo = 'Wenhua-Li/evo-writing-skill'
$SkillName = 'evo-write'

if (-not $Dest) {
  $Dest = if ($Agent -eq 'claude') { Join-Path $HOME '.claude\skills' } else { Join-Path $HOME '.agents\skills' }
}
$Target = Join-Path $Dest $SkillName

if ($Doctor) {
  $Skill = Join-Path $Target 'SKILL.md'
  if (-not (Test-Path $Skill)) { throw "EvoWrite is not installed at $Target" }
  if (-not (Select-String -Path $Skill -Pattern '^name: evo-write$' -Quiet)) { throw 'SKILL.md does not declare name: evo-write' }
  Write-Host "EvoWrite installation looks valid: $Target"
  exit 0
}

function Download-WithRetries([string]$Uri, [string]$OutFile) {
  $Attempts = 0
  while ($true) {
    try {
      Invoke-WebRequest -Uri $Uri -OutFile $OutFile -TimeoutSec 30
      return
    } catch {
      $Attempts += 1
      if ($Attempts -ge 5) { throw }
      Start-Sleep -Seconds 2
    }
  }
}

function Install-FromManifest([string]$Temp) {
  $Source = Join-Path $Temp 'repo'
  New-Item -ItemType Directory -Force -Path $Source | Out-Null
  $BaseUrl = "https://raw.githubusercontent.com/$Repo/$Ref"
  Write-Host "Downloading EvoWrite file manifest from $BaseUrl..."
  $ManifestFile = Join-Path $Temp 'manifest.txt'
  Download-WithRetries "$BaseUrl/install-manifest.txt" $ManifestFile
  foreach ($Rel in (Get-Content $ManifestFile)) {
    $Rel = $Rel.Trim()
    if (-not $Rel) { continue }
    $Out = Join-Path $Source $Rel
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $Out) | Out-Null
    Download-WithRetries "$BaseUrl/$Rel" $Out
  }
  return $Source
}

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
if (Test-Path (Join-Path $ScriptDir 'SKILL.md')) {
  $Source = $ScriptDir
} else {
  $Temp = Join-Path ([IO.Path]::GetTempPath()) ("evowrite-" + [guid]::NewGuid().ToString('N'))
  $Source = $null
  if ($Ref -ne 'main') {
    $ZipUrl = "https://github.com/$Repo/releases/download/$Ref/evo-writing-skill-$Ref.zip"
    $Archive = Join-Path $Temp 'evo-write.zip'
    try {
      Write-Host 'Downloading EvoWrite release archive...'
      Download-WithRetries $ZipUrl $Archive
      $Extract = Join-Path $Temp 'extract'
      Expand-Archive -Path $Archive -DestinationPath $Extract
      $Candidate = Join-Path $Extract 'evo-write'
      if (Test-Path (Join-Path $Candidate 'SKILL.md')) { $Source = $Candidate }
    } catch {
      Write-Host 'Release archive unavailable; falling back to manifest download.'
    }
  }
  if (-not $Source) { $Source = Install-FromManifest $Temp }
}

$SourceSkill = Join-Path $Source 'SKILL.md'
if (-not (Test-Path $SourceSkill)) { throw 'Could not find SKILL.md in the source.' }
if (-not (Select-String -Path $SourceSkill -Pattern '^name: evo-write$' -Quiet)) { throw 'SKILL.md does not declare name: evo-write' }

if ($DryRun) {
  Write-Host "Would install from: $Source"
  Write-Host "Would install to:   $Target"
  if (Test-Path $Target) { Write-Host 'Existing installation would be backed up.' }
  exit 0
}

New-Item -ItemType Directory -Force -Path $Dest | Out-Null
if (Test-Path $Target) {
  if (-not $Force) { throw "$Target already exists. Re-run with -Force to replace it." }
  $Backup = "$Target.backup.$(Get-Date -Format yyyyMMddHHmmss)"
  Move-Item $Target $Backup
  Write-Host "Existing installation backed up to $Backup"
}
New-Item -ItemType Directory -Force -Path $Target | Out-Null

Get-ChildItem -Path $Source -Force | Where-Object { $_.Name -notin @('.git','build','dist','__pycache__') } | ForEach-Object {
  Copy-Item $_.FullName -Destination $Target -Recurse -Force
}

if (-not (Select-String -Path (Join-Path $Target 'SKILL.md') -Pattern '^name: evo-write$' -Quiet)) { throw 'Installation validation failed.' }
Write-Host "EvoWrite installed to $Target"
Write-Host 'Try: Use evo-write. Rewrite this paragraph to remove AI tells and return only the revised English.'
