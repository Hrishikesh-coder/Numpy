import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])


print(a)

print(a[1,5]) # same as a[1,-2]

print(a[0, :])

print(a[:,2])

print(a[0, 1:6:2])

a[1,5]= 20

print(a)

a[:,2]=5

print(a)

#3d

b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

#Get specific element(work outside in)
print(b[0,1,1]) #or b[:,1,0]

#replace
b[:,1,:] = [[9,9],[8,8]]
print(b)