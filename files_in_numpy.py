from numpy import  *


"""savetxt & loadtxt for text files"""
x = array([1, 2, 3, 4, 5])
y = array([6, 7, 8, 9, 0])
savetxt("numpy_file.txt", x)
b = loadtxt("numpy_file.txt")
print(b)

savez_compressed("numpy_file_with_savez", arg1=x,arg2=y)
z = load("numpy_file_with_savez.npz")
print(z)

"""save & load - for binary files"""

c = range(10)

save("numpy_file2.npy",c)
d = load("numpy_file2.npy")
print(d)

