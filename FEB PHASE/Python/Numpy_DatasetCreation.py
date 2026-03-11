import numpy as np

samples = 200
features = 3

X = np.random.randn(samples, features)

mean = np.mean(X, axis=0)
std = np.std(X, axis=0)

X_norm = (X - mean) / std

print("Mean:", mean)
print("Std:", std)

print("Normalized Mean:", np.mean(X_norm, axis=0))
print("Normalized Std:", np.std(X_norm, axis=0))