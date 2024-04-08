import Foundation
var c: String = readLine()!
var a: Double = Double(readLine()!)!
var b: Double = Double(readLine()!)!

print(c)
a = round(a * 100) / 100
b = round(b * 100) / 100
print(String(format: "%.2f", a))
print(String(format: "%.2f", b))