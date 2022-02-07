import random

from numpy import *
a = floor(10 * random.random([2, 12]))
print(a)

"""hsplit 
1st argument - targer array
2nd argument - number of splits wants (number evo hovo joi jema n equal parts possible hoi)

example array x is of shape (3,11), to 3 equal parts possible nathi"""

print(hsplit(a, 3)) # will split array 'a' in to three equal parts

print(hsplit(a, (3,7))) # (3, 7) means apply split operation at 3rd and 4th indices

print(hsplit(a, (3,7,9))) # (3, 7, 9) means apply split operation at 3rd and 7th and 9th column

""":vsplit 
1st argument - targer array
2nd argument - number of splits wants (number evo hovo joi jema n equal parts possible hoi)

example array x is of shape (3,11), to 3 equal parts possible nathi"""

a.resize(12,2)
print(a)

print(vsplit(a, 3)) # split array 'a' in 3 equal parts vertically

print(vsplit(a, (3,5,8))) #split array 'a' from 3rd 5th and 8th row

"""array_split
split array in to equal or nearly equal parts"""

print(array_split(a,5))
#print(array_split(a,(1),axis = 0))
