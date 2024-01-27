n = int(input())
arr = list(map(int, input().split()))
maxNum = 0

for i in range(len(arr)):
    if arr.count(arr[i]) == 1:
        if maxNum < arr[i]:
            maxNum = arr[i]


if maxNum == 0:
    print(-1)
else:
    print(maxNum)