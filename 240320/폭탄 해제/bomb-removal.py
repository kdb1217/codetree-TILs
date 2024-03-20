class Boom:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

code, color, second = tuple(map(str, input().split()))

boom = Boom(code,color,int(second))

print(f"code : {boom.code}")
print(f"color : {boom.color}")
print(f"second : {boom.second}")