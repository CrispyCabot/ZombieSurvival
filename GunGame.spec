# -*- mode: python -*-

block_cipher = None


a = Analysis(['GunGame.py'],
             pathex=['C:\\Users\\cjbas\\Desktop\\ZombieSurvival'],
             binaries=[],
             datas=[('data', 'cdata')],
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
          name='Zombie Survival',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False, icon=os.path.join('data','zombieIco.ico'))
