$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$source = Join-Path $root "_Sistema"
$browser = Join-Path $env:LOCALAPPDATA "ms-playwright"
$dist = Join-Path $root "dist_professores"
$work = Join-Path $root "build_professores"
$spec = Join-Path $root "Automacao Portal SENAI.spec"

if (-not (Test-Path -LiteralPath $browser -PathType Container)) {
    throw "Chromium do Playwright não foi encontrado em $browser"
}

python -m PyInstaller `
    --noconfirm `
    --clean `
    --windowed `
    --onedir `
    --contents-directory "_runtime" `
    --name "Automacao Portal SENAI" `
    --distpath $dist `
    --workpath $work `
    --specpath $root `
    --paths $source `
    --collect-submodules app `
    --add-data "$browser;ms-playwright" `
    (Join-Path $source "iniciar_portal.pyw")

if ($LASTEXITCODE -ne 0) { throw "Falha na compilação do executável." }

$package = Join-Path $dist "Automacao Portal SENAI"
Copy-Item -LiteralPath (Join-Path $root "distribuicao\MANUAL DO PROFESSOR.txt") -Destination $package -Force
Copy-Item -LiteralPath (Join-Path $root "distribuicao\LEIA PRIMEIRO.txt") -Destination $package -Force
Copy-Item -LiteralPath (Join-Path $source "VERSAO.txt") -Destination $package -Force

$zip = Join-Path $root "Automacao_Portal_SENAI_PROFESSORES_EXECUTAVEL.zip"
if (Test-Path -LiteralPath $zip) { Remove-Item -LiteralPath $zip -Force }
Compress-Archive -LiteralPath $package -DestinationPath $zip -CompressionLevel Optimal
Write-Output $zip
