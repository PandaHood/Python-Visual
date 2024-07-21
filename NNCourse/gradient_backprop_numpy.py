import numpy as np
import torch

# f = w * x
# f = 2 * x
X = np.array([1,2,3,4], dtype=np.float32)
Y = np.array([2,4,6,8], dtype=np.float32)

w = 0.0

# model
def forward(x):
    return w * x
# loss = Mean squared
def loss(y, y_predicted):
    return ((y_predicted - y)**2).mean()

# gradient
# MSE = 1/N * (w*x - y)
# dJ/dw = 1/N 2x*(wx-y)
def gradient(x,y,y_predicetd):
    return np.dot(2*x,y_predicetd - y).mean()

print(f'Before Training: f(5): {forward(5):.3f}')

learning_rate = 0.01
n_iters = 10

for epoch in range(n_iters):
    # forward pass prediction 
    y_pred = forward(X)
    #loss
    l = loss(Y,y_pred)
    #gradients
    dw = gradient(X,Y,y_pred)
    #update weight 
    w -= learning_rate * dw

    if epoch %1 == 0:
        print(f'epoch {epoch+1}: w = {w:.3f}, loss = {l:.3f}')

print(forward(5))