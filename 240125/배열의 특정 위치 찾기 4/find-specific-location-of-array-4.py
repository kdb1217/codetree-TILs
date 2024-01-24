arr = list(map(int, input().split()))
cnt = 0
total = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0 and arr[i] != 0:
        total += arr[i]
        cnt += 1
    elif arr[i] == 0:
        break

print(f'{cnt} {total}')