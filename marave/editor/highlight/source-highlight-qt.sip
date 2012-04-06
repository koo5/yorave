%Module SyntaxHighlighter 0

%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip


%ModuleHeaderCode
#include <srchiliteqt/Qt4SyntaxHighlighter.h>
#include <srchiliteqt/LanguageComboBox.h>
#include <srchiliteqt/StyleComboBox.h>
%End

namespace srchiliteqt {

class Qt4SyntaxHighlighter { 
%TypeHeaderCode
#include <srchiliteqt/Qt4SyntaxHighlighter.h>
%End

public:
    Qt4SyntaxHighlighter(QTextDocument *doc = 0);
    void init(const QString &langFile, const QString &styleFile=
            "default.style");
    bool initFromFileName(const QString &fileName);
    virtual void rehighlight();
    void setFormattingStyle(const QString &styleFile);
    void setDocument ( QTextDocument * doc );
    void rehighlightBlock ( const QTextBlock & block );
    const QString getLangDefFileFromFileName(const QString &filename);
    void setDefaultToMonospace(bool);
private:
   Qt4SyntaxHighlighter(const srchiliteqt::Qt4SyntaxHighlighter&);

};

class LanguageComboBox: QComboBox {
%TypeHeaderCode
#include <srchiliteqt/LanguageComboBox.h>
%End
public:
   LanguageComboBox(const QString &path = ""); 
private:
   LanguageComboBox(const srchiliteqt::LanguageComboBox&);
};

class StyleComboBox: QComboBox {
%TypeHeaderCode
#include <srchiliteqt/StyleComboBox.h>
%End
public:
   StyleComboBox(const QString &path = ""); 
private:
   StyleComboBox(const srchiliteqt::StyleComboBox&);
};

};
