## 1.1.0 ##

  * Move to code.google.com/p/preprocess for code hosting.
  * Re-org directory structure to assist with deployment to pypi and better installation with setup.py.
  * Pulled the "content.types" file that assists with filetype determination into "preprocess.py". This makes "preprocess.py" fully independent and also makes the "setup.py" simpler. The "-c|--content-types-path" option can be used to specify addition content types information.

## 1.0.9 ##

  * Fix the 'contentType' optional arg for #include's.
  * Add cheap XML content sniffing.

## 1.0.8 ##

  * Allow for JS and CSS-style comment delims in XML/HTML. Ideally this would deal with full lexing but that isn't going to happen soon.

## 1.0.7 ##

  * Allow explicit specification of content type.

## 1.0.6 ##

  * Add ability to include a filename mentioned in a define: '#include VAR'.

## 1.0.5 ##

  * Make sure to use the longest define names first when doing substitutions. This ensure that substitution in this line: FOO and BAR are FOOBAR will do the right thing if there are "FOO" and "FOOBAR" defines.

## 1.0.4 ##

  * Add WiX XML file extensions.
  * Add XSLT file extensions.

## 1.0.3 ##

  * TeX support (from Hans Petter Langtangen)

## 1.0.2 ##

  * Fix a bug with -k|--keep-lines and preprocessor some directives in ignored if blocks (undef, define, error, include): those lines were not kept. (bug noted by Eric Promislow)

## 1.0.1 ##

  * Fix documentation error for '#define' statement. The correct syntax is '#define VAR [VALUE](VALUE.md)' while the docs used to say '#define VAR[=VALUE]'. (from Hans Petter Langtangen)
  * Correct '! ...' comment-style for Fortran -- the '!' can be on any column in Fortran 90. (from Hans Petter Langtangen)
  * Return a non-zero exit code on error.

## 1.0.0 ##

  * Update the test suite (it had been broken for quite a while) and add a Fortran test case.
  * Improve Fortran support to support any char in the first column to indicate a comment. (Idea from Hans Petter Langtangen)
  * Recognize '.f90' files as Fortran. (from Hans Petter Langtangen)
  * Add Java, C#, Shell script and PHP support. (from Hans Petter Langtangen)

## 0.9.2 ##

  * Add Fortran support (from Hans Petter Langtangen)
  * Ensure content.types gets written to "bindir" next to preprocess.py there so it can be picked up (from Hans Petter Langtangen).

## 0.9.1 ##

  * Fully read in the input file before processing. This allows preprocessing of a file onto itself.

## 0.9.0 ##

  * Change version attributes and semantics. Before: had a version tuple. After: version is a string, version\_info is a tuple.

## 0.8.1 ##

  * Mentioned #ifdef and #ifndef in documentation (these have been there for a while).
  * Add preprocess.exe to source package (should fix installation on Windows).
  * Incorporate Komodo changes:
    * change 171050: add Ruby support
    * change 160914: Only attempt to convert define strings from the command-line to int instead of eval'ing as any Python expression: which could surprise with strings that work as floats.
    * change 67962: Fix '#include' directives in preprocessed files.

## 0.8.0 ##

  * Move hosting to trentm.com. Improve the starter docs a little bit.

## 0.7.0 ##

  * Fix [https://code.google.com/p/preprocess/issues/detail?id=](https://code.google.com/p/preprocess/issues/detail?id=): Nested #if-blocks will not be properly handled.
  * Add 'Text' type for .txt files and default (with a warn) unknown filetypes to 'Text'. Text files are defined to use to '#...'-style comments to allow if/else/.../endif directives as in Perl/Python/Tcl files.

## 0.6.1 ##

  * Fix a bug where preprocessor statements were not ignored when not emitting. For example the following should not cause an error: # #if 0 # #error womba womba womba # #endif
  * Fix a bug where multiple uses of preprocess.preprocess() in the same interpreter would erroneously re-use the same list of preprocessedFiles. This could cause false detection of recursive #include's.
  * Fix #include, broken in 0.6.0.

## 0.6.0 ##

  * substitution: Variables can now replaced with their defined value in preprocessed file content. This is turned OFF by default because, IMO, substitution should not be done in program strings. I need to add lexing for all supported languages before I can do that properly. Substitution can be turned on with the --substitute command-line option or the subst=1 module interface option.
  * Add support for preprocessing HTML files.

## 0.5.0 ##

  * Add #error, #define, #undef, #ifdef and #ifndef statements.
  * #include statement, -I command line option and 'includePath' module interface option to specify an include path
  * Add FILE and LINE default defines.
  * More strict and more helpful error messages:
    * Lines of the form "#else " and "#endif " no longer match.
    * error messages for illegal #if-block constructs
    * error messages for use of defined(BAR) instead of defined('BAR') in expressions
  * New "keep lines" option to output blank lines for skipped content lines and preprocessor statement lines (to preserve line numbers in the processed file).

## 0.4.0 ##

  * Add #elif preprocessor statement.
  * Add defined() built-in, e.g. #if defined('FOO')

## 0.3.2 ##

  * Make #if expressions Python code.
  * Change "defines" attribute of preprocess.preprocess().
  * Add -f|--force option to overwrite given output file.

## 0.2.0 ##

  * Add content types for C/C++.
  * Better module documentation.
  * You can define false vars on the command line now.
  * 'python setup.py install' works.

## 0.1.0 ##

  * First release.