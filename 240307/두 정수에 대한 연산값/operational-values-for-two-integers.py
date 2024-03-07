a, b = tuple(map(int, input().split()))

def printSum(a, b):
    if a < b:
        a *= 2
        b += 25
    else:
        b *= 2
        a += 25
    return a, b

a, b = printSum(a,b)
print(a, b)