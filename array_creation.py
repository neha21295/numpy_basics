from numpy import *
from numpy.random import *

"""by default all element in numpy array is of same type"""

a = array([1,2,3,4], dtype=int)
b = array(['a', 'b', 'c', 'd'])
c = array([1.2, 2.3, 4.5, 6.89])
d = array(['neha', 'pratik', 'john'], dtype=str)
print(a)
print(b)
print(c)
print(d)

"""optionally we can pass type of elements in numpy array
dtype is optional"""

"""linespace(start_range,end_range,stepvalue)
if we do not pass step value it is 50 by default"""
print(linspace(1,100,5)) #it will divide 1 to 100 in 20 equal parts

"""logspace(start_value,end_value)
it will return logarithmic value of all numbers between start_value and end_value"""
print(logspace(0,1))

"""arange same age range() function
arange(start_value, end_value,step_value), default step value is 1
it iterate from start_value till end_value-1
example
 range(1,4) -> output 1,2,3, not 4,it is exclusive in arange"""

print(arange(1,5))
print(arange(1,10,2))
print(arange(10,1,-2))


"""zeros and ones
to define an array of all zero or of all one
array can be of any dimensions

by default these function generate output of type float

"""
print(zeros(5))
print(zeros([2,3])) #2 rows 3 columns
print(ones(5))
print(ones([2,2,2]))

print(zeros([2,2], int))#to convert float zeros and ones array to int
print(ones([2,2,2], int))

"""full() function to initialize an all array elements with same value"""
print(full((2,2),5)) #declare 2*2 array with all values 5

z = array([[1,2,3],[3,4,5,],[6,7,8]])
print(full_like(z,100))
print(zeros_like(z))
print(ones_like(z))

"""empty() - create an array with random values and then it will be filled

The reason to use empty over zeros (or something similar) is speed -
- just make sure to fill every element afterwards!"""

print(empty([2,2]))

print(empty_like(z))

"""argmx - return the indices of maximum value in each dimension(row wise or column wise)"""

x = array([[1,2,4,6,7],[9,6,0,4,2],[7,9,5,2,4],[5,8,0,2,4],[3,5,1,2,4]])

y = argmax(x, axis= 0) #maximum from each column
print(y)

y = argmin(x, axis= 1) #minimum from each row
print(y)

"""default_rng for generation of float random values between 0 to 1"""

f = default_rng().random((2,3))
print(f)

h = floor(10 * default_rng().random((2,3)))
print(h)