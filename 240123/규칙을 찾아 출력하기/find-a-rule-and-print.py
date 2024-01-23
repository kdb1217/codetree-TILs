n = int(input())

for i in range(n):
    for j in range(n):
        if (i == 0 or i == 4 or j == 0 or j == 4):
            print("*", end = " ")
        elif j < i:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()