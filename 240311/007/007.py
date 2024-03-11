class Codetree:
    def __init__(self, secretCode, meetingPoint, time):
        self.secretCode = secretCode
        self.meetingPoint = meetingPoint
        self.time = time

arr = list(map(str, input().split()))

Codetree1 = Codetree(arr[0], arr[1], int(arr[2]))

print(f"secret code : {Codetree1.secretCode}")
print(f"meeting point : {Codetree1.meetingPoint}")
print(f"time :{Codetree1.time}")