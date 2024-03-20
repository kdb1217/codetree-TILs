n = int(input())

arr = list(map(int,input().split()))
arr.sort(reverse = True)

def gcd(a, b):
    if a < b:
        a, b = b, a
    
    while (b > 0):
        a, b = b, a % b
        return a


def lcm(idx, arr):
    idx == len(arr)
    if b == arr[-1]:
        return arr[idx - 1] * [idx] / gcd(arr[idx - 1], arr[idx])
    else:
        return lcm(a * b /gcd (arr[idx - 1],arr[idx]), idx + 1)