import Foundation
let arr = readLine()!.split(separator: " ").map {Int($0)!}
let (a, b) = (arr[0], arr[1])

if a > 0 {
    for i in stride(from: 0, to: b, by: 1) {
        print(a, terminator: "")
    }
}