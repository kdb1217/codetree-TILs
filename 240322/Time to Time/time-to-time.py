a, b, c, d = tuple(map(int, input().split()))

hour, mins = a, b
cntmin = 0
while True:
    if hour == c and mins == d:
        break
    
    cntmin += 1
    mins += 1

    if mins == 60:
        hour += 1
        mins = 0

print(cntmin)