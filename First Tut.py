import numpy as np

a = np.array([1,2,3], dtype='int8')

print(a)

b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])

print(b)

print(b.ndim)

print(b.shape)

print(a.dtype)

print(a.itemsize)

print(a.size)
print(a.nbytes)