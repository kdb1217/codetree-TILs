arr = input().split()

a = int(arr[0])
b = int(arr[1])

if a % 2 == 0:
    a += 1
for i in range(a, b+1, 2):
    print(i,end=" ")