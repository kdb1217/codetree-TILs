arr = []
while True:
    tmp = input()
    if tmp == "0":
        break
    else:
        arr.append(tmp)

print(len(arr))
for i in range(len(arr)):
    if i % 2 == 0:
        print(arr[i])