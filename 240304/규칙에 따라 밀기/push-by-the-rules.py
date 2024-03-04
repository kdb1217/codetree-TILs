inputString = input()
command = input()
inputArr = list(inputString)
commandArr = list(command)


for i in range(len(commandArr)):
    if commandArr[i] == 'L':
        inputString = inputString[1:] + inputString[0]
    elif commandArr[i] == 'R':
        inputString = inputString[-1] + inputString[: -1]

print(inputString)