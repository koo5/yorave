INTRO
=====

Marave is a text editor whose goal is to help you focus on writing.

It's inspired by ommwriter, Darkroom and many other "simple" text 
editors, with a few twists.

REQUIREMENTS
============

As far as I know, all that's needed is:

* PyQt 4.5 or later.
  On Ubuntu and other linuxes, this may mean python-qt4-phonon or some other
  packages in addition to PyQt.

* PyEnchant if you want spellchecking, plus the spellchecking dictionaries for your language.

* I intend to make binaries available for Windows, and am looking for volunteers 
  help to have Mac binaries as well.


MENU
====

If you move your button, you will see a button bar at the right side of the screen.

They are:

* Your font selector

  You can set the font and color of your text.

* Your font size selector

  You can make it larger, smaller, or go back to default.

* The usual file operations

  Open, Save and Save As. For "New File", use Ctrl+N

* A background selector

  Cycle the available backgrounds using the arrows, or use a solid colour.

* A keyclick selector

  Cycle the available key sounds, or disable key clicks.

* A "music station" selector

  Cycle available music stations, or disable music.

* Extra preferences

  Several options, including editor opacity, spell-checking language and more.

* Quit

CHEATCODES
==========

Since the UI is minimal, there are some key combinations that do things you will not
find any buttons for.

* Undo: Ctrl+Z 
* Redo: Strift+Ctrl+Z 
* New Document: Ctrl+N
* Open: Ctrl+O
* Save: Ctrl+S
* Save As: Shift+Ctrl+S
* Find: Ctrl+F
* Find & Replace: Ctrl+R
* Quit: Ctrl+Q
* Document information: Ctrl+I

Adjusting the editor
====================

The Marave window is *always* full screen, you can't change that, but you can change th size of your editor.

If you move your mouse, you will see 4 faint boxes in the corners. Dragging them makes the editor larger or smaller.

If you place the mouse just outside the editor, it should change its shape to a hand. Clicking and dragging will let you move the editor. Remember that the buttons are on the right side, so you need some space there.

CUSTOMIZATION
=============

If you don't like the artwork that comes with Marave, you are of course free to replace it, or expand it.

* You can add new key click sounds by dropping audio files in the clicks folder
* You can add new backgrounds by dropping image files in the backgrounds folder
* You can add new radio stations by adding them in the radios.txt file (one
  per line)

THEMES and STYLES
=================

You can save your settings as a "theme", or choose your theme from the provided presets.

A theme contains: 

* Background
* Font and font size
* Editor size and position
* Editor opacity
* Style
* Music and click sound
* Button style (icon only/text+icon/text only)

Themes are saved in the themes folder, the syntax is INI-like.

A style is a file with a syntax similar to CSS, and it lets you change the look of all UI elements
in Marave. These files are saved in the stylesheets folder, and you can select them from the 
preferences panel.

Note: Style changes only take effect after you restart Marave.

INSTALLATION
============

To install from sources try this::

    python setup.py install

To use Marave without installing, run

::

    python marave-editor

Or, on Linux, make it executable and run it directly::
    
    chmod +x marave-editor
    ./marave-editor

.. sidebar:: Syntax Highlighting

    The syntax highlighting support is experimental and a bit hard to enable.

    You need to install the following:

    * GNU source-highlight, from http://www.gnu.org/software/src-highlite/
    * Source-highlight-qt, from http://srchiliteqt.sourceforge.net/
    * SIP, which should come with PyQt
    * A C++ compiler

    Then, run
    
    ::

        python setup.py build_hl
        python setup.py install

    If all goes well (unlikely ;-), it should work. If it doesn't marave will work anyway, just without 
    syntax highlighting.


CREDITS
=======

CODE
----

Spell checker support and QTextEdit with line numbers thanks to John Schember
http://john.nachtimwald.com/2009/08/22/qplaintextedit-with-in-line-spell-check/


Several patches by Filipe Maia

Plugin system inspired by Armin Ronacher's code at 
http://lucumr.pocoo.org/2006/7/3/python-plugin-system

Smartypants plugin based on smartypants.py by John Gruber and Chad Miller,
http://web.chad.org/projects/smartypants.py/ ( See the `license <smartypants_license.html>`_)

The rest is written by me: Roberto Alsina <ralsina@netmanagers.com.ar>

TRANSLATIONS
------------

* hebrew translation by Yaron Shahrabani
* german translation by Marc Cheng
* polish translation by Łukasz "Cyber Killer" Korpalski
* czech translation by  Martin Stiborský
* italian translation by Pierpaolo da Fieno
* hungarian translation by Németh Gábor
* greek translation by Christos Lazaridis
* french translation by Aymeric Dumaz

ICONS
-----

Some icons are taken from the Reinhardt SVG icon set, or based on them:
http://www.kde-look.org/content/show.php/The+Reinhardt+Icon+Set?content=6153

The Marave icon is by Pierpaolo Da Fieno

Other icons are taken from http://raphaeljs.com/icons/ and they are 
under an MIT license.

IMAGES
------

"Winter landscape classic" by saturn_h
    :license: http://creativecommons.org/licenses/by-nc-sa/2.0/deed.en
    :URL: http://www.flickr.com/photos/hhoyer/3219911918/

"Dutch winter landscape" by zoutedrop
    :license: http://creativecommons.org/licenses/by/2.0/deed.en
    :URL: http://www.flickr.com/photos/zoutedrop/3055849607/

"Landscape with sky" by randihausken
    :license: http://creativecommons.org/licenses/by-nc/2.0/deed.en
    :URL: http://www.flickr.com/photos/randihausken/2212472428/

"Just green curls" by cjcox
    :license: GPL
    :URL: http://www.kde-look.org/content/show.php/Just+Green+Curls?content=118222&PHPSESSID=299f3350a78b1ad0ca3c576436a2ac47

SOUND
-----

The music is streamed from:

* BlueMars radio: http://bluemars.org/
* SomaFM: http://somafm.com/

All click sounds are downloaded from
http://www.adobeflash.com/download/sounds/clicks/

thozi_daCLick.mp3 had no credit information

The following sounds are created by the people at 
http://www.adriantnt.com and this link fulfills 
their license requirements:

* adriantnt_r_plastic.mp3  
* adriantnt_u_click.mp3

The following sounds are created by Partners In Rhyme and
included with permission:

* BEEP1A.WAV
* BEEP1B.WAV
* BEEP1C.WAV
* CLICK10A.WAV 
* SERVO1A.WAV

You can find more click sounds at http://www.partnersinrhyme.com/pirsounds/WEB_DESIGN_SOUNDS_WAV/BUTTONS.shtml
