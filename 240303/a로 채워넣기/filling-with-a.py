inputString = input()
arr = list(inputString)

arr[1] = 'a'
arr[-2] = 'a'
inputString = "".join(arr)

print(inputString)