a, b = tuple(map(int,input().split()))


def count3x(a, b):
    cnt = 0
    for i in range(a, b + 1):
        if  i % 3 == 0 or find369(i):
            cnt += 1
    print(cnt)


def find369(i):
    i = list(str(i))
    for x in range(len(i)):
        if i[x] == '3' or i[x] == '6' or i[x] == '9':
            return True
    return False

count3x(a,b)