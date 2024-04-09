var a = Int(readLine()!)!
var arr = readLine()!.split(separator: " ").map {Int($0)!}
var (b, c, d, e) = (arr[0], arr[1], arr[2], arr[3])

print(a > b ? 1 : 0)
print(a > c ? 1 : 0)
print(a > d ? 1 : 0)
print(a > e ? 1 : 0)