a, b = tuple(map(int, input().split()))
cnt = 0

def checknum(i):
    if i % 2 == 0:
        return False
    elif i % 10 == 5:
        return False
    elif i % 3 == 0 and i % 9 != 0:
        return False
    else:
        return True

for i in range(a, b + 1):
    if checknum(i):
        cnt += 1

print(cnt)