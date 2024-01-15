arr = input().split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

array = [a,b,c]

minnum = min(array)

if minnum == a:
    print(1, end=" ")
else:
    print(0, end=" ")

if a == b == c:
    print(1)
else:
    print(0)