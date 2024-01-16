arr = input().split()

a = int(arr[0])
b = int(arr[1])

while a <= b:
    print(a, end=" ")
    if a % 2 == 1:
        a *= 2
    else:
        a += 3