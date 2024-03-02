arr = [
    input()
    for _ in range(11)
]
cnt = 0

for i in range(len(arr) - 1):
    if arr[i][-1] == arr[-1]:
        print(arr[i])
        cnt += 1

if cnt == 0:
    print("None")