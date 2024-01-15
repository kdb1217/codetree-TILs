arr = input().split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

min = a

if min > b:
    min = b
elif min > c:
    min = c
print(min)