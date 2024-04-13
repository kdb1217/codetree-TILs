import Foundation

let n = Int(readLine()!)!

for i in stride(from: 1, through: n, by: 1) {
    if i % 2 == 0 || i % 3 == 0 {
        print(1, terminator: " ")
    } else {
        print(0, terminator: " ")
    }
}