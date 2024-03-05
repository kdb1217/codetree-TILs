n = int(input())

def checkYear(n):
    if n % 4 !=0:
        print("false")
    elif n % 100 == 0 and n % 400 != 0:
        print("false")
    else:
        print("true")
    
checkYear(n)