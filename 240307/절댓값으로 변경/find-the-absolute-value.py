n = int(input())
arr = list(map(int, input().split()))

def changeabs(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])

changeabs(arr)
for i in arr:
    print(i, end = " ")