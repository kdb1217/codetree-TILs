n = int(input())

def printsum(n):
    if n < 10:
        return n ** 2
    
    return printsum(n // 10) + (n % 10) ** 2

answer = printsum(n)
print(answer)