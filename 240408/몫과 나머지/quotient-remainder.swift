import Foundation
var arr = readLine()!.split(separator: " ").map {Int($0)!}

print(arr[0] / arr[1], terminator: "...")
print(arr[0] % arr[1])