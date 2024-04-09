let arr = readLine()!.split(separator: " ").map {Int($0)!}
let (midTerm, finalExam) = (arr[0], arr[1])

if midTerm >= 90 {
    if finalExam >= 95 {
        print(10)
    } else if finalExam >= 90 {
        print(5)
    } else {
        print(0)
    }
}