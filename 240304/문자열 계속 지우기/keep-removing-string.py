inputString = input()
tagetString = input()
index = 0
inputArr = list(inputString)
tagetArr = list(tagetString)

while index <= len(inputArr):
    if inputArr[index: index + len(tagetArr)] == tagetArr and index <= len(inputArr) - len(tagetString):
        for i in range(index,index + len(tagetArr)):
            inputArr.pop(index)
        index = 0
    else:
        index += 1

answer = "".join(inputArr)
print(answer)