n = int(input())

arr = list(map(float, input().split()))
avg = 0
total = 0

for i in range(n):
    total += arr[i]

avg = total / n

if avg >= 4.0:
    grade = "Perfect"
elif avg >= 3.0:
    grade = "Good"
else:
    grade = "Poor"

print(f"{avg:.1f}")
print(grade)