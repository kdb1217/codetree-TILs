class group:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
arr = []

for i in range(n):
    name,height,weight = input().split()
    arr.append(group(name,height,weight))

arr.sort(key = lambda x: x.height)

for group in arr:
    print(group.name, group.height, group.weight)