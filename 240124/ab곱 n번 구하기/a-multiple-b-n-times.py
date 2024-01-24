n = int(input())

for i in range(n):
    answer = 1
    arr = input().split()
    a, b = int(arr[0]), int(arr[1])
    for j in range(a, b + 1):
        answer *= j
    print(answer)