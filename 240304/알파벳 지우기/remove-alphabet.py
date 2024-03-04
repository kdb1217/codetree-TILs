a = input()
b = input()

alist = list(a)
blist = list(b)

answer = 0
tmp = ""
for i in range(len(alist)):
    if alist[i] >= '0' and alist[i] <= '9':
        tmp += alist[i]


answer += int(tmp)
tmp = ""
for i in range(len(blist)):
    if blist[i] >= '0' and blist[i] <= '9':
        tmp += blist[i]

answer += int(tmp)
print(answer)