n = int(input())

arr = list(map(int, input().split()))
answer = []
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        answer.append(arr[i])

for j in range(len(answer) - 1, -1, -1):
    print(answer[j], end = " ")