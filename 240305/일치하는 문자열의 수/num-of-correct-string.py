n, String = tuple(map(str, input().split()))
n = int(n)
arr = [
    input()
    for i in range(n)
]
cnt = 0

for i in range(len(arr)):
    if String == arr[i]:
        cnt += 1

print(cnt)