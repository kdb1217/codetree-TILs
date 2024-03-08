n = int(input())
arr = list(map(int, input().split()))

n = n - 1
maxnum = 0
def findMax(n, maxnum,arr):
    if n  ==  -1:
        return maxnum
    if arr[n] > maxnum:
        maxnum = arr[n]
    return findMax((n - 1),maxnum, arr)

answer = findMax(n,maxnum,arr)
print(answer)