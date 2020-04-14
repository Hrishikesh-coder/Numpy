import numpy as np

a = np.arange(12)**2
i = np.array([0,1,8,9,11])    # an array of indices

print(a)

print(a[i])    #the elements of a at the positions i

j = np.array([[3,4],[9,7]])  # a bidimensional array of indices

print(a[j])

palette = np.array( [ [0,0,0],

                       [255,0,0],
                       [0,255,0],
                     [0,0,255],
                     [255,255,255] ] )
image = np.array( [ [ 0, 1, 2, 0 ],           # each value corresponds to a color in the palette
                [ 0, 3, 4, 0 ]  ] )
print(palette[image])

a = np.arange(12).reshape(3,4)
print(a)

i = np.array([[0,1],
              [1,2]])    # indices for the first dim of a

j = np.array([[2,1],
             [3,3]])     # indices for the second dim

print(a[i,j])

print(a[i,2])

print(a[:,j])             #i.e. , a[:,j]

l = [i,j]

print(a[l])   #equivalent to a[i,j]

time = np.linspace(20,145,5)
data = np.sin(np.arange(20)).reshape(5,4)

print(time)

print(data)

ind = data.argmax(axis=0)

print(ind)

time_max = time[ind]

data_max = data[ind, range(data.shape[1])]   #=> data[ind[0],0], data[ind[1],1]...

print(time_max)

print(data_max)

print(np.all(data_max == data.max(axis=0)))

a  = np.arange(5)

print(a)

a[[1,3,2,4]] =  0

print(a)

b = np.arange(5)

print(b)

b[[0,0,2]]  = [1,2,3]

print(b)