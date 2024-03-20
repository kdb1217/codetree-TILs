a, b, c = input().split()
a = int(a)
b = int(b)
arr = [
    "" for _ in range(a)
]
answerArr = []

for i in range(a):
    arr[i] = input()

for i in range(a):
    if arr[i][0:len(c)] == c:
        answerArr.append(arr[i])

answerArr.sort()
print(answerArr[b - 1])