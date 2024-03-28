n = list(map(int, list(input())))
answer = 0
answerArr = []
for i in range(len(n)):
    answer += int(n[i]) * 2 ** (len(n) - ( i + 1 ))
answer *= 17

while True:
    if answer < 2:
        answerArr.append(answer)
        break
    
    answerArr.append(answer % 2)
    answer //= 2

for i in answerArr[::-1]:
    print(i, end = "")