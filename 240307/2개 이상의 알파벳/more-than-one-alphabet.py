n = input()
arr = list(n)

def countChr(arr):
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            return True
    return False

if countChr(arr):
    print("Yes")
else:
    print("No")