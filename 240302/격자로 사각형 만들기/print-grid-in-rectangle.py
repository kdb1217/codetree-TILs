n = int(input())

answerArr = [
    [1 for _ in range(n)]
    for _ in range(n)
]

for i in range(1, n):
    for j in range(1, n):
        answerArr[i][j] = answerArr[i - 1][j] + answerArr[i][j - 1] + answerArr[i - 1][j - 1]

for i in range(n):
    for j in range(n):
        print(answerArr[i][j], end = " ")
    print()