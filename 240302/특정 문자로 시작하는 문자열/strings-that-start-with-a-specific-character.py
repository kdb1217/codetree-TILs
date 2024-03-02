n = int(input())

arr = [
    input()
    for _ in range(n + 1)
]
cnt = 0
total = 0

for i in range(n):
    if arr[i][0] == arr[-1]:
        cnt += 1
        total += len(arr[i])


print(f'{cnt} {total / cnt:.2f}')