import Foundation

let a: Double = 5.26
let b: Double = 8.27
var result = String(format: "%.3f",round(a * b * 1000) / 1000)

print(result)