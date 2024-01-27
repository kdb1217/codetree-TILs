arr = list(map(int, input().split()))
minarr = []
maxarr = []

for i in range(len(arr)):
    if arr[i] > 500:
        maxarr.append(arr[i])
    elif arr[i] < 500:
        minarr.append(arr[i])


print(max(minarr), min(maxarr), sep = " ")