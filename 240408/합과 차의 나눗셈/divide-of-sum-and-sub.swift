import Foundation

var arr = readLine()!.split(separator: " ").map {Int($0)!}
var sum = Double(arr[0]) + Double(arr[1])
var minus = Double(arr[0] - arr[1])

var answer: Double = round(sum / minus * 100) / 100
print(String(format: "%.2f", answer))