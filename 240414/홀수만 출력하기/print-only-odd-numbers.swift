import Foundation

let n = Int(readLine()!)!
var arr: [Int] = []

for i in stride(from: 0, to: n, by: 1) {
    let tmp = Int(readLine()!)!
    if tmp % 3 == 0 && tmp % 2 == 1 {
        print(tmp)
    }
}