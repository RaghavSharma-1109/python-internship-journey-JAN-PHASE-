import numpy as np
A = np.random.randint(1,100,5)
B = np.random.randint(100,1000,5)
X = np.column_stack((A,B))


mean_x = np.mean(X)
std_x = np.std(X)
X_norm = (X-mean_x) / std_x

print(f"Mean of X: {mean_x}")
print(f"Standard Deveation of X: {std_x} ")
print(f"Normalized X:{X_norm}")
