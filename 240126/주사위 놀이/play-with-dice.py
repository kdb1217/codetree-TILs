arr = list(map(int, input().split()))
cntArray = [0] * 6

for i in range(len(arr)):
    cntArray[arr[i] - 1] += 1

for i in range(len(cntArray)):
    print(f'{i + 1} - {cntArray[i]}')