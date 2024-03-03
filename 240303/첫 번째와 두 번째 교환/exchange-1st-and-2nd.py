inputString = input()
firstChar = inputString[0]
secondChar = inputString[1]

inputString = list(inputString)

for i in range(len(inputString)):

    if inputString[i] == firstChar:
        inputString[i] = secondChar

    elif inputString[i] == secondChar:
        inputString[i] = firstChar

answer = "".join(inputString)
print(answer)