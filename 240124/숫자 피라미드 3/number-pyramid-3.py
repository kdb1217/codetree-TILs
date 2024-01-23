n = int(input())

for i in range(n):
    for j in range(i + 1):
        if i == 0:
            print(i + 1, end = " ")
        else:
            print((i + 1) + j * (i + 1), end = " ")
    print()