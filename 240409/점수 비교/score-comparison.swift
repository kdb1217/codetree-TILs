var aScore = readLine()!.split(separator: " ").map {Int($0)!}
var bScore = readLine()!.split(separator: " ").map {Int($0)!}

if aScore[0] > bScore[0] && aScore[1] > bScore[1] {
    print(1)
} else {
    print(0)
}