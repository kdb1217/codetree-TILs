var arr = readLine()!.split(separator: " ").map {Int($0)!}

print(arr.reduce(0) {$0 + $1})
print(arr.reduce(0) {$0 + $1} / arr.count)