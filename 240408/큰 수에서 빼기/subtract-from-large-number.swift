var arr = readLine()!.split(separator: " ").map {Int($0)!}

if arr[0] > arr[1] {
    print(arr[0] - arr[1])
} else {
    print(arr[1] - arr[0])
}