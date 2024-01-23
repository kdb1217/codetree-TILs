cnt = 0
for i in range(19):
    for j in range(19):
        print(f"{i + 1} * {j + 1} = {(i + 1) * (j + 1)}",end = " ")
        if (j + 1) % 2 == 0 or j + 1 == 19:
            print()
        else:
            print("/", end = " ")