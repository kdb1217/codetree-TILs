arr = []
for i in range(4):
    numArr = list(map(int, input().split()))
    arr.append(numArr)

sum = 0

for i in range(4):
    for j in range(i + 1):
        sum += arr[i][j]
    
print(sum)