var arr = readLine()!.split(separator: " ").map {Int($0)!}
var a = arr[0]
var b = arr[1]

print(a >= b ? 1 : 0)
print(a > b ? 1 : 0)
print(b >= a ? 1 : 0)
print(b > a ? 1 : 0)
print(a == b ? 1 : 0)
print(a != b ? 1 : 0)