cnt = 1
def check10(cnt):
    if cnt == 9:
        return 1
    else:
        return cnt + 1



def makeSquare(N,cnt):
    for i in range(N):
        for j in range(N):
            print(cnt,end = " ")
            cnt = check10(cnt)
        print()

N = int(input())

makeSquare(N,cnt)