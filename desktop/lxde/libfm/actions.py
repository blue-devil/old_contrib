#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

i = ''.join([
    '--enable-gtk-doc ',
    '--enable-udisks ',
    '--disable-old-actions ',
    '--disable-static ',
    '--with-gtk=3 ',
    ])

def setup():
	pisitools.cflags.add("-Wno-deprecated-declarations -Wno-incompatible-pointer-types")
	autotools.configure(i)

	pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "COPYING", "NEWS")

