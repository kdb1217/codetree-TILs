arr = list(map(int, input().split()))
answer = []
for i in range(len(arr)):
    if arr[i] == 0:
        break
    answer.append(arr[i])

for i in range(len(answer) - 1, -1, -1):
    print(answer[i], end = " ")