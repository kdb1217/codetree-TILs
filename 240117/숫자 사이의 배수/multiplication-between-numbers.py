arr = input().split()

a = int(arr[0])
b = int(arr[1])

total = 0
cnt = 0

for i in range(a, b + 1):
    if i % 5 == 0 or i % 7 == 0:
        total += i
        cnt += 1

avg = total / cnt

print("%d %.1f" %(total,avg))