n = int(input())

for i in range(2, n + 1):
    tmp = 1
    for j in range(2, n + 1):
        if i % j == 0:
            tmp += 1
    if tmp == 2:
        print(i, end = " ")