n = int(input())

def checkCnt(n):
    if n == 1:
        return 0 

    if n % 2 == 0:
        return checkCnt(n // 2) + 1
    else:
        return checkCnt(n // 3) + 1

result = checkCnt(n)
print(result)