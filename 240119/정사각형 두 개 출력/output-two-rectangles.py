n = int(input())

def star(n):
    for i in range(n):
        for j in range(n):
            print("*", end = "")
        print()
        
star(n)
print()
star(n)