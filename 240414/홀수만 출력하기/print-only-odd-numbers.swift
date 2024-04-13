import Foundation

let n = Int(readLine()!)!
var arr: [Int] = []

for i in stride(from: 0, to: 5, by: 1) {
    arr.append(Int(readLine()!)!)
}

var answer = arr.filter {$0 % 3 == 0}
answer = answer.sorted()

for i in answer {
    print(i)
}