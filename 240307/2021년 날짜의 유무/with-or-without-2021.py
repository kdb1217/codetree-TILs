M, D = tuple(map(int, input().split()))


def checkMD(M,D):
    checknum = 0

    if M > 12:
        print("No")

    elif M <= 7 and M % 2 != 0:
        checknum = 31
        if D <= checknum:
            print("Yes")
        else:
            print("No")

    elif M <= 7 and M % 2 == 0:
        checknum = 30
        if M == 2:
            checknum = 28
        if D <= checknum:
            print("Yes")
        else:
            print("No")

    elif M >= 8 and M % 2 == 0:
        checknum = 31

        if D <= checknum:
            print("Yes")
        else:
            print("No")

    elif M >= 8 and M % 2 != 0:
        checknum = 30

        if D <= checknum:
            print("Yes")
        else:
            print("No")


checkMD(M,D)