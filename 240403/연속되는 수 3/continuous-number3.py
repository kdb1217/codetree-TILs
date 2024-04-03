n = int(input())
arr = [
    0 for _ in range(n)
]
answer = 0

for i in range(n):
    arr[i] = int(input())

for i in range(n):
    if i == 0 or not((arr[i - 1] > 0 and arr[i] > 0) or (arr[i - 1] < 0 and arr[i] < 0)):
        cnt = 1
        if answer < cnt:
            answer = cnt
    else:
        cnt += 1
        if answer < cnt:
            answer = cnt


print(answer)