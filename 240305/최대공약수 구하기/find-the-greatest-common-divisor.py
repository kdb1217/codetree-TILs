n, m = tuple(map(int,input().split()))

def gcd(n,m):
    if n == m:
        print(n)
    else:
        n, m = m, n
        while(m > 0):
            n, m = m, n % m
        print(n)

gcd(n,m)