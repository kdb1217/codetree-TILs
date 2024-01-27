arr1 = [
    [0 for _ in range(3)]
    for _ in range(3)
]

arr2 = [
    [0 for _ in range(3)]
    for _ in range(3)
]

for i in range(3):
    tmp = list(map(int, input().split()))
    for j in range(3):
        arr1[i][j] = tmp[j]
a = input()

for i in range(3):
    tmp2 = list(map(int, input().split()))
    for j in range(3):
        arr2[i][j] = tmp2[j]

for i in range(3):
    for j in range(3):
        print(arr1[i][j] * arr2[i][j], end = " ")
    print()