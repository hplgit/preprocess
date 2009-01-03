#!/usr/bin/env python
# Copyright (c) 2005-2006 ActiveState Software Inc.

"""The preprocess test suite entry point."""

import os
from os.path import exists, join, dirname, abspath
import sys
import logging
from pprint import pprint

import testlib


log = logging.getLogger("test")
default_tags = ["-knownfailure"]


def setup():
    # Ensure the *development* preprocess.py is tested.
    lib_dir = join(dirname(dirname(abspath(__file__))), "lib")
    sys.path.insert(0, lib_dir)
    sys.stdout.write("Setup to test: ")
    sys.stdout.flush()
    preprocess_py = join(lib_dir, "preprocess.py")
    os.system("%s %s -V" % (sys.executable, preprocess_py))
    sys.stdout.write("-"*70 + '\n')

if __name__ == "__main__":
    retval = testlib.harness(setup_func=setup, default_tags=default_tags)
    sys.exit(retval)

