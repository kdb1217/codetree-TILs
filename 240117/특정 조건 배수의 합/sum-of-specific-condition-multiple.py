arr = input().split()

a = int(arr[0])
b = int(arr[1])
tmp = a

if a > b:
    a = b
    b = tmp

total = 0

for i in range(a, b + 1):
    if i % 5 == 0:
        total += i

print(total)