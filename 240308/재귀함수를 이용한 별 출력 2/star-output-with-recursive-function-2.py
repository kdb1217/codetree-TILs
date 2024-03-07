n = int(input())

def makeStar(n):
    if n == 0:
        return
    
    print("* " * n)
    makeStar(n - 1)
    print("* " * n)

makeStar(n)