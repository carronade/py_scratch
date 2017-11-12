
# run this first
import setuptools  # This is required for %%cython to run.
%load_ext Cython

# then run this as a whole (%%cython can take care of the entire input command block)
# Don't use "Execute Selection in Console", just simply copy&paste.
# adding -a option will gen html file but don't know where it is...
# Compiled code is in C:\Users\lake\.ipython\cython\Users\lake\.ipython\cython
%%cython -a
def fib_cython(n):
    if n<2:
        return n
    return fib_cython(n-1)+fib_cython(n-2)

cpdef long fib_cython_type(long n):
    if n<2:
        return n
    return fib_cython_type(n-1)+fib_cython_type(n-2)

# same speed as *.pyd
%timeit fib_cython(10)  # 8.2 us per loop
%timeit fib_cython_type(10)  # 349 ns per loop (with caching)


