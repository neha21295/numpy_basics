from numpy import *

a = array([[2,4,7,9],[0,4,9,2],[3,8,1,0],[2,7,4,5]])
b = (a%2==0) #(a%2==0) will be chaecked on every single lement of array 'a', and output will be true or false
print(b)

print(any(b)) #if atleans one element in b is true
print(all(b)) # if all elements of b is ture
print(where(b == True, b, 0)) #same as conditional operator in 'c' language

a[b] = 100 #ALL elements of a is satisfying condition in 'b'(a%2 ==0) will be 100 now
print(a)