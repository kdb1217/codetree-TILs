a, b = tuple(map(str, input().split()))
b = int(b)

for i in range(b):
    inputnum = int(input())
    if inputnum == 1:
        a = a[1:] + a[0]
        print(a)
    elif inputnum == 2:
        a = a[-1] + a[:-1]
        print(a)
    elif inputnum == 3:
        a = a[-1: -(len(a) + 1): -1]
        print(a)