import Foundation

var arr = readLine()!.split(separator: " ").map {Int($0)!}
var (a, b, c) = (arr[0], arr[1], arr[2])

if arr.min()! == a {
    print(1, terminator: " ")
} else {
    print(0, terminator: " ")
}

if a == b && a == c && b == c {
    print(1, terminator: " ")
} else {
    print(0, terminator: " ")
}