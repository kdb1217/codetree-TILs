let arr = readLine()!.split(separator: " ").map {Int($0)!}
let (a, b, c) = (arr[0], arr[1], arr[2])
var max = a

if max < b {
    max = b
}

if max < c {
    max = c
}

print(max)