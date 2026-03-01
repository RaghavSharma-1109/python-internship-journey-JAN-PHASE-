import numpy as np

one_d = np.array([1,2,3,4,5,6])
two_d = np.array([[1,2,3],[4,5,6]])

# print(one_d)
# print(two_d)
# print(two_d.shape)

# 1D array addition and multiplication
print(one_d+1) # adds 1 to all element of one_d array
print(one_d*2) # multiplies 2 to all element of one_d array
# Output
# [2 3 4 5 6 7]
# [ 2  4  6  8 10 12]


# 2D array Addition and Multiplication
print(two_d+2)
print(two_d*4)
# OUTPUT
# [2 3 4 5 6 7]
# [ 2  4  6  8 10 12]
# [[3 4 5]
#  [6 7 8]]
# [[ 4  8 12]
#  [16 20 24]]