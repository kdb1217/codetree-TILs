a, b = tuple(map(str, input().split()))

a = ord(a)
b = ord(b)
print(f"{a + b} {abs(a - b)}")