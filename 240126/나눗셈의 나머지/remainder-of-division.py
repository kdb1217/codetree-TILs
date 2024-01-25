arr = list(map(int, input().split()))
total = 0
cntArray = [0] * arr[1]
cnt = 0
while arr[0] != 0:
    cntArray[arr[0] % arr[1]] += 1
    arr[0] = arr[0] // arr[1]

for i in range(len(cntArray)):
    total += cntArray[i] ** 2

print(total)