n = int(input())
arr = list(map(int, input().split()))
cntArr = [0] * 9

for i in range(len(arr)):
    cntArr[arr[i] - 1] += 1

for i in range(len(cntArr)):
    print(cntArr[i])