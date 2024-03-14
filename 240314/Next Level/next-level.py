class UserInfo:
    def __init__(self, info, lv):
        self.info = info
        self.lv = lv

info, lv = tuple(map(str, input().split()))

inputUser = UserInfo(info,lv)
example = UserInfo("codetree","10")
print(f"user {example.info} lv {example.lv}")
print(f"user {inputUser.info} lv {inputUser.lv}")