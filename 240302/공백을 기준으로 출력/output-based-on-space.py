arrayA = input()
arrayB = input()

tmp = arrayA + arrayB
answerString = ""

for i in range(len(tmp)):
    if tmp[i] != " ":
        answerString += tmp[i]
    
print(answerString)