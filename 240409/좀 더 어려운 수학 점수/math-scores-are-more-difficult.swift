let arrA = readLine()!.split(separator: " ").map {Int($0)!}
let arrB = readLine()!.split(separator: " ").map {Int($0)!}
let (aMath, aEng) = (arrA[0], arrA[1])
let (bMath, bEng) = (arrB[0], arrB[1])

if aMath > bMath {
    print("A")
} else if bMath > aMath {
    print("B")
} else {
    if aEng > bEng {
        print("A")
    } else {
        print("B")
    }
}