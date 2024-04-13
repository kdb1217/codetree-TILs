import Foundation

var arr = readLine()!.split(separator: " ").map {Int($0)!}
var (a, b) = (arr[0], arr[1])

while a < b {
    print(a, terminator: " ")
    if a % 2 == 0 {
        a += 3
    } else {
        a *= 2
    }
}