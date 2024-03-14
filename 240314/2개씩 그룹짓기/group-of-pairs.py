n = int(input())
arr = list(map(int, input().split()))

arr.sort()

answer = []
for i in range (len(arr) // 2):
    answer.append(arr[-(1 + i)] + arr[i])

print(max(answer))