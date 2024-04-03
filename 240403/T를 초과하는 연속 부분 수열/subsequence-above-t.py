n, t = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
answer = 0

for i in range(n):
    if i == 0 or arr[i] <= t:
        cnt = 0
    else:
        cnt += 1
    
    if answer < cnt:
        answer = cnt

print(answer)