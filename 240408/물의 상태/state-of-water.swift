var temperature = Int(readLine()!)!

if temperature < 0 {
    print("ice")
} else if temperature >= 100 {
    print("vapor")
} else {
    print("water")
}