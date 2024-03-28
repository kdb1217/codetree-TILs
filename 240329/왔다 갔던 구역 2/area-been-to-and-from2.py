n = int(input())
arr = [
    0 for _ in range(101)
]
tmp = 0
answer = 0

for _ in range(n):
    a, b = tuple(map(str, input().split()))
    a = int(a)

    if b == "R":
        for i in range(a):
            tmp += 1
            arr[tmp] += 1
            
    else:
        for i in range(a):
            tmp -= 1
            arr[tmp] += 1

for i in range(len(arr)):
    if arr[i] >= 2:
        answer += 1

print(answer)