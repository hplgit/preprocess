A variation on the C preprocessor that (1) works on multiple languages and (2) encodes preprocessor statements as comments in that language so syntax correctness is not broken.
This project provides a Python script: preprocess.py

There are millions of templating systems out there (most of them developed for the web). This isn't one of those, though it does share some basics: a markup syntax for templates that are processed to give resultant text output. The main difference with preprocess.py is that its syntax is hidden in comments (whatever the syntax for comments maybe in the target filetype) so that the file can still have valid syntax. A comparison with the C preprocessor is more apt.

preprocess.py is targetted at build systems that deal with many types of files. Languages for which it works include: C++, Python, Perl, Tcl, XML, JavaScript, CSS, IDL, TeX, Fortran, PHP, Java, Shell scripts (Bash, CSH, etc.) and C#. Preprocess is usable both as a command line app and as a Python module.

Here is how is works: All preprocessor statements are on their own line. A preprocessor statement is a comment (as appropriate for the language of the file being preprocessed). This way the preprocessor statements do not make an unpreprocessed file syntactically incorrect. For example:

```
preprocess -D FEATURES=macros,scc myapp.py
```

will yield this transformation:

```
...                                     ...
# #if "macros" in FEATURES
def do_work_with_macros():              def do_work_with_macros():
    pass                                    pass
# #else
def do_work_without_macros():
    pass 
# #endif
...                                     ...
```

or, with a JavaScript file:

```
...                                     ...
// #if "macros" in FEATURES
function do_work_with_macros() {        function do_work_with_macros() {
}                                       }
// #else
function do_work_without_macros() {
}
// #endif
...                                     ...
```

Despite these contrived examples preprocess has proved useful for build-time code differentiation in the Komodo build system -- which includes source code in Python, JavaScript, XML, CSS, Perl, and C/C++.

The #if expression ("macros" in FEATURES in the example) is Python code, so has Python's full comparison richness. A number of preprocessor statements are implemented:

```
#define VAR [VALUE]
#undef VAR
#ifdef VAR
#ifndef VAR
#if EXPRESSION
#elif EXPRESSION
#else
#endif
#error ERROR_STRING
#include "FILE"
```

As well, preprocess will do in-line substitution of defined variables. Although this is currently off by default because substitution will occur in program strings, which is not ideal. When a future version of preprocess can lex languages being preprocessed it will NOT substitute into program strings and substitution will be turned ON by default.