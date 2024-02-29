n = int(input())

answer = [
    [0 for _ in range(n)]
    for _ in range(n)
]
cnt = 1
row = n - 1
col = n - 1

while answer[n - 1][0] == 0:
    if col % 2 != 0 and row !=0:
        answer[row][col] = cnt

        cnt += 1
        row -= 1

    elif row == 0 and col % 2 != 0:
        answer[row][col] = cnt

        cnt += 1
        col -= 1

    elif row == 0 and col % 2 == 0:
        answer[row][col] = cnt

        row += 1
        cnt += 1

    elif row != n - 1 and col % 2 == 0:
        answer[row][col] = cnt

        row += 1
        cnt += 1

    elif row == n - 1 and col % 2 == 0:
        answer[row][col] = cnt

        col -= 1
        cnt += 1




for i in range(n):
    for j in range(n):
        print(answer[i][j], end = " ")
    print()