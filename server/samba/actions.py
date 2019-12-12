#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

shelltools.export("JOBS", get.makeJOBS().replace("-j", ""))

MODULES = "idmap_ad,idmap_rid,idmap_adex,idmap_hash,idmap_tdb2,\
pdb_tdbsam,pdb_ldap,pdb_ads,pdb_smbpasswd,pdb_wbc_sam,pdb_samba4,\
auth_unix,auth_wbc,auth_server,auth_netlogond,auth_script,auth_samba4"


def setup():
    inarytools.flags.add("-D_FILE_OFFSET_BITS=64", "-D_GNU_SOURCE", "-DLDAP_DEPRECATED", "-fPIC")
    shelltools.system("""sed -i -e '/"dns.resolver":/d' third_party/wscript""")
    shelltools.system("""sed -i -e '/"iso8601":/d' third_party/wscript""")
    shelltools.system("sed -e 's:<gpgme\.h>:<gpgme/gpgme.h>:' \
	                   -i source4/dsdb/samdb/ldb_modules/password_hash.c ")
    autotools.configure("\
                         --libdir=/usr/lib \
                         --with-cachedir=/var/lib/samba \
                         --with-configdir=/etc/samba \
                         --with-lockdir=/var/cache/samba \
                         --with-logfilebase=/var/log/samba \
                         --with-modulesdir=/usr/lib/samba \
                         --with-pammodulesdir=/lib/security \
                         --with-piddir=/run/samba \
                         --with-privatedir=/var/lib/samba/private \
                         --with-sockets-dir=/run/samba \
                         --disable-rpath \
                         --disable-rpath-install \
                         --enable-fhs \
                         --nopyc \
                         --nopyo \
                         --with-acl-support \
                         --with-ads \
                         --with-automount \
                         --with-cluster-support \
                         --with-dnsupdate \
                         --with-pam \
                         --with-quotas \
                         --with-sendfile-support \
                         --with-shared-modules=%s \
                         --with-syslog \
                         --with-utmp \
                         --with-winbind \
                         --bundled-libraries=!tdb,!talloc,!pytalloc-util,!tevent,!popt \
                        " % MODULES)
    # !ldb,!pyldb-util

def build():
    shelltools.system("make")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    inarytools.dosym("samba-4.0/libsmbclient.h", "/usr/include/libsmbclient.h")

    inarytools.insinto("/etc/openldap/", "examples/LDAP/samba.schema", "samba")
    inarytools.insinto("/etc/samba", "examples/smb.conf.default")
