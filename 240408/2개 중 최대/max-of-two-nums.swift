var arr = readLine()!.split(separator: " ").map {Int($0)!}
var a = arr[0]
var b = arr[1]
var max = a > b ? a : b
print(max)