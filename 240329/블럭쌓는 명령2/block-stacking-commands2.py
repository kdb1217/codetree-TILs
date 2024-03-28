N, K = tuple(map(int, input().split()))
answer = [
    0 for _ in range(N + 1)
]

for _ in range(K):
    a, b = tuple(map(int, input().split()))
    for i in range(a, b + 1):
        answer[i] += 1

print(max(answer))