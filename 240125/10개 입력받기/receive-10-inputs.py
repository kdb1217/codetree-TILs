arr = list(map(int, input().split()))
cnt = 0
total = 0
for i in range(len(arr)):
    if arr[i] == 0:
        break
    total += arr[i]
    cnt += 1

avg = total / cnt

print(f'{total} {avg:.1f}')