import numpy as np

def sum_2_rows(M):
    return np.array([M[i:i+2,:].sum(0) for i in range(0,M.shape[0],2)])
def sum_left_right(M):
    return np.array([M[:,[i, i+M.shape[1]//2]].sum(1) for i in range(M.shape[0]//2)]).T
def sum_upper_lower(M):
    return np.array([M[[i, i+M.shape[0]//2],:].sum(0) for i in range(M.shape[1]//2)])
def sum_4_quadrants(M):
    # for i in range(M.shape[0]//2):
    #     print(M[[i, i+M.shape[0]//2],:][:, [i, i+M.shape[1]//2]].sum())
    return np.array([M[[i,i,i+M.shape[0]//2,i+M.shape[0]//2], [j,j+M.shape[1]//2,j,j+M.shape[1]//2]].sum() for i in range(M.shape[0]//2) for j in range(M.shape[1]//2)]).reshape(M.shape[0]//2, M.shape[1]//2)
def sum_4_cells(M):
    return np.array([M[i:i+2, j:j+2].sum() for i in range(0,M.shape[0],2) for j in range(0,M.shape[1],2)]).reshape(M.shape[0]//2, M.shape[1]//2)
def count_leap_years(years):
    years -= 543
    b = years[(years % 400 == 0) | (years % 4 == 0) & (years % 100 != 0)]
    return b.shape[0]
exec(input().strip())
#print(sum_2_rows(np.arange(36).reshape(6,6)))
#print(sum_left_right(np.arange(36).reshape(6,6)))
#print(sum_upper_lower(np.arange(36).reshape(6,6)))
#print(sum_4_quadrants(np.arange(36).reshape(6,6)))
#print(sum_4_cells(np.arange(36).reshape(6,6)))
#print(count_leap_years(np.array([2543, 2559, 2560])))
