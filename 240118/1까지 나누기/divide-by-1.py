n = int(input())
answer = n
for i in range(1, n):
    answer /= i
    if answer <= 1:
        print(i)
        break