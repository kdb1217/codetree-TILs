arr = list(map(int, input().split()))

cnt = 0

for i in range(len(arr)):
    if arr[i] % 3 == 0:
        cnt = i - 1
        break

print(arr[cnt])