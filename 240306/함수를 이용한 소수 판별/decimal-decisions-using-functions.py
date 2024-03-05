a, b = tuple(map(int ,input().split()))
answer = 0

def checkPrime(n):
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True

for i in range(a, b + 1):
    if checkPrime(i):
        answer += i

print(answer)