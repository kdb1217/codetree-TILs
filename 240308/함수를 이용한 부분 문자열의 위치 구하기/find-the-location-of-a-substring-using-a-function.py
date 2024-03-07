inputString = input()
tagetString = input()

def common(inputString,tagetString):
    for i in range(len(inputString) - (len(tagetString) - 1)):
        if inputString[i:i+len(tagetString)] == tagetString:
            return i
    return -1

answer = common(inputString,tagetString)
print(answer)