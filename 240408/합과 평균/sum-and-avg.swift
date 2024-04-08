import Foundation
var arr = readLine()!.split(separator: " ").map {Int($0)!}
var sum = Double(arr[0] + arr[1])
var ave = String(format: "%.1f", sum / Double(arr.count))

print(Int(sum), ave)