inputString = input()
inputString = inputString.lower()
inputArr = list(inputString)

for i in range(len(inputArr)):
    if (inputArr[i] >= 'a' and inputArr[i] <= 'z') or inputArr[i].isdigit():
        print(inputArr[i],end = "")