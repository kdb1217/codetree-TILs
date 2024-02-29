# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))

answer = [
    [0 for _ in range(m)]
    for _ in range(n)
]

cnt = 1

# step 1:
for start_col in range(m):
    current_row = 0
    current_col = start_col

    while 0 <= current_col and current_row < n:
        answer[current_row][current_col] = cnt

        #변수 업데이트
        current_row += 1
        current_col -= 1
        cnt += 1

for start_low in range(1, n):
    current_row = start_low
    current_col = m - 1

    while 0 <= current_col and current_row < n:
        answer[current_row][current_col] = cnt

        current_row += 1
        current_col -= 1
        cnt += 1

for row in range(n):
    for col in range(m):
        print(answer[row][col], end = " ")
    print()