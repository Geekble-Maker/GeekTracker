# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['GeekTracker.py'],
             pathex=['C:\\Users\\SUPERGEEKBLE\\Desktop\\GeekTracker'],
             binaries=[],
             datas=[(HOMEPATH + '\\PyQt5\\Qt\\bin\*', 'PyQt5\\Qt\\bin'), ('UI\\GeekUI(V3).ui', 'UI'), ('Img\\geekblelogo.jpg', 'Img'), ('Custom\\Menu.csv', 'Custom'), ('Custom\\User.csv', 'Custom'), ('Custom\\Key.csv', 'Custom') ],
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
          [],
          exclude_binaries=True,
          name='GeekTracker',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True , icon='Img\\geekble.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='GeekTracker')
