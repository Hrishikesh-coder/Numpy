import numpy as np

print(np.zeros((2,3)))

print(np.ones((4,2,2), dtype='int16'))

print(np.full((2,2),99, dtype = 'float32'))

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])


print(np.full_like(a,4)) # or np.full(a.shape,4)

#Random deci no.s

print(np.random.rand(4,2)) #np.random.random_sample(a.shape)

#Random Int

print(np.random.randint(9,size=(3,3)))

#Identity Matrix

print(np.identity(5))

#Repeat

arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis=0)

print(r1)