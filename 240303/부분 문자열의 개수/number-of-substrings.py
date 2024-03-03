inputString = input()
tagetString = input()
cnt = 0

for i in range(len(inputString) - 1):
    if inputString[i: i + 2] == tagetString:
        cnt += 1

print(cnt)