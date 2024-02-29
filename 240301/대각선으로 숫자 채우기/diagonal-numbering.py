# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))

answer = [
    [0 for _ in range(m)]
    for _ in range(n)
]

cnt = 1

for col in range(m):
    current_low = 0
    current_col = col

    while(0 <= current_col and current_low < n ):
        answer[current_low][current_col] = cnt

        cnt += 1
        current_low += 1
        current_col -= 1

for low in range(1, n):
    current_low = low
    current_col = m - 1

    while(0 <= current_col and current_low < n):
        answer[current_low][current_col] = cnt
        
        cnt += 1
        current_low += 1
        current_col -= 1

for low in range(n):
    for col in range(m):
        print(answer[low][col], end = " ")
    print()