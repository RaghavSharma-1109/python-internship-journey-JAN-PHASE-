import numpy as np
X = np.array([1,2,3,4,5])
y = np.array([7,11,15,19,23])

w = 0
b = 0
lr = 0.01
epochs = 1000
n = len(X)
for epoch in range(epochs):
    y_pred = w*X +b
    error = y - y_pred
    loss = np.mean(error**2)
    dw = (-2/n)*np.sum(X*error)
    db = (-2/n)*np.sum(error)

    w = w-lr*dw
    b = b-lr*db

    if(epoch%100==0):
        print("Epoch:", epoch, "Loss:", loss)
print("Final w:", w)
print("Final b:", b)
print("Final loss:", loss)