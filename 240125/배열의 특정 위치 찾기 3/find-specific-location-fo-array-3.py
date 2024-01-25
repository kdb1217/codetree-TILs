cnt = 0
arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        break
    else:
        cnt += 1

print(arr[cnt - 1] + arr[cnt - 2] + arr[cnt - 3])