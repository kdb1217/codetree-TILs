n = int(input())

cnt = 1

while n > 2:
    n = n // 2
    cnt += 1

print(cnt)