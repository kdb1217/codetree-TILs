arr = [
    [0] * 2001 for _ in range(2000)
]
answer = 0
for a in range(3):
    x1, y1, x2, y2 = tuple(map(int, input().split(" ")))
    x1, y1 = x1 + 1000, y1 + 1000
    x2, y2 = x2 + 1000, y2 + 1000

    for i in range(y1, y2):
        for j in range(x1, x2):
            if a == 2:
                arr[i][j] = 0
            else:
                arr[i][j] += 1

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]:
            answer += 1

print(answer)