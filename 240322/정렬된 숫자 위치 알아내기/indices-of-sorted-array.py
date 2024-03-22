class numInfo:
    def __init__(self, num, order):
        self.num = num
        self.order = order

n = int(input())
arr = []
tmp = list(map(int, input().split()))

for i in range(n):
    arr.append(numInfo(tmp[i], i))

tmp = sorted(arr, key=lambda x: (x.num, x.order))

for info in arr:
    index_in_tmp = tmp.index(info) 
    print(index_in_tmp + 1, end=" ")