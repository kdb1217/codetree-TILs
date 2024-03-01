n, m = tuple(map(int, input().split()))

answerArr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(m):
    x, y = tuple(map(int, input().split()))
    answerArr[x - 1][y - 1] = x * y


for i in range(n):
    for j in range(n):
        print(answerArr[i][j], end = " ")
    print()