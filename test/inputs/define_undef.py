#!python

# #define FOO_A
# #define FOO_B 0
# #define FOO_C 1

if __name__ == '__main__':
# #if FOO_A
    print "a"
# #endif
# #if FOO_B
    print "b"
# #endif
# #if defined("FOO_B")
    print "b defined"
# #endif
# #if FOO_C
    print "c"
# #endif
# #if defined("FOO_D")
    print "d defined"
# #endif

# #undef FOO_B
# #undef FOO_D

# #if FOO_A
    print "a"
# #endif
# #if defined("FOO_B")
    print "b defined"
# #endif
# #if FOO_C
    print "c"
# #endif
# #if defined("FOO_D")
    print "d defined"
# #endif

