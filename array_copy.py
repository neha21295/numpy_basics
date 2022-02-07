from numpy import *

a1 = arange(1,10)
a2 = a1.view() #create shallow copy
print(resize(a2,(3,3)))
print("a1 = ",a1)
print("a2 = ",a2)

a2[2] = 100
print("after modification")
print("a1 = ",a1)
print("a2 = ",a2)
"""we hav changed only a2[2] to 100 but in output we can see that content of a1 is also modified
to prevent we have function called copy()"""

a3 = arange(1,10)
a4 = a3.copy() #create deep copy

print("a3 = ",a3)
print("a4 = ",a4)

a4[2] = 100
print("after modification")
print("a3 = ",a3)
print("a4 = ",a4)

e = array([[2,3,4],[4,5,6],[5,6,7]])
print(full_like(e,9)) #will declare array of shape same as e(which is 3*3), but all elements will be 9
print(full(e.shape,99)) #same as full_like function