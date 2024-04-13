var arr = readLine()!.split(separator: " ").map {Int($0)!}
var (a, n) = (arr[0], arr[1])

for i in 1...n  {
    print(a + i * n)
}