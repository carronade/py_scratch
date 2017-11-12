
import scipy.linalg._fblas as blas
import time
import numpy as np


x = np.ones(shape=(1000000,), dtype=np.float32, order='F')
y = np.ones(shape=(1000000,), dtype=np.float32, order='F')
t0 = time.time()
blas.caxpy(x=x, y=y, a=(2.0, 3.0))
t1 = time.time()
print t1-t0

# numpy speed benchmark
n = 3000
t0 = time.time()
sm = np.matrix(np.random.rand(n, n))
a = np.matrix(np.random.rand(2, n))
b = np.matrix(np.random.rand(n, 3))
c = sm * sm  # the same as np.matmul(sm, sm)
cNormal = (a*c)*b  # the same as np.matmul(np.matmul(a, c), b)
t1 = time.time()
print (t1-t0)
print cNormal
