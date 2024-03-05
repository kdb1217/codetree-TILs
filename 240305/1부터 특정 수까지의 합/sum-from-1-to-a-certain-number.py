n = int(input())

def add(n):
    answer = 0
    for i in range(1, n + 1):
        answer += i
    return answer // 10

print(add(n))