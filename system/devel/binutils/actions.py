#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

multilib = "--enable-multilib" if get.ARCH() == "x86_64" else ""


def setup():
    autotools.configure('--enable-shared \
                         --build=x86_64-pc-linux-gnu \
                         --enable-threads \
                         --enable-ld=default \
                         --enable-gold \
                         --enable-plugins \
                         --with-pkgversion="Sulin" \
                         --with-bugurl=http://gitlab.com/sulinos/main/issues \
                         %s \
                         --with-pic \
                         --disable-werror' % ( multilib))

def build():
    autotools.make("configure-host")
    autotools.make("tooldir=/usr")

#def check():
#    autotools.make("check -j1")

def install():
    autotools.rawInstall("tooldir=/usr DESTDIR=%s" % get.installDIR())
