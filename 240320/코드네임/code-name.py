class PersonInfo:
    def __init__(self, name, score):
        self.name = name
        self.score = score

person = []
minscore = 101
minName = ""
for _ in range(5):
    name, score = tuple(map(str, input().split()))
    person.append(PersonInfo(name,int(score)))

for i in range(len(person)):
    if person[i].score < minscore:
        minscore = person[i].score 
        minName = person[i].name

print(minName, minscore)