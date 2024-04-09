let arr = readLine()!.split(separator: " ").map {Int($0)!}
let (a, b) = (arr[1], arr[0])

for i in stride(from: b, to: a - 1, by: -2) {
    print(i, terminator: " ")
}