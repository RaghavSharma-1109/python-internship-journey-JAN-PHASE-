import numpy as np
import time
# Python Loop Version
X_list = [1,2,3,4,5,6,7,8,9,10]
start = time.time()

y=[]
for x in X_list:
    y.append(3*(x**2)+2*x+5)

end = time.time()
print("Result from python Loops:",y)
print("Time for python Loops:",end-start)

# Numpy Verctorsation Version

X_numpy = np.array([1,2,3,4,5,6,7,8,9,10])
start = time.time()

y=3*(X_numpy**2) + 2*X_numpy + 5

end = time.time()

print("Result from Numpy Vectorisation: ",y)
print("Time for Numpy Vectorisation:", end-start)