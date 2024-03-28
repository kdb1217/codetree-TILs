a, b = tuple(map(int, input().split()))
n = list(map(int, list(input())))
answerArr = []
answer = 0
for i in range(len(n)):
    answer += n[i] * a ** (len(n) - (i + 1))

while True:
    if answer < b:
        answerArr.append(answer)
        break
    
    answerArr.append(answer % b)
    answer //= b

for i in answerArr[::-1]:
    print(i, end = "")