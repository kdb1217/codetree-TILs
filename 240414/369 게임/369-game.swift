import Foundation
var num = Int(readLine()!)!


for i in stride(from: 1, through: num, by: 1) {
    if (i % 3 == 0) || (i / 10 == 3 || i / 10 == 6 || i / 10 == 9) || (i % 10 == 3 || i % 10 == 6 || i % 10 == 9) {
        print(0, terminator: " ")
    }
    else{
        print(i, terminator: " ")
    }
}