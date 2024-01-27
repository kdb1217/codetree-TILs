a, b= tuple(map(int, input().split()))

answerArr = [
    [0 for _ in range(b)]
    for _ in range(a)
]
cnt = 0

for i in range(a):
    for j in range(b):
        if j == 0:
            tmp = i
            answerArr[i][j] = tmp
        elif j % 2 == 1:
            tmp += (2 * (a - (i + 1)) + 1) 
            answerArr[i][j] = tmp  
        else:
            tmp += (2 * i) + 1
            answerArr[i][j] = tmp
    


for i in range(a):
    for j in range(b):
        print(answerArr[i][j], end = " ")
    print()