n = int(input())
answer = 0

for i in range(n):
    tmp = int(input())
    answer += tmp

answer = str(answer)
answer = answer[1:] + answer[0]
print(answer)