import numpy as np
def peak_indexes(x):
    a=x[1:-1]
    # np.arange(1,len(x)-1)[a>x[:-2]&a>x[2:]]
    return np.where(np.logical_and(a>x[:-2],a>x[2:]))[0]+1
def main():
    pos = peak_indexes(np.array([float(e) for e in input().split()]))
    print(*pos,sep=", ") if len(pos)>0 else print("No peaks")
exec(input().strip())

"""
main()
1 9 1 9 1 9 1 9 1 9 1
"""