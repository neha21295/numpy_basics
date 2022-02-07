from numpy import *

a1 = array([10, 30, 50, 60, 90])
a2 = array([20, 30, 60, 80, 100])

print((a1 > a2))
print(a1 < a2)
print(a1 >= a2)
print(a1 <= a2)
print(a1 == a2)
print(a1 != a2)

print(any(a1 > a2)) #return true isf atleast one element of a1 is greater than a2
print(any(a1 >= a2)) #30 == 30, atleans one element in both array is satisfying >= condition

print(all(a1 > a2)) #check for all elements of a1 and a2 AND gate

"""logical operations on each elements of an array
logical_and - when we wants to check multiple conditions"""
print(logical_and(a1>10, a1<110))
print(logical_or(a1>10, a1<110))
print(logical_not(a1==50))
print(logical_xor(a1>10, a1==50))

"""where- check fro specific condition
same as ternary operator in c language"""
a3 = array([1,2,3,4,5])
a4 = array([-1,-2,3,10,20])
print(where(a3 % 2 == 0, a3, 0)) #if condition is true elemt of a3 will be return,else 0 will be return
print(where(a4>a3, a4,a3)) #if condition is true element of a4 will be return,etse elements of a4 will be return