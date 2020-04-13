import time

import numpy as np
import sys





a = np.arange(12)

b = a #no new object is created

print(b is a) # a and b are two names for the same ndarray object

b.shape = 3,4 #changes the shape of a

print(a.shape)

def func(x):
    print(id(x))

print(id(a))

func(a)

#Shallow copy

c = a.view()
print(c is a)

print(c.base is a) #c is a view of the data owned by a

print(c.flags.owndata)

c.shape = 2,6 #a's shapee doesnt change

print(a.shape)

c[0,4] = 1234 #a's data changes

print(a)

#Slicing an array returns a view of it

s = a[:,1:3]
s[:] = 10   #s[:] is a view of s

print(a)

#Deep copy

d = a.copy()   # a new array object with new data is created

print(d is a)

print(d.base is a)

d[0,0] = 9999 #d doesnt share anything with a

print(a)



a = np.arange(int(1e8))


print(a)

b = a[:100].copy()

print(b)

del a
