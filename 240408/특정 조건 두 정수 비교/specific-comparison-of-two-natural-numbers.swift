import Foundation

var arr = readLine()!.split(separator: " ").map {Int($0)!}

if arr[0] < arr[1] {
    print(1, terminator: " ")
} else {
    print(0, terminator: " ")
}

if arr[0] == arr[1] {
    print(1, terminator: " ")
} else {
    print(0, terminator: " ")
}