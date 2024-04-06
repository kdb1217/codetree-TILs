import Foundation
var weight: Int = 13
var gravity: Double = 0.165
var moonWeight: Double = Double(weight) * gravity
let strGravity = String(format: "%.6f", gravity)
let strMoonWeight = String(format: "%.6f", moonWeight)

print("\(weight) * \(strGravity) = \(strMoonWeight)")