arr = input().split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

min = a

if a > b:
    min = b
elif a > c:
    min = c

if b > c:
    min = c

print(min)