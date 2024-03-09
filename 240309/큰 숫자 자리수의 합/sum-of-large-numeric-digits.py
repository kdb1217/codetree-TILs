a, b, c = map(int,input().split())

n = a * b * c

def sumNum(n):
    if n < 10:
        return n

    return sumNum(n // 10) + n % 10

answer = sumNum(n)
print(answer)