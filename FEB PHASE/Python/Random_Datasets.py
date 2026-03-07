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

size = np.random.randint(500,4000,200)
bedrooms = np.random.randint(1,6,200)
age_house = np.random.randint(0,30,200)

X = np.column_stack((size,bedrooms,age_house))

mean = np.mean(X,axis=0)
variance = np.var(X,axis=0)
std = np.std(X,axis=0)

X_norm = normalize_features(X)
print(np.mean(X_norm, axis=0))
print(np.std(X_norm, axis=0))