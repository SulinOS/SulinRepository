#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Suleyman POYRAZ (Zaryob)
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir = "dialog-%s-20190808" % get.srcVERSION().replace('_','-')

def setup():
    autotools.configure("--with-ncursesw \
                         --prefix=/usr \
                         --with-libtool \
                         --enable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s install-full" % get.installDIR())

    inarytools.insinto("/usr/share/doc/%s/samples" % get.srcNAME(), "samples/*")
    inarytools.dodoc("CHANGES", "README")
