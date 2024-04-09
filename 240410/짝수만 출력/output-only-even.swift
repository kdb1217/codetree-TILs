let arr = readLine()!.split(separator: " ").map {Int($0)!}
var (a, b) = (arr[0], arr[1])

while(a <= b) {
    print(a, terminator: " ")
    a += 2
}