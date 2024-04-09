let info1 = readLine()!.split(separator: " ").map {$0}
let info2 = readLine()!.split(separator: " ").map {$0}
let (age1, gender1) = (Int(info1[0]), info1[1])
let (age2, gender2) = (Int(info2[0]), info2[1])

var answer = 0

if age1! >= 19 || age2! >= 19 {
    if gender1 == "M" || gender2 == "M" {
        if age1! >= 19 && gender1 == "M" {
            answer = 1
        }

        if age2! >= 19 && gender2 == "M" {
            answer = 1
        }
    }
} 

print(answer)