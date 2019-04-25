# -*- mode: python -*-
block_cipher = None

datas = [('./UI/Icons/*.ico','./UI/Icons'),
#('C:\\Python34\\Lib\\site-packages\\PyQt4\\plugins\\platforms\\qwindows.dll','.'),
#('C:\\Python34\\Lib\\site-packages\\PyQt4\\libEGL.dll','.'),
#('C:\\Python34\\Lib\\site-packages\\PyQt4\\plugins\\imageformats\\qico.dll','.\\imageformats'),
]

a = Analysis(['Rudy.py'],
             pathex=[r'/home/csmythe/PycharmProjects/Rudy'],
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
          icon = './UI/Icons/RUDYicon.ico')
          
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='Rudy')
