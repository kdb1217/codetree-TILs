class DotInfo:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num

arr = []
inputNum = int(input())

for i in range(1,inputNum + 1):
    x, y = tuple(map(int, input().split()))
    arr.append(DotInfo(x, y, i))

arr.sort(key = lambda x: (abs(x.x) + abs(x.y), x.num))

for i in arr:
    print(i.num)