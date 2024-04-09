var arr = readLine()!.split(separator: " ").map {Int($0)!}
var (a, b) = (arr[1], arr[0])
while b >= a {
    print(b, terminator: " ")
    b -= 2
}