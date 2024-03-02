inputChar = input()

arr = ["apple","banana","grape","blueberry","orange"]
cnt = 0

for i in range(len(arr)):
    if inputChar in arr[i][3] or inputChar in arr[i][2]:
        print(arr[i])
        cnt += 1

print(cnt)