[CmdletBinding()]
param(
  [ValidateSet('claude','codex','kimi','generic')]
  [string]$Agent = 'generic',
  [string]$Dest,
  [string]$Ref = 'main',
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

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
if (Test-Path (Join-Path $ScriptDir 'SKILL.md')) {
  $Source = $ScriptDir
} else {
  $Temp = Join-Path ([IO.Path]::GetTempPath()) ("evowrite-" + [guid]::NewGuid().ToString('N'))
  New-Item -ItemType Directory -Path $Temp | Out-Null
  $Zip = Join-Path $Temp 'repo.zip'
  Write-Host "Downloading $Repo@$Ref..."
  Invoke-WebRequest -Uri "https://github.com/$Repo/archive/$Ref.zip" -OutFile $Zip
  Expand-Archive -Path $Zip -DestinationPath $Temp
  $Source = (Get-ChildItem -Path $Temp -Directory | Select-Object -First 1).FullName
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
