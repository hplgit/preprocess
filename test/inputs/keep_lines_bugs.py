# Test a bug where --keep-lines wasn't obeyed for directives inside
# skipped #if-blocks.

print "this is line 4"

# #ifdef UNDEFINED
# #error "UNDEFINED is defined!"
# #define BAR 1

# #endif

print "this is line 12"

# #define FOO 2
print "this is line 15"

