# -*- coding: utf-8 -*-
import sys

from PyQt4 import QtCore, QtGui
from SyntaxHighlighter import srchiliteqt


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window=QtGui.QWidget()
    window.show()
        
    w = QtGui.QPlainTextEdit()
    langs=srchiliteqt.LanguageComboBox()
    styles=srchiliteqt.StyleComboBox()
    
    
    layout=QtGui.QVBoxLayout()
    layout.addWidget(langs)
    layout.addWidget(styles)
    layout.addWidget(w)

    window.setLayout(layout)

    hp=srchiliteqt.Qt4SyntaxHighlighter(w.document())

    def changeLang(idx):
        print langs.currentText(), styles.currentText()
        hp.init(langs.currentText())
        hp.setFormattingStyle(styles.currentText())
        hp.rehighlight()

    langs.currentIndexChanged.connect(changeLang)
    styles.currentIndexChanged.connect(changeLang)
    
    hp.init('python.lang')

    if len(sys.argv) >1:
        w.setPlainText(open(sys.argv[1]).read())

    sys.exit(app.exec_())