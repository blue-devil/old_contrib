#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, autotools, pisitools

def setup():
	shelltools.system("./bootstrap")
	autotools.configure()

def build():
	autotools.make()

def install():
	autotools.install()

	pisitools.dodoc("AUTHORS")
