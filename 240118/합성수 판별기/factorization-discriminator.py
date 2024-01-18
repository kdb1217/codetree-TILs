n = int(input())
state = False

for i in range(n):
    if i % n == 0:
        state = True

if state:
    print("C")
else:
    print("N")