n = int(input())
arr = list(map(int, input().split()))
maxNum = 0

cnt = []
for i in range(len(arr)):
    if maxNum < arr[i]:
        maxNum = arr[i]
        cnt.append(i + 1)

for i in range(len(cnt) - 1, -1, -1):
    print(cnt[i],end = ' ')