
import setuptools
import pyximport; pyximport.install()

import cython_example.hello as hello
# Compiled code in C:\Users\lake\.pyxbld\lib.win-amd64-2.7\
print hello.__file__
