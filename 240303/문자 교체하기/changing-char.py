a, b = tuple(map(str, input().split()))

arrA = list(a)
arrB = list(b)

arrB[0] = arrA[0]
arrB[1] = arrA[1]
answer = "".join(arrB)

print(answer)