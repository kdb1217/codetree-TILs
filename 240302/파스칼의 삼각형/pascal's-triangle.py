n = int(input())

answerArr = [
    [1 for j in range(i + 1)]
    for i in range(n)
]

for i in range(n):
    for j in range(i):
        if (i - 1 >= 0 and j  > 0) and i - 1 > 0:
            answerArr[i][j] = answerArr[i - 1][j - 1] + answerArr[i - 1][j]

for i in range(n):
    for j in range(i + 1):
        print(answerArr[i][j], end = " ")
    print()