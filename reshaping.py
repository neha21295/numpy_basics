from numpy import *

b = array([[1,2,3,4],[5,6,7,8]])

b.shape = (4,2)
print(b, b.shape)
c = b.transpose() #perform transpose operation on array
print(c, c.shape)

a1 = array([1,2,3,4])
a2 = array([5,6,7,8])

print(vstack([a1,a2])) #appending elements of a2 array in next line after a1 array, result in to 2d array

print(vstack([a2,a1])) #2d array

print(hstack([a1,a2])) #appaneding elements of a2 array after  a1 array in same line, result in to 1d array

print(concatenate([a1,a2])) #same as hstack


"""reshape & resize

The reshape function returns its argument with a modified shape,
whereas the resize method modifies the array itself"""
z = arange(12)

print(z)
print(z.reshape(2,6))
print("z after reshape \n",z)
print(z.resize(2,6))
print("z after resize\n",z)

"""in reshape() if we pass any argument  as -1 , means it will calculate the required argument decide 
the new shape of array"""

# print(reshape(z, (6,-1)))

"""reversing an array using flip() function"""
#print(flip(z)) #will flip horozontally as well as vertically by default

#print(flip(z, axis =0)) #column wise

print(flip(z, axis =1)) #row wise
print(z)