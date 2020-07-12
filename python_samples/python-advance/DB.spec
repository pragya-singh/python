# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['DB.py'],
             pathex=['/Users/singg/git/all/python/python_samples/python-advance'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='DB',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='download.png')
app = BUNDLE(exe,
             name='DB.app',
             icon='download.png',
             bundle_identifier=None)
