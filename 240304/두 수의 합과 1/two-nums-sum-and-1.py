a, b = tuple(map(int, input().split()))

plus = str(a + b)
arr =list(plus)
cnt = 0
for i in range(len(arr)):
    if arr[i] == "1":
        cnt += 1

print(cnt)