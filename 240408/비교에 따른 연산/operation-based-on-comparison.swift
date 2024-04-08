import Foundation
var arr = readLine()!.split(separator: " ").map {Int($0)!}
var a = arr[0]
var b = arr[1]

if a > b {
    print(a * b)
} else {
    print(b / a)
}