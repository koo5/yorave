all: icons_rc.py \
     Ui_prefs.py \
     README.html \
     smartypants_license.html \
     plugins/Ui_conf.py \
     editorwidgets

icons_rc.py: icons.qrc
	pyrcc4 icons.qrc -o icons_rc.py

Ui_searchreplacewidget.py: searchreplwidget.ui
	pyuic4 searchreplwidget.ui -o Ui_searchreplacewidget.py -x

Ui_searchwidget.py: searchwidget.ui
	pyuic4 searchwidget.ui -o Ui_searchwidget.py -x

Ui_prefs.py: prefs.ui
	pyuic4 prefs.ui -o Ui_prefs.py -x

plugins/Ui_conf.py: plugins/conf.ui
	pyuic4 plugins/conf.ui -o plugins/Ui_conf.py -x

README.html: ../README
	rst2html ../README README.html

smartypants_license.html: smartypants_license
	rst2html smartypants_license smartypants_license.html

translations: force
	cd translations && make

editorwidgets: force
	cd editor/widgets && make

force:
	true
