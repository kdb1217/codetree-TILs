n = int(input())

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print( i // 2 * n + (i * n) + 1 + j,end = " ")
        else:
            print( i // 2 * n + i * n + 2 * (j + 1), end = " ")
    print()