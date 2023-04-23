import numpy as np

def mult_table(nrows, ncols):
    return (np.arange(nrows)+1)[..., np.newaxis].dot((np.arange(ncols)+1)[...,np.newaxis].T)

exec(input().strip())
# print(mult_table(2,2))