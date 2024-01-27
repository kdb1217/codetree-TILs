n = int(input())
arr = list(map(int, input().split()))
minnum = max(arr)

for i in range(n):
    for j in range(i + 1, n):
        if arr[j] - arr[i] < minnum:
            minnum = arr[j] - arr[i]

print(minnum)