
import random
import datetime
import calendar

tempList = ["freezing", "cold", "cool", "warm", "hot"]
precList = ["snowing", "sleet", "raining", "drizzling", "foggy", "overcast", "cloudy", "clear"]
windList = ["light", "strong", "howling"]
timeList = ["midnight", "the small hours", "early morning", "late morning", "midday", "early afternoon", "late afternoon", "evening"]
terrainList = ["plains", "forest", "dark forest", "hills", "mountains", "high mountains", "lake", "river", "marshlands", "bog", "coast"]
seasonList = ["summer", "autumn", "winter", "spring"]
monthList = ["na", "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
snowDepth = ["none", "light", "medium", "heavy"]
road = bool


todayDate = datetime.datetime(1272, 5, 1)
dayPart = 0
currentLocation = random.randint(0, 9)
# currentMonth = random.randint(1, 12)
currentMonth = todayDate.strftime("%b")
sigma = 6
mu = 0
weather = 0
time = 0
day = 1


timeInput = input("Enter a time of day:")

timeInput = int(timeInput)

time = timeInput

def monthly_temps():
    if currentMonth == 1:
        mu = -2
        return mu
    elif currentMonth == 2:
        mu = -1
        return mu
    elif currentMonth == 3:
        mu = 3
        return mu
    elif currentMonth == 4:
        mu = 9
        return mu
    elif currentMonth == 5:
        mu = 14
        return mu
    elif currentMonth == 6:
        mu = 17
        return mu
    elif currentMonth == 7:
        mu = 19
        return mu
    elif currentMonth == 8:
        mu = 18
        return mu
    elif currentMonth == 9:
        mu = 14
        return mu
    elif currentMonth == 10:
        mu = 9
        return mu
    elif currentMonth == 11:
        mu = 3
        return mu
    elif currentMonth == 12:
        mu = 0
        return mu


temp = round(random.gauss(mu, sigma))

while time > 1440:
    time = time - 1440
    day = day + 1
    todayDate = todayDate + datetime.timedelta(days=1)

if temp < 1:
    weather = tempList[0]
if temp >= 1 < 11:
    weather = tempList[1]
if temp >= 11 < 21:
    weather = tempList[2]
if temp >= 21 < 31:
    weather = tempList[3]
if temp >= 31:
    weather = tempList[4]


precipitation = random.choice(precList)

if temp < 0:
    snowChance = random.randint(1, 20)
    if snowChance < 11:
        precipitation = precList[0]


def snow_levels():
    global snowLevel
    snowLevel = 0
    if temp <= 0 and precipitation == precList[0]:
        snowLevel = snowLevel + 1
    elif temp > 0 and snowLevel > 0:
        snowLevel = - 1
    else:
        snowLevel = snowLevel = 0


snow_levels()

print(terrainList[currentLocation])
# print(monthList[currentMonth]) - cannot get this to work
print(monthList[])
print(temp, "degrees")



def tell_weather():
    print("The weather is currently", weather, "and", precipitation)
    print("Wind is", random.choice(windList))
    print("The snow level is ", snowDepth[snowLevel])


if time in range(90, 269):
    dayPart = 1
elif time in range(270, 449):
    dayPart = 2
elif time in range(450, 539):
    dayPart = 3
elif time in range(540, 629):
    dayPart = 4
elif time in range(630, 819):
    dayPart = 5
elif time in range(810, 989):
    dayPart = 6
elif time in range(990, 11699):
    dayPart = 7
elif time in range(1170, 1349):
    dayPart = 8
else:
    dayPart = 9

print("It is", timeList[dayPart])

convertedDay = str(day)

# print("It is " + dayPart + " of day " + convertedDay + ".")
print("Today's date is:", todayDate.strftime("%A"), todayDate.strftime("%B"), todayDate.strftime("%d"), ",", todayDate.strftime("%Y"))

tell_weather()


print(snowLevel)
