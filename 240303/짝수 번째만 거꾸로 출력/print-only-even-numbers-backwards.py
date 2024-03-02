n = input()
answer = ""
for i in range(1,len(n),2):
    answer += n[i]

for i in range(len(answer) - 1, -1, -1):
    print(answer[i],end = "")