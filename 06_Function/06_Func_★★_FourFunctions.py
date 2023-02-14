def make_int_list(x):
    # Receive x as string input and convert them into int list
    # Ex: x='12 34 5' returns [12, 34, 5]
    return [int(y) for y in x.split()]
def is_odd(e):
    # Return true if e is an odd number, otherwise return false
    return int(e)%2==1
def odd_list(alist):
    # Return a list which is like alist but contains only odd numbers
    # Ex:alist = [10, 11, 13, 14, 24, 25] returns [11, 13, 25]
    ans = []
    for a in alist:
        if is_odd(a):
            ans.append(a)
    return ans
def sum_square(alist):
    # Return a sum of square of each number in alist
    # Ex: alist=[1, 3, 4] returns (1*1 + 3*3 + 4*4) which is 26
    return sum(map(lambda x:x*x, alist))
exec(input().strip())