#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    autotools.autoreconf("-if")
    autotools.configure("\
                         --disable-static \
                         --enable-dri \
                         --enable-viaregtool \
                         --enable-debug \
                         --enable-xv-debug \
                        ")
    
    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()
    inarytools.dodoc("COPYING", "ChangeLog", "NEWS", "README")
