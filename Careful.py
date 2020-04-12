from numpy import *

#Be careful when copying Arrays

a = array([1,2,3])
b=a
print(b)

b[0] = 100

print(b)
print(a)

#Value of a also changes while changing b

#Solution

a2 = array([1,2,3])
b2 = a2.copy()
b2[0] = 100

print(b2)
print(a2)

#Value of only b2 changes and not a2