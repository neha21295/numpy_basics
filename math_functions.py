from numpy import *

"""in numpy array we do not need to apply any arithmatic operation on each element of array
we can directly apply it on entire array"""
a1 = array([1, 2, 3, -4])
a2 = array([10, 11, 12, 13])

print(a1 + a2) #addition of each elements of a1 and a2
print(a1 - 2) #reduce each elemens of a1 by 2
#like above we can appy any arithmatic operation on numpy arrays {+, -, *, /, %, //, **}
print(sin(a1))
print(log(a2))
print(mean(a1))
print(min(a1))
print(abs(a1))
print(sqrt(a2))
print(sum(a2))
print(pow(a2,2))

a = array([[1,2,3],[4,5,6]])
print(sum(a, axis = 0)) #axis = 0 means column wise addition
print(sum(a, axis = 1))  #axis = 1 means row wise addition

x = array([[1, 2, 3], [3, 4, 5]])
y = array([[1, 2, 3], [3, 4, 5]])
#print(x @ y) # '@' calculate the product of 2 matrices

#print(x.dot(y)) # this also generate the same result as '@'
"""row and column wise operation

on a 2 dimensional array

if axis = 0 it will perform column wise operation
 axis = 1 it will perform row wise operation"""
print(x.sum()) #calculate sum of each element of x
print(x.sum(axis=0)) #calculate sum of each column of x
print(x.sum(axis=1)) #calculate sum of each row of x
print(x.cumsum(axis=0)) #calculate cumelative sum column wise
print(x.cumsum(axis=1)) #calculate cumelative sum row wise