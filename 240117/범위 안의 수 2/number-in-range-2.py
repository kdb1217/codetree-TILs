total = 0
cnt = 0

for i in range(10):
    a = int(input())
    if a >= 0 and a <= 200:
        cnt += 1
        total += a

arr = total / cnt
print("%d %.1f" %(total,arr))