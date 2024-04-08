var arr = readLine()!.split(separator: " ").map {Int($0)!}

arr[0] += arr[1]
arr[1] += arr[0]

print(arr[0], arr[1])