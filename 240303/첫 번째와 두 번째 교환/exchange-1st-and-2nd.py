inputString = input()
firstChar = inputString[0]
secondChar = inputString[1]

for i in range(len(inputString)):

    if inputString[i] == firstChar:
        inputString[i] = secondChar

    elif inputString[i] == secondChar:
        inputString[i] = firstChar

print(inputString)