import numpy as np
from numpy import newaxis


a = np.floor(10*np.random.random((2,2)))

print(a)

b = np.floor(10*np.random.random((2,2)))

print(b)

print(np.vstack((a,b)))

print(np.hstack((a,b)))

print(np.column_stack((a,b)))

x  = np.array([4.,2.])
y = np.array([3.,8.])

print(np.column_stack((a,b)))

print(np.hstack((a,b)))


print(x[:,newaxis])

print(np.column_stack((a[:,newaxis],b[:,newaxis])))

print(np.hstack((a[:,newaxis],b)))

print(np.r_[1:4,0,4])