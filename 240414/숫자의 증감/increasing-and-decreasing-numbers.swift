import Foundation
var arr = readLine()!.split(separator: " ").map {String($0)}

var c = arr[0]
var n = Int(arr[1])!

if c == "A" {
    for i in 1...n {
        print(i, terminator: " ")
    }
} else if c == "D" {
    for i in 1...n {
        print(n - i, terminator: " ")
    }
}