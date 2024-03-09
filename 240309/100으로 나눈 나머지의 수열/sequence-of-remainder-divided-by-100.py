n = int(input())

def division(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4
    
    return division(n - 1) * division(n - 2) % 100


answer = division(n)
print(answer)