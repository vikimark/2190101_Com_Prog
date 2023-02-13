def is_prime(n):
    # Check if n is a prime number
    if n <= 1:
        return False
    for k in range(2, int(n**0.5)+1):
        if n%k == 0:
            return False
    return True

def next_prime(n):
    # return the least prime number which is more than N
    ans = n+1
    found = is_prime(ans)
    while not found:
        ans += 1
        found = is_prime(ans)
    return ans
def next_twin_prime(n):
    # Return the least twin prime number which is more than N
    # twin prime number are 2 prime numbers differed by 2. For example -> (11 amd 13) or (41 and 43).
    ans = n
    n_prime = next_prime(ans)
    n_n_prime = next_prime(ans+1)
    while n_n_prime - n_prime != 2:
        ans += 1
        n_prime = next_prime(ans)
        n_n_prime = next_prime(ans+1)
    return (n_prime, n_n_prime)
exec(input().strip())