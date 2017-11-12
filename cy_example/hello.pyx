
import numpy as np
cimport numpy as np
import time
import cython
cimport scipy.linalg.cython_blas as blas
cimport scipy.linalg.cython_lapack as lapack


def fib_cython(n):
    if n<2:
        return n
    return fib_cython(n-1)+fib_cython(n-2)

cpdef long fib_cython_type(long n):
    if n<2:
        return n
    return fib_cython_type(n-1)+fib_cython_type(n-2)

# This won't speed up...
@cython.locals(n=cython.int)
@cython.returns(cython.int)
def fib_cython_type_dec(n):
    if n<2:
        return n
    return fib_cython(n-1)+fib_cython(n-2)

def with_bytes():
    for n in (100000, ):
        data = 'x'*n
        start = time.time()
        b = data
        while b:
            b = b[1:]
        print 'bytes', n, time.time()-start

def with_mv():
    for n in (100000, ):
        data = 'x'*n
        start = time.time()
        b = memoryview(data)
        while b:
            b = b[1:]
        print 'memoryview', n, time.time()-start