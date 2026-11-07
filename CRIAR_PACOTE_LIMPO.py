"""Generate a shareable package without copying any teacher data."""
from __future__ import annotations

import shutil
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "_Sistema"
OUTPUT = ROOT / "Automacao_Portal_SENAI_FINAL_LIMPA.zip"

EXCLUDED_PARTS = {
    "data", "logs", "screenshots", "tests", "__pycache__", ".git", ".pytest_cache",
}
EXCLUDED_NAMES = {
    "verify_frequency_portal.py", "erro_inicializacao.txt", "LEIA_PRIMEIRO.txt",
}


def allowed(path: Path) -> bool:
    relative = path.relative_to(SOURCE)
    return not any(part in EXCLUDED_PARTS for part in relative.parts) and path.name not in EXCLUDED_NAMES


with tempfile.TemporaryDirectory(prefix="senai-package-") as temp_name:
    package = Path(temp_name) / "Automacao Portal SENAI"
    system = package / "_Sistema"
    system.mkdir(parents=True)
    for path in SOURCE.rglob("*"):
        if not path.is_file() or not allowed(path):
            continue
        target = system / path.relative_to(SOURCE)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)

    shutil.copy2(ROOT / "distribuicao" / "INSTALAR.bat", package / "INSTALAR.bat")
    shutil.copy2(ROOT / "distribuicao" / "ABRIR PORTAL.bat", package / "ABRIR PORTAL.bat")
    shutil.copy2(ROOT / "distribuicao" / "LEIA PRIMEIRO.txt", package / "LEIA PRIMEIRO.txt")
    shutil.copy2(ROOT / "distribuicao" / "MANUAL DO PROFESSOR.txt", package / "MANUAL DO PROFESSOR.txt")
    shutil.copy2(ROOT / "distribuicao" / "requirements.txt", package / "requirements.txt")

    with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in package.rglob("*"):
            if path.is_file():
                archive.write(path, path.relative_to(package.parent))

print(OUTPUT)
