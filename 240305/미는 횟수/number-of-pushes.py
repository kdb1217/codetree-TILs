inputString = input()
compareString = input()
cnt = 0

for i in range(len(inputString) - 1):
    inputString = inputString[1:] + inputString[0]
    cnt += 1
    if inputString == compareString:
        break

if inputString != compareString:
    cnt = -1

print(cnt)