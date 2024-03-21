class WeatherInfo:
    def __init__(self,date,day,weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())

arr = []
temp = []

for i in range(n):
    date, day, weather = tuple(map(str, input().split()))
    arr.append(WeatherInfo(date,day,weather))
idx = 0

for i in range(len(arr)):
    if arr[i].weather == "Rain":
        temp.append(arr[i])

tmp = "3000"
for i in range(len(temp)):
    if temp[i].date < tmp:
        tmp = temp[i].date
        idx = i

print(f"{temp[idx].date} {temp[idx].day} {temp[idx].weather}")