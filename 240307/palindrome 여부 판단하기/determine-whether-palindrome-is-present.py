inputString = input()

def palindrome(inputString):
    if inputString == inputString[::-1]:
        print("Yes")
    else:
        print("No")

palindrome(inputString)