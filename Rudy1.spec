# -*- mode: python -*-
block_cipher = None
qt_dlls_path = r'C:\Users\DevComp900.1\PyQt4dlls'
datas = [(r'.\UI\Icons\*.ico',r'.\UI\Icons'),
(r'{}\qwindows.dll'.format(qt_dlls_path),'.'),
(r'{}\libEGL.dll'.format(qt_dlls_path),'.'),
(r'{}\qico.dll'.format(qt_dlls_path),r'.\imageformats'),
]

a = Analysis(['Rudy.py'],
             pathex=[r'C:\Users\DevComp900.1\PycharmProjects\Rudy'],
             binaries=None,
             datas=datas,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['win32.gen_py'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

 
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
             
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='Rudy',
          debug=False,
          strip=False,
          upx=False,
          window =True ,
          console = True,          
          icon = r'.\UI\Icons\RUDYicon.ico')
          
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='Rudy')
