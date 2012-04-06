# -*- coding: utf-8 -*-

from distutils.cmd import Command
from distutils.core import setup, Extension
import os

class build_hl(Command):
    """Builds the syntax highlighter extension"""
    user_options = []
    description = "Build the syntax highlighter extension"
    
    def initialize_options(self):
        self._dir = os.path.abspath(os.path.dirname(__file__))

    def finalize_options(self):
        pass    
    
    def run(self):
        os.chdir(os.path.join(self._dir,'marave','editor','highlight'))
        r=os.system('python2 configure.py')
        if r==0:
            os.system('make')
        os.chdir(self._dir)

setup(name='Marave',
      version='0.7',
      description='A relaxed text editor',
      author='Roberto Alsina',
      author_email='ralsina@netmanagers.com.ar',
      url='http://marave.googlecode.com',
      packages=['marave',
                'marave.editor',
                'marave.editor.widgets',
                'marave.plugins'],
      scripts=['marave-editor'],
      package_data={'marave': ['backgrounds/*',
                               'icons/*svg',
                               'clicks/*wav',
                               'themes/*',
                               'stylesheets/*',
                               'translations/*',
                               'highlight/*',
                               'editor/highlight/*',
                               'radios.txt'
                               ]},
     cmdclass = { 'build_hl': build_hl },
     )
