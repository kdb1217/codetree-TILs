n = int(input())

def pabonachi(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    
    return pabonachi(n - 1) + pabonachi(n - 2)

answer = pabonachi(n) 
print(answer)