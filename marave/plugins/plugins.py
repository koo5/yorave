# -*- coding: utf-8 -*-

import os, sys
from PyQt4 import QtGui

from Ui_conf import Ui_Dialog as ConfDialog

if hasattr(sys, 'frozen'):
    PATH = os.path.join(os.path.abspath(os.path.dirname(sys.executable)),'plugins')
else:
    PATH = os.path.abspath(os.path.dirname(__file__))

class ConfigDialog(QtGui.QDialog):
    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent)
        self.ui=ConfDialog()
        self.ui.setupUi(self)

class Plugin (object):
    
    instances = {}
    settings = None
    
    def __init__(self, client):
        '''client is the MainWindow of Marave, everything is there somewhere'''
        self.client=client
        self.sc=QtGui.QShortcut(QtGui.QKeySequence(self.shortcut), client)
        self.sc.activated.connect(self.run)

    def run(self):
	pass
    
    @classmethod
    def addConfigWidgets(self, dialog):
        '''Add whatever config widgets are needed to dialog'''
        
    @classmethod
    def enable(self, enabled=None, client=None):
        if enabled is None: return
        if client is None: return
        
        enabledPlugins = client.settings.value('enabledplugins')
        if enabledPlugins.isValid():
            enabledPlugins=unicode(enabledPlugins.toString()).split(',')
        else:
            enabledPlugins=[]
        if self.name not in enabledPlugins and enabled:
            enabledPlugins.append(self.name)
        elif self.name in enabledPlugins and not enabled:
            enabledPlugins.remove(self.name)
        
        if any(enabledPlugins):
            client.pluginButton.show()
        else:
            client.pluginButton.hide()
        client.layoutButtons()
        
        client.settings.setValue('enabledplugins',','.join(enabledPlugins))
        client.settings.sync()
        
        Plugin.instance(self, client)
        
        
    @classmethod
    def loadConfig(self):
        # Override shortcut with settings
        if self.settings:
            sc=self.settings.value('shortcut-'+self.name+'-shortcut')
            if sc.isValid():
                self.shortcut=unicode(sc.toString())
        
    @classmethod
    def showConfig(self, client):
        self.settings=client.settings
        dialog=ConfigDialog(client)
        self.loadConfig()
        self.addConfigWidgets(dialog)
        dialog.ui.shortcut.setText(self.shortcut)
        r=dialog.exec_()        
        if r==QtGui.QDialog.Accepted:
            self.saveConfig(dialog)
            
    @classmethod
    def saveConfig(self, dialog):
        self.shortcut=unicode(dialog.ui.shortcut.text())
        if self.settings:
            self.settings.setValue('plugin-'+self.name+'-shortcut', self.shortcut)
            self.settings.sync()
    
    @classmethod
    def selectorWidget(self):
        w=QtGui.QWidget()
        w.check=QtGui.QCheckBox(self.description)
        w.conf=QtGui.QPushButton(QtGui.QIcon(os.path.join(PATH,'icons','configure.svg')),'')
        l=QtGui.QHBoxLayout()
        l.addWidget(w.check)
        l.addStretch(10)
        l.addWidget(w.conf)
        w.setLayout(l)
        return w
        
    @classmethod
    def instance(self, pluginClass, client):
        if pluginClass not in self.instances:
            self.instances[pluginClass]=pluginClass(client)
        return self.instances[pluginClass]
            

    @classmethod
    def initPlugins(self):
        l=[]
        for p in os.listdir(PATH):
            if p.endswith('.py') and p != 'plugins.py':
                l.append(p)
        for p in l:
            if hasattr(sys, 'frozen'):
                print __import__('plugins.'+p[:-3], level=-1)
            else:
                print __import__('marave.plugins.'+p[:-3], level=-1)

    @classmethod
    def listPlugins(self):
        return Plugin.__subclasses__()
