a, b = tuple(map(int ,input().split()))

arr = list(map(int, input().split()))

arr.sort()
print(arr[b - 1])