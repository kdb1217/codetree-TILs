n = int(input())


for i in range(n):
    cnt = 0
    m = int(input())
    while m != 1:
        if m % 2 == 0:
            m = m // 2
            cnt += 1
        else:
            m = m * 3 + 1
            cnt += 1

    print(cnt)