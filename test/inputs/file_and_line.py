
# #if defined('__FILE__')
print "__FILE__ is defined"
# #endif

# #if __FILE__.endswith("file_and_line.py")
print "__FILE__.endswith('file_and_line.py')"
# #endif

# #if defined('__LINE__')
print "__LINE__ is defined"
# #endif

# #if __LINE__ == 14
print "__LINE__ is 14"
# #endif

# #if __LINE__ == 18
print "__LINE__ is 18"
# #endif
