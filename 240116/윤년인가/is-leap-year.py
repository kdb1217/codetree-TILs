y = int(input())

find = "true"
if y % 4 == 0:
    find = "true"
    if y % 100 == 0:
        find = "false"
        if y % 400 == 0:
            find = "true"
else:
    find = "false"

print(find)