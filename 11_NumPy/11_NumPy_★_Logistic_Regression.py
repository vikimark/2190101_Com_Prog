import numpy as np

def p(x):
    p = 1/(1+np.exp(-(x.dot(np.array([[0.1], [0.5]])) -3.98)))
    return p

print(p(np.array([[80, 2.50], [1, 4.00]])))