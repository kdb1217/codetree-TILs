import Foundation

var arr = readLine()!.split(separator: " ").map { Int($0)! }
var (a, b) = (arr[0], arr[1])

print(a >= b ? 1 : 0)
print(a > b ? 1 : 0)
print(b >= a ? 1: 0)
print(b > a ? 1: 0)