inputString = input()
inputString = inputString.upper()
inputArr = list(inputString)
for i in range(len(inputArr)):
    if inputArr[i] >= 'A' and inputArr[i] <= 'Z':
        print(inputArr[i], end = "")