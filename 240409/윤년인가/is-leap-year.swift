let year = Int(readLine()!)!

if year % 4 == 0 {
    if year % 100 == 0 && year % 400 != 0 {
        print("false")
    } else {
        print("true")
    }
} else {
    print("false")
}