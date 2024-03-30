n = int(input())
answer = 0

arr = [
    [0] * 201 for _ in range(201)
]

for i in range(n):
    x1, y1, x2, y2 = tuple(map(int, input().split(" ")))
    for i in range(y1,y2):
        for j in range(x1,x2):
            arr[i][j] += 1

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] >= 1:
            answer += 1

print(answer)