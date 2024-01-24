arr = list(map(int, input().split()))
result = 0
for i in range(len(arr)):
    result += arr[i]
print(result)