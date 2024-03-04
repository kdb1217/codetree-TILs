inputString = input()

print(inputString)

for i in range(-1,-(len(inputString) + 1), -1):
    answer = inputString[i:] + inputString[:len(inputString) + i]
    print(answer)