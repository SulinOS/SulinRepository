#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -fPIC" % get.CFLAGS())
    autotools.autoreconf("-vfi")
    autotools.configure("--prefix=/usr \
                         --enable-ipv6 \
                         --enable-bluetooth")

def build():
    autotools.make("all")
    autotools.make("shared")

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # No static libs
    inarytools.remove("/usr/lib/*.a")

    # it is needed for ppd etc.
    inarytools.insinto("/usr/include", "pcap-int.h")

    inarytools.dodoc("CHANGES", "CREDITS", "README*", "VERSION", "TODO")
