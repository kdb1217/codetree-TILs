n = int(input())
arr = [
    "gray" for _ in range(200001)
]
current = 100000

for i in range(n):
    distance, direction = tuple(map(str, input().split()))
    distance = int(distance)

    if direction == "R":
        for _ in range(distance):
            arr[current] = "black"
            current += 1
        current -= 1
    else:
        for _ in range(distance):
            arr[current] = "white"
            current -= 1
        current += 1

print(arr.count("white"), arr.count("black"))