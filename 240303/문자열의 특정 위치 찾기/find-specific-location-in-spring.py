inputString, char = tuple(map (str, input().split()))

if char in inputString:
    print(inputString.index(char))
else:
    print("No")