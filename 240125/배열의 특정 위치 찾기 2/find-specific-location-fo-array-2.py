arr = list(map(int ,input().split()))
a = 0
b = 0
for i in range(0,len(arr), 2):
    a += arr[i]

for i in range(1, len(arr), 2):
    b += arr[i]

print(abs(a - b))