let gender = Int(readLine()!)!
let age = Int(readLine()!)!

if age >= 19 {
    print(gender == 0 ? "MAN" : "WOMAN")
} else {
    print(gender == 0 ? "BOY" : "GIRL")
}