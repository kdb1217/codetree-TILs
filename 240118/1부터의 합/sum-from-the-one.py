n = int(input())
total = 0
cnt = 0

for i in range(100):
    total += i
    
    if total >= n:
        break
    else:
        cnt += 1
print(cnt)