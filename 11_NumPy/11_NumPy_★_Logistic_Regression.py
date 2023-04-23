import numpy as np
p=lambda x:(1/(1+np.exp(-(x.dot(np.array([[.1],[.5]]))-3.98)))).flatten()
exec(input().strip())