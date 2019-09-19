#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import perlmodules
from inary.actionsapi import inarytools
from inary.actionsapi import get
from inary.actionsapi import shelltools

WorkDir=""
shelltools.export("HOME", get.workDIR())

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

# FIXME: test fails
def check():
    perlmodules.make("test")

def install():
    perlmodules.install()
    inarytools.removeDir("/usr/share/man/man3")
