n = int(input())

answer = [
    0 for _ in range(101)
]

for _ in range(n):
    a, b = tuple(map(int, input().split()))
    for i in range(a, b + 1):
        answer[i] += 1


print(max(answer))