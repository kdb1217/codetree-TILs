n = int(input())

arr = []
lencnt = 0
acnt = 0
for i in range(n):
    arr.append(input())
    lencnt += len(arr[i])
    acnt += arr[i].count("a")

print(f'{lencnt} {acnt}')