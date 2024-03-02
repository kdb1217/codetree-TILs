n = int(input())

arr = []
lencnt = 0
acnt = 0
for i in range(n):
    arr.append(input())
    lencnt += len(arr[i])
    if arr[i][0] == "a":
        acnt += 1

print(f'{lencnt} {acnt}')