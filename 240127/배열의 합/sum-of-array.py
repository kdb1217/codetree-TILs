for i in range(4):
    arr = list(map(int, input().split()))
    sum_arr = 0
    for j in range(len(arr)):
        sum_arr += arr[j]
    print(sum_arr)