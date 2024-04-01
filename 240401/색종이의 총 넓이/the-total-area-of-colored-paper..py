n = int(input())
answer = 0

arr = [
    [0] * 201 for _ in range(201)
]

for i in range(n):
    a, b= tuple(map(int, input().split()))
    a, b = a + 100, b + 100

    for i in range(b, b + 8):
        for j in range(a, a + 8):
            arr[i][j] += 1

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] >= 1:
            answer += 1

print(answer)