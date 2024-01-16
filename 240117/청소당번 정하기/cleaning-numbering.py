n = int(input())

room = n // 2
hall = n // 3
bath = n // 12

hall -= bath
room -= (n // 6) + bath

print(room,hall,bath,sep = " ")