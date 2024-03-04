inputString = input()
arr = list(inputString)
answer = 0
for i in range(len(arr)):
    if arr[i] >= "0" and arr[i] <= "9":
        answer += int(arr[i])
print(answer)