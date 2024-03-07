n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

def cnt(arr, m):
    answer = 0
    while m >= 1:
        if m % 2 == 1:
            answer += arr[m - 1]
            m -= 1
        else:
            answer += arr[m - 1]
            m //= 2
    return answer

answer = cnt(arr,m)
print(answer)