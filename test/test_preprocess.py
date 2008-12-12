
# Copyright (c) 2002 Trent Mick
# 
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""Grab bag of test cases for preprocess.py."""

import sys
import os
import unittest
import difflib
import pprint

import testsupport
from testsupport import TMPDIR



#----- test cases

class PreprocessTestCase(unittest.TestCase):
    def setUp(self):
        self.tmpdir = os.path.join(TMPDIR, "preprocess")
        if not os.path.exists(self.tmpdir):
            os.makedirs(self.tmpdir)

    def test_false_recursive_includes(self):
        # There was a bug pre-0.6.1 where the private list of already
        # preprocessed files, used to trap recursive includes, would not
        # get cleared between independent preprocess() calls in the same
        # Python process. Test that that case has been fixed here.
        import preprocess
        inFile = os.path.join(self.tmpdir, "test_false_recursive_includes.in.py")
        outFile = os.path.join(self.tmpdir, "test_false_recursive_includes.out.py")
        fout = open(inFile, 'w')
        fout.write("foo")
        fout.close()
        preprocess.preprocess(inFile, outFile)
        # If this second one works then the bug is fixed.
        try:
            preprocess.preprocess(inFile, outFile)
        except preprocess.PreprocessError, ex:
            self.fail("Second independant preprocess() call incorrectly "\
                      "re-used list of already preprocessed files froma "\
                      "previous call.")



#---- mainline

def suite():
    """Return a unittest.TestSuite to be used by test.py."""
    return unittest.makeSuite(PreprocessTestCase)

if __name__ == "__main__":
    runner = unittest.TextTestRunner(sys.stdout, verbosity=2)
    result = runner.run(suite())

