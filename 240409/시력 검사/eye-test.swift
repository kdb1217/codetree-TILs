var leftEye = Double(readLine()!)!
var rightEye = Double(readLine()!)!

if leftEye >= 1.0 && rightEye >= 1.0 {
    print("High")
} else if leftEye >= 0.5 && rightEye >= 0.5 {
    print("Middle")
} else {
    print("Low")
}