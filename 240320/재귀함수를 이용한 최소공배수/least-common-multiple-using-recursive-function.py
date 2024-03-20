n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def array_lcm(arr, idx):
    if idx == len(arr) - 1:
        return arr[idx]
    return lcm(arr[idx], array_lcm(arr, idx + 1))


arr.sort(reverse=True)
result = array_lcm(arr, 0)
print(result)