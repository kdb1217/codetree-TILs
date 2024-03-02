inputArr = input()
answer = ""
cnt = 1
for i in range(len(inputArr)):
    if i == len(inputArr) - 1:
        answer += inputArr[i] + str(cnt)
    elif inputArr[i] == inputArr[i + 1]:
        cnt += 1
    else:
        answer += inputArr[i] + str(cnt)
        cnt = 1

print(len(answer))
print(answer)