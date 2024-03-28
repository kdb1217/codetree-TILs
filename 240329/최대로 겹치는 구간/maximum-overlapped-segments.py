n = int(input())
arr = [
    0 for _ in range(200)
]

for _ in range(n):
    a, b = tuple(map(int, input().split()))
    for i in range(a + 100, b + 100):
        arr[i] += 1

print(max(arr))