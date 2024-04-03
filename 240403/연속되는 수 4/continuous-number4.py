n = int(input())
arr = [
    int(input()) 
    for _ in range(n)
]
answer = 0

for i in range(n):
    if i == 0 or arr[i - 1] > arr[i]:
        cnt = 0
    else:
        cnt += 1
    if cnt > answer:
        answer = cnt

print(answer)