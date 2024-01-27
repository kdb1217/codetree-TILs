n = int(input())
arr = list(map(int, input().split()))
maxnum = arr[0]
minnum = arr[0]

for i in range(1, len(arr)):
    if maxnum < arr[i]:
        maxnum = arr[i]
    
    if minnum > arr[i]:
        minnum = arr[i]

print(minnum, arr.count(minnum), sep = " ")