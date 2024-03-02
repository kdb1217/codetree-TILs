inputString = input()
inputNum = int(input())

if inputNum > len(inputString):
    for i in range(len(inputString) - 1,-1,-1):
        print(inputString[i], end="")
else:
    for i in range(len(inputString) - 1,len(inputString) - (inputNum + 1), -1):
        print(inputString[i], end = "")