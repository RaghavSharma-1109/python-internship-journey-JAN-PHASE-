import numpy as np
def normalize_features(X):
    # computing mean along column (Feature)
    mean = np.mean(X,axis=0)
    # computing standard deviation along column
    std = np.std(X,axis=0) 
    std[std==0] =1
    # applying Normalization
    X_norm = (X-mean) / std
    return X_norm
X = np.array([
    [1,2],
    [3,4],
    [5,6]
])
print(X.shape)
normalized_X = normalize_features(X)
print(normalized_X)
print("mean:", np.mean(normalized_X, axis=0))
print("std:", np.std(normalized_X, axis=0))