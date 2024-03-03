inputString = input()
firstIndex = inputString[0]
secondIndex = inputString[1]
arr = list(inputString)

for i in range(len(arr)):
    if arr[i] == secondIndex:
        arr[i] = firstIndex

answer = "".join(arr)

print(answer)