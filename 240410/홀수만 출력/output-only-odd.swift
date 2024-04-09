let arr = readLine()!.split(separator: " ").map {Int($0)!}
let (a, b) = (arr[0], arr[1])

for i in stride(from: a, to: b + 1, by: 2) {
    print(i, terminator: " ")
}