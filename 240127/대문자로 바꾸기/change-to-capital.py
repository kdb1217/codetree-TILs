for i in range(5):
    arr = list(input().split())

    for j in range(len(arr)):
        print(chr(ord(arr[j]) - 32), end = " ")

    print()