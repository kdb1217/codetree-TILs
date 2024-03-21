class StudentInfo:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

arr = []

for _ in range(5):
    name, height, weight = input().split()
    arr.append(StudentInfo(name, int(height), float(weight)))

arr.sort(key = lambda x: (x.name))

print("name")
for i in arr:
    print(f"{i.name} {i.height} {i.weight}")

arr.sort(key = lambda x: -x.height)
print()

print("height")
for i in arr:
    print(f"{i.name} {i.height} {i.weight}")