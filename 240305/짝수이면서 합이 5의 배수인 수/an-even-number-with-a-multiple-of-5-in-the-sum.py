n = int(input())

def isTrue(n):
    if n % 2 == 0 and n % 5 == 0:
        print("Yes")
    else:
        print("No")

isTrue(n)