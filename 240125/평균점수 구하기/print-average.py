arr = list(map(float, input().split()))
total = 0

for i in range(len(arr)):
    total += arr[i]

avg = total / len(arr)

print(f"{avg:.1f}")