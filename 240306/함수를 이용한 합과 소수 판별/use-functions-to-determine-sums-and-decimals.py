a, b = tuple(map(int, input().split()))
cnt = 0

def checkPrime(i):
    if i == 1:
        return False
    for j in range(2, i):
        if i % j == 0:
            return False
    tmp = 0
    while(i > 0):
        tmp += i % 10
        i = i // 10
    if tmp % 2 == 0:
         return True
    else:
        return False

for i in range(a, b + 1):
    if checkPrime(i):
        cnt += 1

print(cnt)