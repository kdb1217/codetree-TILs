n = int(input())

def strange(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    return strange(n // 3) + strange(n - 1)

print(strange(n))