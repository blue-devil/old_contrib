#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

#WorkDir = "."

def setup():
	pass

def build():
	pythonmodules.compile()

def install():
	pythonmodules.install()

#	pisitools.dodoc("LICENSE")

