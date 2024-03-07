n = int(input())

def makeStar(n):
    if n == 0:
        return
    
    makeStar(n - 1)
    print("*" * n)

makeStar(n)