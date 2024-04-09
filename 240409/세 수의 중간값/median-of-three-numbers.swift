let arr = readLine()!.split(separator: " ").map {Int($0)!}
let (a, b, c) = (arr[0], arr[1], arr[2])

print(b > a && b < c ? 1 : 0)