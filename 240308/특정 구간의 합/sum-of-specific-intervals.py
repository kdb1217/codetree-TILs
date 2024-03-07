a, b = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

def resultSum(a, b, arr):
    result = 0
    for i in range(a - 1, b):
        result += arr[i]
    return result

for i in range(b):
    x, y = tuple(map(int, input().split()))
    result = resultSum(x,y,arr)
    print(result)