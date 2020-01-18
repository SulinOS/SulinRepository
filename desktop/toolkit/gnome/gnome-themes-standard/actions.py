#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    autotools.configure("--prefix=/usr")

def build():
    autotools.make()

def install():
    autotools.install()
    # fix conflict with gnome-themes
    inarytools.remove("usr/share/icons/HighContrast/index.theme")
    inarytools.remove("usr/share/themes/HighContrast/index.theme")
    inarytools.remove("usr/share/themes/HighContrast/gtk-2.0/gtkrc")
