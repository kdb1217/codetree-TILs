cnt = 0
total = 0
while True:
    n = int(input())
    if n >= 30 or n < 20:
        break
    total += n
    cnt += 1

avg = total / cnt

print("%.2f" %avg)