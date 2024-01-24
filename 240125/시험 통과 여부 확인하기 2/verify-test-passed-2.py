n = int(input())
cnt = 0
for i in range(n):
    arr = list(map(int, input().split()))
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    avg = total / len(arr)
    if avg >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")


print(cnt)