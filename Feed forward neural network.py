import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def feedforward(X, weights):
    for w in weights:
        X = sigmoid(np.dot(X, w))
    return X

X = np.array([0.5, 0.1, 0.2])
weights = [np.random.rand(3, 4), np.random.rand(4, 1)]
output = feedforward(X, weights)
print(output)
