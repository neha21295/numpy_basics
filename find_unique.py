from numpy import *

a = array([10,20,340,10,34,5,7,28,90,62,34,8,9,6,7,5,20,7,7,6,5])

# unique_values = unique(a)
# print(unique_values)
#
# unique_values, unique_value_indices = unique(a, return_index=1)
# print(unique_value_indices)

unique_values, unique_value_indices, count_of_occurance_of_value = unique(a, return_index=1, return_counts=1)
print(unique_values)
print(unique_value_indices) #index will be of first occurance of number in an array
print(count_of_occurance_of_value)


"""in 2d array"""
b = array([[1,2,3,7,2,3,3],[8,2,5,8,0,3,3],[1,2,3,7,2,3,3]])
uni_in_column = unique(b, axis=1)
print(uni_in_column)
