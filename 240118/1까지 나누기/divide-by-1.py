n = int(input())
cnt = 0
while n > 1:
    n /= cnt + 1
    cnt += 1

print(cnt)