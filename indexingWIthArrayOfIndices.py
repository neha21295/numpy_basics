import random

from numpy import *

a = arange((12))**2
print(a)

b = array([3,4,6,8])

c = a[b] #all values of 'b' will act as indices of b

print(c)

"""in above example array 'a' and 'b' both are of 1D

both can be of any dimensions"""

b = array([[3, 4], [6, 7]])
d = a[b]
print(d)  # output will be always os shape of indices array


"""and target array can also be of nD
indices array can also be of nd type- 
output is of same shape as indices array"""

x = array([[0, 0, 0],
           [255, 0, 0],
           [0, 255, 0],
           [0, 0, 255],
           [255, 255, 255]])
y = array([[0, 2, 3], [0, 1, 0]])

print(x[y])
print(shape(x[y]))

"""We can also give indexes for more than one dimension.
 The arrays of indices for each dimension must have the same shape."""

a = arange(12).reshape(3,4)

print(a)

i = array([[0, 1],
           [2, 1]])

j = array([[3, 2],
           [0, 3]]) # i and j must have same shape





print(a[i, j])