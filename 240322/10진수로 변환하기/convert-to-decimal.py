n = int(input())
n = list(map(int, str(n)))
answer = 0

for i in range(len(n)):
    answer += int(n[i]) * 2 ** (len(n) - ( i + 1 ))
print(answer)