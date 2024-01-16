A = input().split()
B = input().split()

aMath = int(A[0])
aEng = int(A[-1])

bMath = int(B[0])
bEng = int(B[-1])


if aMath > bMath:
    print("A")
elif aMath == bMath:
    if aEng > bEng:
        print("A")
    else:
        print("B")
else:
    print("B")