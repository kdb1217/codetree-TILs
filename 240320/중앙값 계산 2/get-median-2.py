n = int(input())
arr = list(map(int, input().split()))

def printNum(arr):
    tmp = sorted(arr)
    print(tmp[len(tmp) // 2], end = " ")

for i in range(len(arr)):
    if i % 2 == 0:
        printNum(arr[:i + 1])