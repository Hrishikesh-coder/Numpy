import numpy as np

a = np.floor(10*np.random.random((3,4)))


print(a)
print(a.shape)

print(a.ravel()) #returns the array flatenned

print(a.reshape(6,2))

print(a.T) #returns the array,transposed

print(a.T.shape)
print(a.shape)

a.resize((2,6))

print(a)

print(a.reshape(3,-1))

