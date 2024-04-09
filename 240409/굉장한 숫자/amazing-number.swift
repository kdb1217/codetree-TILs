let a = Int(readLine()!)!

print((a % 2 == 1 && a % 3 == 0) || (a % 2 == 0 && a % 5 == 0) ? "true" : "false")