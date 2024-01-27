n = int(input())
arr = list(map(int, input().split()))
answer = 0
for i in range(n):
    for j in range(i + 1, n):
        if answer > arr[i] - arr[j]:
            answer = arr[i] - arr[j]

if answer < 0:
    print(abs(answer))
else:
    print(0)