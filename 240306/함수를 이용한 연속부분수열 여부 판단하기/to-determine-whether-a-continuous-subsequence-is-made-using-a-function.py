a, b = tuple(map(int, input().split()))

arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

def checkAnswer(arrA, arrB):
    for i in range(len(arrA) - len(arrB) + 1):
        if arrA[i: i + len(arrB)] == arrB:
            return True
    return False
    
if checkAnswer(arrA,arrB):
    print("Yes")
else:
    print("No")