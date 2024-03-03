inputString, n = tuple(map(str, input().split()))
inputArr = list(inputString)

for i in range(int(n)):
    arr = list(map(str, input().split()))
    tmp = ""

    if arr[0] == "1":
        tmp = inputArr[int(arr[1]) - 1]
        inputArr[int(arr[1]) - 1] = inputArr[int(arr[2]) - 1]
        inputArr[int(arr[2]) - 1] = tmp
        answer = "".join(inputArr)
        print(answer)

    
    elif arr[0] == "2":
        for i in range(len(inputArr)):
            if inputArr[i] == arr[1]:
                inputArr[i] = arr[2]
        answer = "".join(inputArr)
        print(answer)