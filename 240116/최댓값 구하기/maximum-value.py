arr = input().split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

max = a

if a < b:
    max = b
    if b < c:
        max = c
elif a < c:
    max = c
print(max)