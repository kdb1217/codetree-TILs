import Foundation

var arr = readLine()!.split(separator: " ").map {Int($0)!}
var height = Double(arr[0])
var weight = Double(arr[1])
var bmi = 10000 * weight / pow(height,2)

bmi = trunc(bmi)

print(String(format: "%.0f", bmi))
if bmi >= 25 {
    print("Obesity")
}