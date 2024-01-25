n = int(input())
cnt = 1
fiveCount = 0
arr = []

while fiveCount != 2:
    if n * cnt % 5 == 0:
        fiveCount += 1
    arr.append(n * cnt)
    cnt += 1

for i in range(len(arr)):
    print(arr[i], end = " ")