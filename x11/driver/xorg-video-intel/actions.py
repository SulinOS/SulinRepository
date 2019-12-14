# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import mesontools

def setup():
    mesontools.meson_configure("-D default-dri=3")


def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()
