import Foundation

var arr = readLine()!.split(separator: " ").map {Int($0)!}
var (a, b) = (arr[0], arr[1])

print(a, terminator: " ")
while a < b {
    if a % 2 == 0 {
        a += 3
        print(a, terminator: " ")
    } else {
        a *= 2
        print(a, terminator: " ")
    }
}