from numpy import *

a = arange(5,15) #generate arraye of elements from 5 to 19, 20 is exclusive
print(a)
print(a[2:6]) #print elements from 2nd to 5ht index, 6th index element is exclusive

"""we can also step value in slicing"""
print(a[2:9:2])

"""start element till last element"""
print(a[4:]) #4th indexed element till last element
print(a[:5])#from oth element till 4th element, 5th element is exclusive
print(a[::2])#from first to last element with step value 2

b = array([[1,2,3,4,5,6,7,8,9],[10,20,30,40,50,60,70,80,90]])
print(b[1,1:5:2]) #will access 1st row, 1st to 4th element with step value 2

b[0,:] = 5 #changing all values of 0th row to 5
print(b)

b[0,:] = [1,2,3,4,5,6,7,8,9] #changing all values of 0th row with values on RHS
print(b)