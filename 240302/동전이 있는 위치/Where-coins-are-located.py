n, m = tuple(map(int, input().split()))

answerArr = [
    [0 for j in range(n)]
    for i in range(n) 
]

for i in range(m):
    r, c = tuple(map(int, input().split()))
    answerArr[r - 1][c - 1] = 1


for i in range(n):
    for j in range(n):
        print(answerArr[i][j], end = " ")
    print()