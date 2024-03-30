m1, d1, m2, d2 = tuple(map(int, input().split()))
day = input()
Months = [0,31,29,31,30,31,30,31,31,30,31,30,31]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
dayIndex = 0
cnt = 1

while True:
    if m1 == m2 and d1 == d2:
        break

    if days[dayIndex] == day:
        cnt += 1

    d1 += 1
    if dayIndex == 6:
        dayIndex = 0
    else:
        dayIndex += 1



    if d1 >= Months[m1]:
        m1 += 1
        d1 = 1

print(cnt)