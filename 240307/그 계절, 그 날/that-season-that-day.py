Y,M,D = map(int, input().split())

def checkDay(Y, M, D):
    season = ""
    maxday = 0
    if M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12:
        maxDay = 31
        if D <= maxDay:
            season = checkSeason(M)
            print(season)
        else:
            print(-1)

    elif M == 4 or M == 6 or M == 9 or M == 11:
        maxDay = 30
        if D <= maxDay:
            season = checkSeason(M)
            print(season)
        else:
            print(-1)
    elif M == 2:
        maxDay = 28
        if checkYear(Y):
            maxDay = 29

        if D <= maxDay:
            season = checkSeason(M)
            print(season)
        else:
            print(-1)

def checkSeason(M):
    if M >= 3 and M <= 5:
        return "Spring"
    elif M >= 6 and M <= 8:
        return "Summer"
    elif M >= 9 and M <= 11:
        return "Fall"
    elif M == 12 or M == 1 or M == 2:
        return "Winter"


def checkYear(Y):
    if Y % 4 == 0:
        if Y % 100 == 0:
            if Y % 400 == 0:
                return True
            return False
        return True
    else:
        return False
checkDay(Y,M,D)