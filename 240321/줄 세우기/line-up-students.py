class StudentInfo:
    def __init__ (self, height, weight, num):
        self.height = height
        self.weight = weight
        self.num = num


n = int(input())
arr = []

for i in range(1,n + 1):
    height, weight = tuple(map(int, input().split()))
    arr.append(StudentInfo(height,weight,i))

arr.sort(key = lambda x: (-x.height, -x.weight, x.num))

for i in arr:
    print(f'{i.height} {i.weight} {i.num}')