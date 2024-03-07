n = int(input())

def reverseprint(n):
    if n == 0:
        return
    reverseprint(n - 1)
    print(n, end = " ")

def printn(n):
    if n == 0:
        return
    print(n, end = " ")
    return printn(n - 1)

reverseprint(n)
print()
printn(n)