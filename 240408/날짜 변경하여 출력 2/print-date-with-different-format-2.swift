var day = readLine()!.split(separator: "-").map {Int($0)!}

print("\(day[2]).\(day[0]).\(day[1])")