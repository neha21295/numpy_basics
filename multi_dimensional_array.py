from numpy import *

a = array([1,2,3,4,5])
b = array([[1,2,3],
           [4,5,6]])
c = array([[[1,2],
            [3,4]],
           [[5,6],
           [7,8]]])

print("one dimension array \n", a)
print("two dimension array\n", b)
print("three dimension array\n", c)

"""ndim() to find the dimensions of an array"""
print(a.ndim)
print(b.ndim)
print(c.ndim)

"""shape() function- give shape of array in form of[x,y]
where x - number of rows
y - number of columns"""
print(a.shape)
print(b.shape)
print(c.shape)


"""size() - gives total size of array(total number of elements in an array)"""
print(a.size)
print(b.size)
print(c.size)

"""itmesize() gives size of element in an array, depends on type of data array is holding"""
print(a.itemsize)
print(b.itemsize)
print(c.itemsize)

"""dtype() gives to datatype of elements in an array"""
print(a.dtype)
print(b.dtype)
print(c.dtype)

"""nbytes() gives total bytes require to store an entire array"""
print(a.nbytes) #5*4 = 20, 5 elements, 4 bytes for each element of type int32
print(b.nbytes) #6*4 = 24, 6 elements, 4 bytes for each element of type int32
print(c.nbytes) #8*4 = 32, 8 elements, 4 bytes for each element of type int32