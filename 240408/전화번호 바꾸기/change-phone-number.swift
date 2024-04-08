import Foundation
var arr = readLine()!.split(separator: "-").map {Int($0)!}
print("010-\(arr[2])-\(arr[1])")