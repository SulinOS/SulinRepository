#!/usr/bin/env python3

import os

def createNode(mode, uid, gid, minor, major, path):
    os.system("/bin/mknod --mode=%d %s c %d %d" % (mode, path, minor, major))
    os.system("/bin/chown %s:%s %s" % (uid, gid, path))

def postInstall():
    os.system("mkdir -p /lib/udev/devices/net 2>/dev/null")
    createNode(600, "root", "root",     1, 11,      "/lib/udev/devices/kmsg")
    createNode(666, "root", "root",     1, 3,       "/lib/udev/devices/null")
    createNode(666, "root", "root",     1, 5,       "/lib/udev/devices/zero")
    createNode(600, "root", "root",     10, 130,    "/lib/udev/devices/watchdog")
    createNode(666, "root", "root",     10, 229,    "/lib/udev/devices/fuse")
    createNode(600, "root", "tty",      5, 1,       "/lib/udev/devices/console")
    createNode(666, "root", "tty",      5, 2,       "/lib/udev/devices/ptmx")
    createNode(666, "root", "tty",      5, 0,       "/lib/udev/devices/tty")
    createNode(620, "root", "tty",      4, 1,       "/lib/udev/devices/tty1")
    createNode(600, "root", "root",     10, 200,    "/lib/udev/devices/net/tun")
    createNode(600, "root", "root",     36, 0,      "/lib/udev/devices/route")
    createNode(600, "root", "root",     10, 200,    "/lib/udev/devices/skip")
    createNode(660, "root", "dialout",  108, 0,     "/lib/udev/devices/ppp")

    os.system("/sbin/udevadm hwdb --update")

def postRemove():
    pass
    
def preRemove():
    pass
