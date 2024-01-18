state = True

for i in range(5):
    n = int(input())
    if n % 3 != 0:
        state = False

if state:
    print(1)
else:
    print(0)