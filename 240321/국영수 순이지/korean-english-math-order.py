class StudentInfo:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())
arr = []
for i in range(n):
    name, kor, eng, math = input().split()
    arr.append(StudentInfo(name, int(kor), int(eng), int(math)))

arr.sort(key = lambda x : (-x.kor, -x.eng, -x.math))

for i in arr:
    print(f"{i.name} {i.kor} {i.eng} {i.math}")