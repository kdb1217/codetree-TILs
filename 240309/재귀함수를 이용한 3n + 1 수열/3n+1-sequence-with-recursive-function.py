n = int(input())

def test(n):
    if n <= 1:
        return 0
    if n % 2 == 0:
        return test(n // 2) + 1
    else:
        return test(n * 3 + 1) + 1
    
answer = test(n)
print(answer)