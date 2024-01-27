arr = list(map(int, input().split()))

arr1 = [
    list(map(int ,input().split()))
    for _ in range(arr[0])
]

arr2 = [
    list(map(int ,input().split()))
    for _ in range(arr[0])
]

for i in range(arr[0]):
    for j in range(arr[1]):
        if arr1[i][j] == arr2[i][j]:
            print(0, end = " ")
        else:
            print(1, end = " ")
    print()