arr = list(map(int, input().split()))

avg = 0
total = 0
cnt = 0

for i in range(len(arr)):
    if arr[i] >= 250:
        break
    total += arr[i]
    cnt += 1

avg = total / cnt

print("%d %.1f" %(total, avg))