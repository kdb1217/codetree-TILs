arr = input().split()

a = int(arr[0])
b = int(arr[1])

if a > b:
    big = a
    small = b
else:
    big = b
    small = a

for i in range(b, a - 1, -1):
    print(i, end=" ")