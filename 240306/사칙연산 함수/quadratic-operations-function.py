arr = list(map(str, input().split()))
arr[0] = int(arr[0])
arr[2] = int(arr[2])

def plus(a, o, c):
    print(f'{a} + {c} = {a + c}')

def minus(a, o, c):
    print(f'{a} - {c} = {a - c}')

def division(a, o, c):
    print(f'{a} / {c} = {a // c}')

def multiple(a, o, c):
    print(f'{a} * {c} = {a * c}')

def error():
    print("False")

if arr[1] == "+":
    plus(arr[0],arr[1],arr[2])
elif arr[1] == "-":
    minus(arr[0],arr[1],arr[2])
elif arr[1] == "/":
    division(arr[0],arr[1],arr[2])
elif arr[1] == "*":
    multiple(arr[0],arr[1],arr[2])
else:
    error()