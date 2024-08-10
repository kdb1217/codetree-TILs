import Foundation

var input = readLine()!.split(separator: " ").map { Int($0)! }
let N = input[0]
let M = input[1]
var flag = false

var a = 0
var b = 0
var aCommand: [String] = []
var bCommand: [String] = []
var count = 0

for _ in 0..<N {
    let tmp = readLine()!.split(separator: " ").map { String($0) }
    for _ in 0..<Int(tmp[1])! {
        aCommand.append(tmp[0])
    }
}

for _ in 0..<M {
    let tmp = readLine()!.split(separator: " ").map { String($0) }
    for _ in 0..<Int(tmp[1])! {
        bCommand.append(tmp[0])
    }
}


func moveLeft(_ player: Int) -> Int {
    return player - 1
}

func moveRight(_ player: Int) -> Int {
    return player + 1
}




for i in 0..<aCommand.count {
    if aCommand[i] == "R" {
        a = moveRight(a)
    } else {
        a = moveLeft(a)
    }

    if bCommand[i] == "R" {
        b = moveRight(b)
    } else {
        b = moveLeft(b)
    }
    count += 1
    if a == b { 
        print(count)
        flag = true
        break
    }
}

if !flag {
    print("-1")
}