import Foundation
var arr = readLine()!.split(separator: ".").map {Int($0)!}

print("\(arr[1])-\(arr[2])-\(arr[0])")