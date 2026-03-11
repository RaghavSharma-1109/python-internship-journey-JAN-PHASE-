from re import X
import numpy as np
class DatasetShapeError(Exception):
    pass 
class DatasetValidator:
    
    def __init__(self, X, y):
        self.X = X
        self.y = y
    def validate_shapes(self):
        if self.X.ndim != 2:
            raise DatasetShapeError('X must be 2D')
        if self.y.ndim != 1:
            raise DatasetShapeError('y must be 1D')
        if self.X.shape[0] != self.y.shape[0]:
            raise DatasetShapeError('Number of samples of X and y must be same')
    def validate_numeric(self):
        if not np.issubdtype(self.X.dtype, np.number):
            raise DatasetShapeError('Only numeric data are allowed')
        if not np.issubdtype(self.y.dtype, np.number):
            raise DatasetShapeError('Only numeric data are allowed')

    def summary(self):
        samples = self.X.shape[0]
        features = self.X.shape[1]

        return f"""Dataset Summary
---------------
Samples: {samples}
Features: {features}
"""
X = np.random.randn(200,3)
y = np.random.randn(200)

validator = DatasetValidator(X,y)

validator.validate_shapes()
validator.validate_numeric()
print(validator.summary())