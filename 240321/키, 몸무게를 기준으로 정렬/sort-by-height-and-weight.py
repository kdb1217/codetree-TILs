class PeopleInfo:
    def __init__ (self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

inputNum = int(input())
arr = []

for i in range(inputNum):
    name, height, weight = input().split()
    arr.append(PeopleInfo(name, int(height), int(weight)))


arr.sort(key = lambda x: (x.height, -x.weight))
for i in arr:
    print(i.name, i.height, i.weight)