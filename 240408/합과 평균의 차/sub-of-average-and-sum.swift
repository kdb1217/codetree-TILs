var arr = readLine()!.split(separator: " ").map {Int($0)!}

var total = arr.reduce(0) {$0 + $1}
var avg = total / arr.count

print(total)
print(avg)
print(total - avg)