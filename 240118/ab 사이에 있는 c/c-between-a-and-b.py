arr = input().split()

a, b, c =  int(arr[0]), int(arr[1]), int(arr[2])
state = False
for i in range(a, b + 1):
    if i % c == 0:
        state = True

if state:
    print("YES")
else:
    print("NO")