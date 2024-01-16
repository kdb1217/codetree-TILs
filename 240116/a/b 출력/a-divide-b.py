arr = input().split()

a = int(arr[0])
b = int(arr[1])

c = a // b

print("%.f."%c,end = "")

a %= b

for i in range(20):
    a *= 10
    print(a//b, end="")
    a %= b