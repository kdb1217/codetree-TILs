import Foundation

var arr = readLine()!.split(separator: " ").map {Int($0)!}
var a = arr.max()!
var b = arr.min()!

for i in stride(from: a, through: b, by: -1) {
    print(i, terminator: " ")
}