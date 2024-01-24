arr = input().split()
a, b = int(arr[0]), int(arr[1])
cnt = 0

for i in range(a, b + 1):
    tmp = 0
    for j in range(1, i):
        if i % j == 0:
            tmp += 1
    if tmp == 3:
        cnt += 1

print(cnt)