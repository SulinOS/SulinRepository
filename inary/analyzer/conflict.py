# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 - 2018, Suleyman POYRAZ (Zaryob)
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

"""conflict analyzer"""

import gettext
__trans = gettext.translation('inary', fallback=True)
_ = __trans.gettext

import inary.data.relation as relation

""" Conflict relation """
class Conflict(relation.Relation):
    def __str__(self):
        s = self.package
        if self.versionFrom:
            s += _(" version >= ") + self.versionFrom
        if self.versionTo:
            s += _(" version <= ") + self.versionTo
        if self.version:
            s += _(" version ") + self.version
        if self.releaseFrom:
            s += _(" release >= ") + self.releaseFrom
        if self.releaseTo:
            s += _(" release <= ") + self.releaseTo
        if self.release:
            s += _(" release ") + self.release
        return s

def installed_package_conflicts(confinfo):
    """determine if an installed package in *repository* conflicts with
given conflicting spec"""
    return inary.data.relation.installed_package_satisfies(confinfo)

def package_conflicts(pkg, confs):
    for c in confs:
        if pkg.name == c.package and c.satisfies_relation(pkg.version, pkg.release):
            return c

    return None

def calculate_conflicts(order, packagedb):
    """
    Return a tuple of the conflicting packages information -> tuple
    @param packages: list of package names -> list_of_strings

    >>> (pkgs, within, pairs) = inary.api.calculate_conflicts(packages)
    >>>
    >>> pkgs # list of packages that are installed and conflicts with the
             # given packages list -> list_of_strings
    >>> [...]
    >>> within # list of packages that already conflict with each other
               # in the given packages list -> list_of_strings
    >>> [...]
    >>> pairs # dictionary of conflict information that contains which package in the
              # given packages list conflicts with which of the installed packages

    >>> {'imlib2': <class inary.data.conflict.Conflict>, 'valgrind': <class inary.conflict.Conflict>,
    'libmp4v2':'<class inary.data.conflict.Conflict>}

    >>> print map(lambda c:str(pairs[c]), pairs)
    >>> ['imblib', 'callgrind', 'faad2 release >= 3']
    """
    # check conflicting packages in the installed system
    def check_installed(pkg, order):
        conflicts = []

        for conflict in pkg.conflicts:
            if conflict.package not in order and installed_package_conflicts(conflict):
                conflicts.append(conflict)

        return conflicts

    B_0 = set(order)
    conflicting_pkgs = conflicts_inorder = set()
    conflicting_pairs = {}

    for x in order:
        pkg = packagedb.get_package(x)

        # check if any package has conflicts with the installed packages
        conflicts = check_installed(pkg, order)
        if conflicts:
            conflicting_pairs[x] = [str(c) for c in conflicts]
            conflicting_pkgs = conflicting_pkgs.union([c.package for c in conflicts])

        # now check if any package has conflicts with each other
        B_i = B_0.intersection(set([c.package for c in pkg.conflicts]))
        conflicts_inorder_i = set()
        for p in [packagedb.get_package(x) for x in B_i]:
            conflicted = package_conflicts(p, pkg.conflicts)
            if conflicted:
                conflicts_inorder_i.add(str(conflicted))

        if conflicts_inorder_i:
            conflicts_inorder = conflicts_inorder.union(conflicts_inorder_i)
            conflicts_inorder.add(pkg.name)

    return (conflicting_pkgs, conflicts_inorder, conflicting_pairs)