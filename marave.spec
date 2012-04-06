# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support/_mountzlib.py'), os.path.join(HOMEPATH,'support/useUnicode.py'), 'marave-editor'],
             pathex=['/home/ralsina/Desktop/proyectos/marave/trunk'])
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build/pyi.linux2/marave-editor', 'marave-editor'),
          debug=False,
          strip=False,
          upx=True,
          console=1 )
coll = COLLECT( exe,
               a.binaries,
               [('radios.txt','marave/radios.txt','DATA')],
               Tree('marave/icons','icons'),
               Tree('marave/backgrounds','backgrounds'),
               Tree('marave/clicks','clicks'),
               Tree('marave/stylesheets','stylesheets'),
               Tree('marave/themes','themes'),
               Tree('marave/translations','translations'),
               Tree('marave/editor/highlight','marave/editor/highlight'),
               Tree('marave/plugins','plugins'),
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name=os.path.join('dist', 'marave-editor'))
