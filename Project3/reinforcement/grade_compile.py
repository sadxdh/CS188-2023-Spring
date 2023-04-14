import py_compile

sfile = "submission_autograder_original.py"
cfile = "submission_autograder.pyc"

py_compile.compile(sfile, cfile)