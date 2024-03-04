inputString = input()
arr = list(inputString)

while len(arr) > 1:
    n = int(input())
    if n < len(arr):
        arr.pop(n)
        answer = "".join(arr)
        print(answer)
    else:
        arr.pop(-1)
        answer = "".join(arr)
        print(answer)
        break