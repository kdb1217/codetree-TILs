n = int(input())
arr = list(str(n))
answer = 0

for i in range(len(arr)):
    answer += int(arr[i])

print(answer)