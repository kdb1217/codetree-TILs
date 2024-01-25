arr = list(map(int, input().split()))
cntArray = [0] * 11

for i in range(len(arr)):
    if arr[i] == 0:
        break
    cntArray[arr[i] // 10] += 1

for i in range(10, 0, -1):
    print(f'{i * 10} - {cntArray[i]}')