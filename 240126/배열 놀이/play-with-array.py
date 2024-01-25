repeatArray = list(map(int, input().split()))
numArray = list(map(int,input().split()))

for i in range(repeatArray[1]):
    arr = list(map(int,input().split()))
    if arr[0] == 1:
        print(numArray[arr[1] - 1])
    elif arr[0] == 2:
        if arr[1] in numArray:
            print(numArray.index(arr[1]) + 1)
        else:
            print(0)
    else:
        for i in range(arr[1] - 1, arr[2]):
            print(numArray[i], end = " ")
        print()