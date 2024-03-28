a, b = tuple(map(int, input().split()))
answer = []
if b == 4:
    while True:
        if a < 4:
            answer.append(a)
            break
        answer.append(a % 4)
        a //= 4
    
    for i in answer[::-1]:
        print(i, end = "")
else:
    while True:
        if a < 8:
            answer.append(a)
            break
        answer.append(a % 8)
        a //= 8
    
    for i in answer[::-1]:
        print(i, end = "")