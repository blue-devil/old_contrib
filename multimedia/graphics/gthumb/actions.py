#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("LC_ALL", "en_US.UTF-8")

z = "-Dwarn-deprecated=false \
     -Dlibbrasero=false \
    "

def setup():
	mesontools.configure(z)

def build():
	mesontools.build()

def install():
	mesontools.install()

	pisitools.dodoc("AUTHORS", "COPYING", "MAINTAINERS", "NEWS", "README.md")

