while True:
    a = input().split()
    x = int(a[0])
    y = int(a[1])

    print(x * y)
    if a[2] == "C":
        break