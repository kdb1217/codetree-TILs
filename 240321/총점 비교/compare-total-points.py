class StudentInfo:
    def __init__(self, name, subject1, subject2, subject3):
        self.name = name
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3

inputNum = int(input())
arr = []

for i in range(inputNum):
    name, subject1, subject2, subject3 = input().split()
    arr.append(StudentInfo(name, int(subject1), int(subject2), int(subject3)))

arr.sort(key = lambda x: x.subject1 + x.subject2 + x.subject3)
for i in arr:
    print(i.name, i.subject1, i.subject2, i.subject3)