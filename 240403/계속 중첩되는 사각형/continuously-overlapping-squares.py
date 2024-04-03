n = int(input())

arr = [
    [0] * 201 for _ in range(201)
]
tmp = 0
answer = 0

for k in range(n):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    x1, y1, x2, y2 = x1 + 100, y1 + 100, x2 + 100, y2 + 100
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = k % 2



for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] == 1:
            answer += 1

print(answer)