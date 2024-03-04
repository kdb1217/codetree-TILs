inputString = input()
inputArr = list(inputString)

for i in range(len(inputString)):
    if inputArr[i] == 'e':
        inputArr.pop(i)
        break

answer = "".join(inputArr)
print(answer)