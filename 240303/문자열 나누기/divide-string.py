inputNum = int(input())
inputArr = list(map(str, input().split()))
answer = "".join(inputArr)
cnt = 0

for i in range(len(answer)):
    if cnt == 5:
        print()
        print(answer[i],end = "")
        cnt = 1
    else:
        print(answer[i], end = "")
        cnt += 1