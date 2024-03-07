n = int(input())

def cntprint(n):
    if n == 0:
        return
    
    print(n, end = " ")
    cntprint(n - 1)
    print(n, end = " ")

cntprint(n)