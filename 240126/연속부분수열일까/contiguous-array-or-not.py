arr = list(map(int,input().split()))
aarr = list(map(int,input().split()))
barr = list(map(int,input().split()))
status = False
for i in range(0, len(aarr) - len(barr) + 1):
    for j in range(len(barr)):
        if aarr[i + j] == barr[j]:
            status = True
        else:
            status = False
            break
    if status == True:
        print("Yes")
        break

if status == False:
    print("No")