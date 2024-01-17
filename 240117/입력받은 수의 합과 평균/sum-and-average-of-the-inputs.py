n = int(input())
total = 0

for i in range(n):
    a = int(input())
    total += a

arr = total / n
print("%d %.1f" %(total,arr))