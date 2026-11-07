# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules

hiddenimports = []
hiddenimports += collect_submodules('app')


a = Analysis(
    ['C:/Users/guilh/Desktop/Projetos pessoais/Automacao_Portal_SENAI_v2.1.10_FLUXO_CORRIGIDO/_Sistema/iniciar_portal.pyw'],
    pathex=['C:/Users/guilh/Desktop/Projetos pessoais/Automacao_Portal_SENAI_v2.1.10_FLUXO_CORRIGIDO/_Sistema'],
    binaries=[],
    datas=[('C:/Users/guilh/AppData/Local/ms-playwright', 'ms-playwright')],
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Automacao Portal SENAI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    contents_directory='_runtime',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Automacao Portal SENAI',
)
