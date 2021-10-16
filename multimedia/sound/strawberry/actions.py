#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = ''.join([
    ' -DBUILD_WITH_QT5=ON',
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DUSE_TAGPARSER=ON',
    ' -DCMAKE_INSTALL_PREFIX=/usr -L '
    ])

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure(j, sourceDir = '..')

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("../Changelog", "../COPYING", "../README.md")
