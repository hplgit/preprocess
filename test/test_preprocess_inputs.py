#!/usr/bin/env python
# Copyright (c) 2002 Trent Mick
# License: MIT License (http://www.opensource.org/licenses/mit-license.php)
# Contributors:
#   Trent Mick (TrentM@ActiveState.com)

"""Test preprocessing of inputs/... with preprocess.py."""

import sys
import os
from os.path import join, dirname
import unittest
import difflib
import pprint

import testsupport
from testsupport import TMPDIR



#----- test cases

class PreprocessInputsTestCase(unittest.TestCase):
    def setUp(self):
        if not os.path.exists(TMPDIR):
            os.makedirs(TMPDIR)


def _testOneInputFile(self, fname):
    import preprocess

    # Determine input options to use, if any.
    optsfile = os.path.join('inputs', fname+'.opts') # input options
    opts = []
    if os.path.exists(optsfile):
        for line in open(optsfile, 'r').readlines():
            if line[-1] == "\n": line = line[:-1]
            opts.append(line.strip())
        #print "options from '%s': %s" % (optsfile, pprint.pformat(opts))

    # Preprocess.
    infile = os.path.join('inputs', fname) # input
    outfile = os.path.join('tmp', fname) # actual output
    preprocess_py = join(dirname(dirname(__file__)), "preprocess.py")
    argv = [sys.executable, preprocess_py] + opts + ["-o", outfile, infile]
    dummy, err, retval = testsupport.run(argv)
    try:
        out = open(outfile, 'r').read()
    except IOError, ex:
        self.fail("unexpected error running '%s': '%s' was not generated:\n"
                  "\t%s" % (' '.join(argv), outfile, err))
    #print
    #print "CMD   : %r" % ' '.join(argv)
    #print "STDOUT: %r" % err
    #print "STDERR: %r" % err
    #print "RETVAL: %r" % retval

    # Compare results with the expected.
    expoutfile = os.path.join('outputs', fname) # expected stdout output
    experrfile = os.path.join('outputs', fname+'.err') # expected error output
    if os.path.exists(expoutfile):
        expout = open(expoutfile, 'r').read()
        #print "expected stdout output: %r" % expout
        if not sys.platform.startswith("win"):
            expout = expout.replace('\\','/') # use Un*x paths
        if expout != out:
            diff = list(difflib.ndiff(expout.splitlines(1), out.splitlines(1)))
            self.fail("%r != %r:\n%s"\
                      % (expoutfile, outfile, pprint.pformat(diff)))
    if os.path.exists(experrfile):
        experr = open(experrfile, 'r').read()
        #print "expected stderr output: %r" % experr
        massaged_experr = experr.replace("inputs/", "inputs"+os.sep)
        diff = list(difflib.ndiff(massaged_experr.strip().splitlines(1),
                                  err.strip().splitlines(1)))
        self.failUnlessEqual(massaged_experr.strip(), err.strip(),
                             "<expected error> != <actual error>:\n%s"\
                             % pprint.pformat(diff))
    elif err:
        self.fail("there was error output when processing '%s', but no "\
                  "expected stderr output file, '%s'" % (infile, experrfile))

    # Ensure next test file gets a clean preprocess.
    del sys.modules['preprocess']
        

#for fname in ["keep_lines_bugs.py"]:
for fname in os.listdir('inputs'):
    if fname.endswith(".opts"): continue # skip input option files
    if os.path.isdir(os.path.join('inputs', fname)): continue
    testFunction = lambda self, fname=fname: _testOneInputFile(self, fname)
    name = 'test:'+fname
    setattr(PreprocessInputsTestCase, name, testFunction)


#---- mainline

def suite():
    """Return a unittest.TestSuite to be used by test.py."""
    return unittest.makeSuite(PreprocessInputsTestCase)

if __name__ == "__main__":
    runner = unittest.TextTestRunner(sys.stdout, verbosity=2)
    result = runner.run(suite())

