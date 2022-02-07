from numpy import *

a1 = arange(12)
print("a1",a1)

a2 = reshape(a1,(2,6)) #reshape a1 one dimensional array to 2*6 array
print("a2",a2)

a3 = reshape(a1,(2,2,3))
print("a3",a3)

print(a3.flatten()) #convert multi demensional array to one dimension array

print(eye(2)) #create 2*2 identity metrix