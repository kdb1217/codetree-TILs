arr = list(map(int, input().split()))
maxnum = arr[0]

for i in range(1, len(arr)):
    if maxnum < arr[i]:
        maxnum = arr[i]
    
print(maxnum)