arr = list(map(int, input().split()))
cnt = 1
answerArr = [
    [0 for _ in range(arr[1])]
    for _ in range(arr[0])
]

for i in range(arr[0]):
    for j in range(arr[1]):
        answerArr[i][j] = cnt
        cnt += 1


for i in range(arr[0]):
    for j in range(arr[1]):
       print(answerArr[i][j], end = " ")
    print()