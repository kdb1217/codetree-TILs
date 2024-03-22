m1, d1, m2, d2 = tuple(map(int, input().split()))


num_of_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

month = m1
day = d1
while True:
    day += 1
    cnt_days += 1

    if day > num_of_days[month]:
        month += 1
        day = 0
    
    if month == m2 and day == d2:
        break

print(cnt_days)