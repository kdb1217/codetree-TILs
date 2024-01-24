arr = list(map (int, input().split()))
total = 0
for i in range(len(arr)):
    if i % 2 == 1:
        total += arr[i]

print(f"{total} {(arr[2] + arr[5] + arr[8]) / 3:.1f}")