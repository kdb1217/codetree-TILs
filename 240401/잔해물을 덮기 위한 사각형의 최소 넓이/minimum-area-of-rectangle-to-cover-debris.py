arr = [
   [0] * 2001 for _ in range(2001) 
]
answer = 0
maxX = 0
maxY = 0
for x in range(1, 3):
    x1,y1,x2,y2 = tuple(map(int, input().split()))
    x1,y1,x2,y2 = x1 + 1000, y1 + 1000, x2 + 1000, y2 + 1000

    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] += x

for i in range(len(arr)):
    if arr[i].count(1) > maxX:
        maxX = arr[i].count(1)

for i in range(len(arr)):
    tmp = 0
    for j in range(len(arr)):
        if arr[j][i] == 1:
            tmp += 1
    if tmp > maxY:
        maxY = tmp
        
print(maxX * maxY)