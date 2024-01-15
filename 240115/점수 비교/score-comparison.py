math = input().split()
eng = input().split()

math1 = int(math[0])
math2 = int(math[1])

eng1 = int(eng[0])
eng2 = int(eng[1])

if math1 > math2 and eng1 > eng2:
    print(1)
else:
    print(0)