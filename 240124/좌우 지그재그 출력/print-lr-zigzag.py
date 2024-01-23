n = int(input())
cnt = 0
for i in range(n):
    if i % 2 == 0 and i == 0:
        for j in range(n):
            cnt += 1
            print(cnt, end = " ")
    elif i % 2 == 0:
        cnt += n
        for j in range(n):
            cnt += 1
            print(cnt, end = " ")
    else:
        cnt += n
        for j in range(n):
            print(cnt, end = " ")
            cnt -= 1
            
    print()