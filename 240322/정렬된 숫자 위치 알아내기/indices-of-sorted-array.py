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

for i in arr:
    tmp_index = tmp.index(i)
    print(tmp_index + 1, end = " ")