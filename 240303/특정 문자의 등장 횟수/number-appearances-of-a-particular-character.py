inputString = input()
ebCount = 0
eeCount = 0

for i in range(len(inputString) - 1):
    if inputString[i: i + 2] == 'eb':
        ebCount += 1
    elif inputString[i: i + 2] == "ee":
        eeCount += 1

print(eeCount,ebCount,sep = " ")