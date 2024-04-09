let n = Int(readLine()!)!

for i in stride(from: n, to: n * 5 + 1, by: n) {
    print(i, terminator: " ")
}