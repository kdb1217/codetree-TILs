n = int(input())
state = False

for i in range(2,n):
    if n % i == 0:
        state = True

if state:
    print("C")
else:
    print("N")