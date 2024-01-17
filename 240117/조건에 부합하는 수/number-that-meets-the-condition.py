a = int(input())

for i in range(1, a + 1):
    tmp = i // 8
    if (i % 2 == 0 and i % 4 != 0) or ( tmp % 2 == 0 ) or (i % 7 < 4):
        continue
    print(i, end = " ")