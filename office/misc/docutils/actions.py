#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import pythonmodules
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

WorkDir="docutils-%s" % get.srcVERSION()

def setup():
    shelltools.cd("..")
    shelltools.makedirs("build_python")
    shelltools.copytree("./%s" % WorkDir,  "build_python")
    shelltools.cd(WorkDir)
    
    shelltools.cd("..")
    shelltools.makedirs("build_python3")
    shelltools.copytree("./%s" % WorkDir,  "build_python3")
    shelltools.cd(WorkDir)

def build():
    pythonmodules.compile()
    
    shelltools.cd("../build_python/%s" % WorkDir)
    pythonmodules.compile()
    
    shelltools.system("pwd")
    shelltools.cd("../../build_python3/%s" % WorkDir)
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install()
    
    shelltools.cd("../build_python/%s" % WorkDir)
    pythonmodules.install()
    
    shelltools.cd("../../build_python3/%s" % WorkDir)
    pythonmodules.install(pyVer="3")

    #Remove .py extensions from scripts in /usr/bin
    for f in shelltools.ls("%s/usr/bin" % get.installDIR()):
        inarytools.domove("/usr/bin/%s" % f, "/usr/bin", f.replace(".py", ""))