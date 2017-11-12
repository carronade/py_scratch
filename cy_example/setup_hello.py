
try:
    from setuptools import setup
    from setuptools import Extension
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension

from Cython.Build import cythonize
import numpy as np


inc_path = [np.get_include()]
my_file = cythonize(r"C:\Users\lake\PycharmProjects\py_scratch\infra\cy_example\hello.pyx", language='c++', include_path=inc_path, annotate=True)
setup(name='bench'
      , ext_modules=my_file
      , include_dirs=inc_path
      )



# in PyCharm console: run C:\Users\lake\PycharmProjects\untitled1\cython_example\setup_hello.py build_ext --inplace --compiler=msvc
# in cmd, use "python" rather than "run"

# code up to the "cythonize" line can be directly run in Python interactive mode to generate c/cpp and html.
# And this is equivalent to running "cython hello.pyx -a --cplus" in terminal
