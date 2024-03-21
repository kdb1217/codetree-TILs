class regionArr:
    def __init__(self, name, code, region):
        self.name = name
        self.code = code
        self.region = region

inputNum = int(input())
arr = []
idx = 0

for i in range(inputNum):
    name,code,region = tuple(map(str, input().split()))
    arr.append(regionArr(name,code,region))

tmp = arr[0].name

for i in range(len(arr)):
    if arr[i].name > tmp:
        tmp = arr[i].name
        idx = i

print(f"name {arr[idx].name}")
print(f"addr {arr[idx].code}")
print(f"city {arr[idx].region}")