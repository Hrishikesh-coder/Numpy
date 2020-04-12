import numpy as np
from numpy import pi
a = np.array([20,30,40,50])
b = np.array([10,15,20,25])

c = a-b
print(c)

print(b**3)

print(10*np.sin(a))

print(a<35)

for i in a:
    print(i)

e = np.array([[1,1],[0,1]])
d = np.array([[2,0],[3,4]])

print(e*d)
print(e @ d) #matrix product
print(e.dot(d)) #same matrix product

f = np.ones(3,dtype=np.int32)
n = np.linspace(0,pi,3)
print(n)

o = np.exp(c*1j)
print(o)

p = np.random.random((2,3))
print(p)

print(p.sum())
print(p.min())
print(p.max())

u = np.arrange(12).reshape(3,4)
print(u)

print(u.sum(axis=0))

#u.cumsum(axis=1) #cumulative sum along each row