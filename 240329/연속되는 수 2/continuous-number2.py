n = int(input())
answer = 0
arr = [
    0 for _ in range(n)
]
for i in range(n):
    arr[i] = int(input())

for i in range(n):
    if i == 0 or arr[i - 1] != arr[i]:
        cnt = 1
    else:
        cnt += 1
        if answer < cnt:
            answer = cnt


print(answer)