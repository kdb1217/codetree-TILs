n = int(input())

def odd(n):
    if n == 1:
        return 1
    return odd(n - 2) + n

def Even(n):
    if n == 0:
        return 0
    return Even(n - 2) + n

if n % 2 == 0:
    answer = Even(n)
else:
    answer = odd(n)

print(answer)