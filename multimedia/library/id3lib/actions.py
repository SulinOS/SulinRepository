#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import libtools
from inary.actionsapi import inarytools
from inary.actionsapi import get


def setup():
    libtools.libtoolize("-fc")
    autotools.aclocal()
    autotools.autoconf()
    autotools.automake("--add-missing --copy")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.dodoc("AUTHORS*", "COPYING*", "NEWS*", "README*")
