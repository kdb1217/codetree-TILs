var a: Int = 5
var b: Int = 6
var c: Int = 7
var temp: Int
var temp2: Int

temp = b
temp2 = c
b = a
c = temp
a = temp2

print(a)
print(b)
print(c)