a, b = tuple(map(int,input().split()))


def count3x(a, b):
    cnt = 0
    for i in range(a, b + 1):
        if i % 3 == 0 or find369(i):
            cnt += 1
    print(cnt)


def find369(i):
    return i % 10 == 3 or i % 10 == 6 or i % 10 == 9 or i // 10 == 3 or i // 10 == 6 or i // 10 == 9

count3x(a,b)