arr1 = input().split()
arr2 = input().split()
arr3 = input().split()

arr1a = arr1[0]
arr1b = int(arr1[1])

arr2a = arr2[0]
arr2b = int(arr2[1])

arr3a = arr3[0]
arr3b = int(arr3[1])


def checkResult(a,b):
    if a == "Y" and b >= 37:
        return "E"
    else:
        return "A"


arr1Result = checkResult(arr1a,arr1b)
arr2Result = checkResult(arr2a,arr2b)
arr3Result = checkResult(arr3a,arr3b)

resultArr = [arr1Result,arr2Result,arr3Result]

if resultArr.count("E") >= 2:
    print("E")
else:
    print("N")