#!python

if __name__ == '__main__':
    print "hi"
# #if 0
    print "should not be emitted 1"
# #if 1
    print "should not be emitted 2"
# #endif
    print "should not be emitted 3"
# #endif
    print "bye"

