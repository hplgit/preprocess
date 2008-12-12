#!/usr/bin/env python
# Copyright (c) 2002-2005 ActiveState Corp.
# See LICENSE.txt for license details.
# Author:
#   Trent Mick (TrentM@ActiveState.com)
# Home:
#   http://trentm.com/projects/preprocess/

"""Distutils setup script for 'preprocess'."""

import sys
import os
import shutil
from distutils.core import setup


#---- support routines

def _getVersion():
    import preprocess
    return preprocess.__version__


def _getBinDir():
    """Return the current Python's bindir."""
    if sys.platform.startswith("win"):
        bindir = sys.prefix
    else:
        bindir = os.path.join(sys.prefix, "bin")
    return bindir

def _getSiteLibDir():
    if sys.platform.startswith("win"):
        sitelibdir = os.path.join(sys.prefix, "Lib", "site-packages")
    else:
        ver = '.'.join(map(str, sys.version_info[:2]))
        sitelibdir = os.path.join(sys.prefix, "lib", "python%s" % ver,
                                  "site-packages")
    return sitelibdir


#---- setup mainline

if sys.platform.startswith('win'):
    scripts = []
    binFiles = ["preprocess.exe", "preprocess.py"]
else:
    if os.path.exists("preprocess"):
        os.remove("preprocess")
    shutil.copy2("preprocess.py", "preprocess")
    scripts = ["preprocess"]
    binFiles = []
siteFiles = ["content.types"]

setup(name="preprocess",
      version=_getVersion(),
      description="a multi-language preprocessor",
      author="Trent Mick",
      author_email="TrentM@ActiveState.com",
      url="http://trentm.com/projects/preprocess/",
      license="MIT License",
      platforms=["Windows", "Linux", "Mac OS X", "Unix"],
      keywords=["preprocess", "preprocessor", "#if", "#else", "#endif"],

      py_modules=['preprocess'],
      scripts=scripts,
      data_files=[ (_getBinDir(), binFiles + siteFiles),
                   (_getSiteLibDir(), siteFiles) ],
     )

