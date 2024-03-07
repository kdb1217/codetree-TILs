n = int(input())

def cntsum(n):
    if n == 1:
        return 1
    
    return cntsum(n - 1) + n

answer = cntsum(n)
print(answer)