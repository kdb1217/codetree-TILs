arr = []

for i in range(2):
    sum = 0
    arr2 = list(map(int, input().split()))
    arr.append(arr2)
    for j in range(len(arr2)):
        sum += arr2[j]
    print(f'{sum / len(arr2):.1f}', end = " ")

print()

for i in range(len(arr2)):
    sum = 0
    for j in range(len(arr)):
        sum += arr[j][i]
    print(f'{sum / len(arr):.1f}', end = " ")

print()

sum = 0
for i in range(len(arr)):
    for j in range(len(arr2)):
        sum += arr[i][j]
print(f'{sum / (len(arr) * len(arr2)):.1f}')