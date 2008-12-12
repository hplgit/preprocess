#!python
# Test that substitution does NOT happen in strings. In current
# preprocess.py it *does* (hence this test is currently expected to
# fail). However, the long term goal is to understand languages' string
# tokens and skip them for substitution.

# #define VAR foo

if __name__ == '__main__':
    foo = 1
    # The V-A-R should _not_ be substituted in the string.
    print "VAR is", VAR

