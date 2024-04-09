let arr = readLine()!.split(separator: " ").map {Int($0)!}
let (a, b) = (arr[0], arr[1])

for i in stride(from: b, to: a - 1, by: -1) {
    print(i, terminator: " ")
}