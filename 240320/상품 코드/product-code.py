class Goods:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
name,code = tuple(map(str, input().split()))
goods = [Goods("codetree",50)]
goods.append(Goods(name,int(code)))

for i in range(len(goods)):
    print(f'product {goods[i].code} is {goods[i].name}')