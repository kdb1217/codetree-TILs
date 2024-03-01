answerArr = [
    [0 for _ in range(5)]
    for _ in range(5)
]

for j in range(5):
    answerArr[0][j] = 1

for i in range(5):
    answerArr[i][0] = 1

for i in range(1, 5):
    for j in range(1, 5):
        answerArr[i][j] = answerArr[i - 1][j] + answerArr[i][j - 1]

for i in range(5):
    for j in range(5):
        print(answerArr[i][j], end = " ")
    print()