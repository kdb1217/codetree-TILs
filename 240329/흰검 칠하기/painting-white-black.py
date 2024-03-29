n = int(input())
arr = [
    []
    for _ in range(50)
]
tmp = 25
white = 0
black = 0
gray = 0
for _ in range(n):
    distance, direction = tuple(map(str, input().split()))
    distance = int(distance)

    if direction == "R":
        if distance == 1:
            arr[tmp].append("black")
        else:
            for _ in range(distance):
                arr[tmp].append("black")
                tmp += 1
            tmp -= 1
            
            
    else:
        if distance == 1:
            arr[tmp].append("white")
        else:
            for _ in range(distance):
                arr[tmp].append("white") 
                tmp -= 1
            tmp += 1                
for x in arr:
    if len(x) > 0:
        if x.count("black") >= 2 and x.count("white") >= 2:
            gray += 1
        elif x[-1] == "black" :
            black += 1
        elif x[-1] == "white":
            white += 1

print(white, black, gray)