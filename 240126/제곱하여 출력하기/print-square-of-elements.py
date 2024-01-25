n = int(input())

arr = list(map(int, input().split()))

for i in range(len(arr)):
    arr[i] = arr[i] ** 2
    print(arr[i], end = " ")