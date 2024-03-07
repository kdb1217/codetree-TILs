n = int(input())
arr = list(map(int, input().split()))

def arrManager(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = arr[i] // 2

arrManager(arr)
for i in range(len(arr)):
    print(arr[i], end = " ")