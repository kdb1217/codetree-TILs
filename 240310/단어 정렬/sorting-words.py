n = int(input())
arr = [
    '0' for _ in range(n)
]
for i in range(n):
    innputString = input()
    arr[i] = innputString

arr.sort()

for i in arr:
    print(i)