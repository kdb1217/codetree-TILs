import Foundation
var a: Double = Double(readLine()!)!
var b: Double = Double(readLine()!)!
var c: Double = Double(readLine()!)!

a = round(a * 1000) / 1000
b = round(b * 1000) / 1000
c = round(c * 1000) / 1000

print(String(format: "%.3f", a))
print(String(format: "%.3f", b))
print(String(format: "%.3f", c))