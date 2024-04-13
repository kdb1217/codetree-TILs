import Foundation
var cnt: Int = 0

for i in 0...9 {
    let tmp = Int(readLine()!)!
    if tmp % 2 == 1 {
        cnt += 1
    }
}
print(cnt)