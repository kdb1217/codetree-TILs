day ,hour ,mins = tuple(map(int, input().split()))

cntmin = 0
currentDay = 11
currenthour = 11
currentmin = 11

if day >= 11 and hour >= 11 and mins >= 11:
    while True:
        if currentDay == day and currenthour == hour and currentmin == mins:
            break
        
        currentmin += 1
        cntmin += 1

        if currentmin == 60:
            currenthour += 1
            currentmin = 0

        if currenthour == 24:
            currenthour = 0
            currentDay += 1
    print(cntmin)
else:
    print(-1)