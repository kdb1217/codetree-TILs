cntArray = [0] * 4

for i in range(3):
    arr = input().split()
    a = arr[0]
    b = int(arr[1])

    if a == 'Y' and b >= 37:
        cntArray[0] += 1
    elif a == 'N' and b >= 37:
        cntArray[1] += 1
    elif a == 'Y' and b < 37:
        cntArray[2] += 1
    else:
        cntArray[3] += 1

for i in range(len(cntArray)):
    print(cntArray[i], end = " ")

if cntArray[0] >= 2:
    print("E")