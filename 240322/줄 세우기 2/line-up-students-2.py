class StudentInfo:
    def __init__(self, height, weight, num):
        self.height = height
        self.weight = weight
        self.num = num

inputNum = int(input())
arr = []

for i in range(1, inputNum + 1):
    height, weight = tuple(map(int, input().split()))
    arr.append(StudentInfo(height,weight,i))

arr.sort(key = lambda x: (x.height, -x.weight))

for i in arr:
    print(i.height, i.weight, i.num)