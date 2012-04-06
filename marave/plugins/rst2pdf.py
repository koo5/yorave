# -*- coding: utf-8 -*-

from plugins import Plugin
from PyQt4 import QtCore, QtGui
import tempfile, codecs
import os, subprocess

class rst2pdf(Plugin):
    name='rst2pdf'
    shortcut='Ctrl+F8'
    description='Run through rst2pdf and preview'
    tmpf=None

    def run(self):
        print "Running rst2pdf"
        
        text=unicode(self.client.editor.toPlainText())
        # Save to a named file
        if self.tmpf is None:
            self.tmpf=tempfile.NamedTemporaryFile(delete=False)
            self.tmpf.close()
        f=codecs.open(self.tmpf.name,'w','utf-8')
        f.write(text)
        f.close()
        
        # FIXME: unsafe
        # FIXME: show output of the process somewhere
        try:
            self.client.notify('Running rst2pdf')
            subprocess.check_call('rst2pdf %s'%self.tmpf.name, shell=True)
        except subprocess.CalledProcessError:
            #FIXME: show error dialog
            return
        # Open with default PDF viewer 
        # FIXME: would be awesome if we could know when this is still open
        # and not launch it again, since it refreshes automatically.
        self.client.notify('Launching PDF viewer')
        QtGui.QDesktopServices.openUrl(QtCore.QUrl('file://'+self.tmpf.name+'.pdf'))