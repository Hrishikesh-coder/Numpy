import numpy as np
from math import *

a = np.arange(10)**3
print(a)

print(a[2])

print(a[2:5])

a[:6:2] = 1000    # equivalent to a[0:6:2] = -1000; from start to position 6, exclusive, set every 2nd element to -1000
print(a)
print( a[ : :-1])                                 # reversed a
for i in a:
     print(i**(1/3))
     print(ceil(i**(1/3)))

def func(x,y):
    return 10*x+y

b = np.fromfunction(func,(5,4),dtype=int)
print(b)

print(b[2,3])

print(b[0:5,1])

print(b[:,1]) # equal to b[0:5,1]

print(b[1:3,:])

#b[-1] = b[-1,:]

c = np.array( [[[  0,  1,  2],               # a 3D array (two stacked 2D arrays)
                 [ 10, 12, 13]],
                [[100,101,102],
                [110,112,113]]])

#... represent as many ':'s required to complete all params

print(c.shape)
print(c[1,...]) #same as c[1,:,:] or c[1]

print(c[...,2]) #same as c[:,:,2]

for row in b:
    print(row)

for element in b.flat:
    print(element)