import numpy as np

A = np.random.randint(1,100,5)
B = np.random.randint(100,1000,5)

X = np.column_stack((A,B))

mean_x = np.mean(X, axis=0)
std_x = np.std(X, axis=0)

X_norm = (X - mean_x) / std_x

print("Matrix:\n", X)
print("Mean:", mean_x)
print("Std:", std_x)

print("Normalized Matrix:\n", X_norm)

print("Check Mean:", np.mean(X_norm, axis=0))
print("Check Std:", np.std(X_norm, axis=0))