strA = input()
strB = input()
strC = input()

lenA = len(strA)
lenB = len(strB)
lenC = len(strC)

answerArr = [lenA,lenB,lenC]

print(max(answerArr) - min(answerArr))