#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir="xfce-polkit-0.3"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.make("install DESTDIR={}".format(get.installDIR()))
    #only start with xfce
    f=open("{}/etc/xdg/autostart/xfce-polkit.desktop".format(get.installDIR()),"a")
    f.write("OnlyShowIn=XFCE;")
    f.close()

