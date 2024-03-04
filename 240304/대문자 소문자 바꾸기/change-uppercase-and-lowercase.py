inputString = input()
inputArr = list(inputString)

for i in range(len(inputArr)):
    if inputArr[i] >= 'a' and inputArr[i] <= 'z':
        inputArr[i] = inputArr[i].upper()
    else:
        inputArr[i] = inputArr[i].lower()

inputString = "".join(inputArr)
print(inputString)