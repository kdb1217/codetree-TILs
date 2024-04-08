var arr = readLine()!.split(separator: " ").map {Int($0)!}

arr[0] += 8
arr[1] *= 3

print(arr[0])
print(arr[1])
print(arr[0] * arr[1])