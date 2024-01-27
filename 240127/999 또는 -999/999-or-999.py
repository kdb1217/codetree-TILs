arr = list(map(int, input().split()))
maxNum = arr[0]
minNum = arr[0]

for i in range(1, len(arr)):
    if maxNum < arr[i] and arr[i] != 999:
        maxNum = arr[i]
    
    if minNum > arr[i] and arr[i] != -999:
        minNum = arr[i]

print(maxNum, minNum, sep = " ")