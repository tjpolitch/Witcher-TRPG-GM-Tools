import random
import datetime
import calendar

tempList = ["freezing", "cold", "cool", "warm", "hot"] # can add 'mild' and other categories.
precList = ["snowing", "sleet", "raining", "drizzling", "foggy", "overcast", "cloudy", "clear"]
windList = ["light", "strong", "howling"]
timeList = ["midnight", "the small hours", "early morning", "late morning", "midday", "early afternoon",
            "late afternoon", "evening"]
terrainList = ["plains", "forest", "dark forest", "hills", "mountains", "high mountains", "lake", "river", "marshlands",
               "bog", "coast"]
seasonList = ["summer", "autumn", "winter", "spring"]
monthList = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
snowDepth = ["none", "light", "medium", "heavy"]
moonList = ["full moon", "waning gibbous", "last quarter", "waning crescent", "new moon", "waxing crescent",
            "first quarter", "waxing gibbous"]
listList = ["night", "sunrise", "day", "sunset"]
road = bool
choice = ""

todayMoon = 0 #random.randint(0, 7)
todayDate = datetime.datetime(1272, 5, 1)
dayPart = 0
currentLocation = random.randint(0, 9)
# currentMonth = random.randint(1, 12)
currentMonth = todayDate.strftime("%b")
sigma = 6
mu = 0
time = 0
day = 1
moonDay = 1
temp = 0
precipitation = 0
snowLevel = 0
weather = 0
choice = ""
today = 0
snowChance = 0


# Spence created this as an example of how a weather variables class can look
# class WeatherVariables:
#     def __init__(self, temp, precipitation, snowLevel):
#         self.temp = temp
#         self.precipitation = precipitation
#         self.snowLevel = snowLevel
#
#     def setSnowLevel(self, level):
#         self.temp -= level / 2
#         self.snowLevel = level



# Tells the phase of the moon based on a cycle of 28 days
def moon_phase():
    global todayMoon, moonDay
    # advances the moon cycle forward one day and resets at 28
    if moonDay <= 28:
        moonDay = moonDay + 1
    else:
        moonDay = 1

# tells the phase of the moon
    if moonDay == 1:
        todayMoon = 0
    elif moonDay in range(2, 7):
        todayMoon = 1
    elif moonDay == 8:
        todayMoon = 1
    elif moonDay in range(9, 14):
        todayMoon = 2
    elif moonDay == 15:
        todayMoon = 3
    elif moonDay in range(16, 21):
        todayMoon = 4
    elif moonDay == 15:
        todayMoon = 5
    elif moonDay in range(23, 28):
        todayMoon = 6
    elif moonDay == 22:
        todayMoon = 7

# row is month and day part starts at midnight. including temps based on the 15th of each month on Warsaw
temperaturesModifiers = {
    0: [-2, -3, -5, -1, 1, 1, 0, -1],
    1: [-2, -3, -5, -1, 1, 1, 2, 0],
    2: [1, 0, -1, 3, 4, 5, 7, 2],
    3: [5, 4, 3, 8, 9, 11, 12, 14],
    4: [13, 11, 8, 15, 16, 17, 18, 20],
    5: [13, 11, 16, 17, 18, 19, 20, 22],
    6: [16, 13, 16, 18, 20, 21, 23, 24],
    7: [17, 15, 13, 17, 20, 21, 23, 24],
    8: [11, 9, 8, 13, 15, 17, 19, 13],
    9: [6, 5, 4, 8, 9, 11, 13, 10],
    10: [2, 1, 0, 3, 4, 5, 6, 2],
    11: [-2, -3, -4, 0, 1, 2, 0, -1]
}

# Day Part/ Time Key
#        midnight: 10:30PM - 1:30AM
#     small hours: 1:30AM - 4:30 AM
#   early morning: 4:30AM - 7:30 AM
#    late morning: 7:30AM - 10:30AM
#          midday: 10:30AM - 1:30PM
# early afternoon: 1:30PM - 4:30PM
#  late afternoon: 4:30PM - 7:30PM
#         evening: 7:30PM - 10:30PM

# sunset and sunrise for each month; 0 = night, 1 = sunrise; 2 = day, 3 = sunset: might actually replace this with a spreadsheet of sunrise/sunset times https://www.timeanddate.com/sun/poland/warsaw?month=1&year=2023
lightModifiers = {
    0: [0, 0, 0, 1, 2, 3, 0, 0],
    1: [0, 0, 1, 2, 2, 2, 3, 0],
    2: [0, 0, 1, 2, 2, 2, 3, 0],
    3: [0, 0, 1, 2, 2, 2, 2, 3],
    4: [0, 0, 1, 2, 2, 2, 2, 3],
    5: [0, 1, 2, 2, 2, 2, 2, 3],
    6: [0, 1, 2, 2, 2, 2, 2, 3],
    7: [0, 0, 1, 2, 2, 2, 2, 3],
    8: [0, 0, 1, 2, 2, 2, 3, 0],
    9: [0, 0, 1, 2, 2, 2, 3, 0],
    10: [0, 0, 1, 2, 2, 3, 0, 0],
    11: [0, 0, 0, 1, 2, 3, 0, 0]
}


# Function for providing am average temp for each month - based on average temps in Warsaw
def monthly_temps(dayPart):

    # this is equivalent of what you have below
    mu = temperaturesModifiers[currentMonth][dayPart]

    print(currentMonth)
    print(dayPart)
    print(mu)

    return mu


# Provide a weather description based on the temperature
def tell_weather():
    global weather, temp
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
    return weather, temp


# Function that determines whether it is snowing based on whether the temp is freezing (below 0) and then giving it a 50/50 chance
# A boolean should probably be added in here
def snowing():
    global temp, precipitation, snowChance
    if temp < 0:
        snowChance = random.randint(1, 2)
        if snowChance == 1:
            precipitation = precList[0]
    return precipitation


# Function to create a persistent level of snow which rises if it snows and recedes if it doesn't - the persistnce is not included yet
def snow_levels():
    global snowLevel
    if temp <= 0 and precipitation == precList[0]:
        snowLevel = snowLevel + 1
    elif temp > 0 and snowLevel > 0:
        snowLevel = - 1
    else:
        snowLevel = snowLevel = 0
    return snowLevel


# Function to convert the time of the day (in minutes) into a part of a day e.g. midday.
def convert_time_to_daypart():
    global dayPart
    if time in range(90, 269):
        dayPart = 1
    elif time in range(270, 449):
        dayPart = 2
    elif time in range(450, 629):
        dayPart = 3
    elif time in range(630, 809):
        dayPart = 4
    elif time in range(810, 989):
        dayPart = 5
    elif time in range(990, 1169):
        dayPart = 6
    elif time in range(1170, 1349):
        dayPart = 7
    else:
        dayPart = 0


# Convert the datetime month to an integer that corresponds with the monthList
def convert_month():
    global currentMonth
    if todayDate.strftime("%B") == "January":
        currentMonth = 0
    elif todayDate.strftime("%B") == "February":
        currentMonth = 1
    elif todayDate.strftime("%B") == "March":
        currentMonth = 2
    elif todayDate.strftime("%B") == "April":
        currentMonth = 3
    elif todayDate.strftime("%B") == "May":
        currentMonth = 4
    elif todayDate.strftime("%B") == "June":
        currentMonth = 5
    elif todayDate.strftime("%B") == "July":
        currentMonth = 6
    elif todayDate.strftime("%B") == "August":
        currentMonth = 7
    elif todayDate.strftime("%B") == "September":
        currentMonth = 8
    elif todayDate.strftime("%B") == "October":
        currentMonth = 9
    elif todayDate.strftime("%B") == "November":
        currentMonth = 10
    elif todayDate.strftime("%B") == "December":
        currentMonth = 11
    return currentMonth


# Moves time forward
def forward_time():
    # Iterates the day counter based on the number of minutes inputted by user
    global time, day, todayDate
    while time > 1440:
        time = time - 1440
        day = day + 1
        todayDate = todayDate + datetime.timedelta(days=1)


def generate_weather():
    global temp, precipitation, day, todayDate, time
    forward_time()
    convert_time_to_daypart()
    convert_month()
    mu = monthly_temps(dayPart)
    # Provides a semi-random temperature based on the monthly average on a gaussian curve
    precipitation = random.choice(precList)
    temp = round(random.gauss(mu, sigma))
    tell_weather()
    snowing()
    snow_levels()
    moon_phase()
    # convertedDay = str(day) - not working for now
    # print(monthList[currentMonth]) - cannot get this to work


# Takes user input for the time of day (in minutes) and turns into an integer - this is here for testing purposes
timeInput = input("Enter a time of day:")
timeInput = int(timeInput)
time = timeInput

# Loop to create a menu. This is not final and some options are just for testing at the moment.
while True:
    generate_weather()

    print("1) Tell date")
    print("2) Tell time (day part + month)")
    print("3) Look at moon")
    print("4) Tell weather")
    print("5) Tell snow levels (number and description)")
    print("6) Tell wind")
    print("7) Tell terrain")
    print("8) Regenerate weather")
    print("9) Regenerate time")
    print("10) Quit")

    choice = input("Enter choice:")
    choice = choice.strip()

    if choice == "1":
        print("Today's date is:", todayDate.strftime("%A"), todayDate.strftime("%B"), todayDate.strftime("%d"), ",",
              todayDate.strftime("%Y"))
    elif choice == "2":
        print("It is", timeList[dayPart])
        print(monthList[currentMonth])
    elif choice == "3":
        moon_phase()
        print(moonList[todayMoon])
    elif choice == "4":
        print(temp, "degrees")
        print(f"The weather is currently {weather} and {precipitation}")
    elif choice == "5":
        print("The snow level is ", snowDepth[snowLevel])
        print(snowLevel)
    elif choice == "6":
        print(f"Wind is {random.choice(windList)}")  # test f-string function - I will adjust more later
    elif choice == "7":
        print(terrainList[currentLocation])
    elif choice == "8":
        generate_weather()
    elif choice == "9":

        while True:
            print("1) Regenerate time")
            print("2) Step forward time 3 hours")
            print("3) Step forward time 1 day")
            print("4) Step forward time 1 week")
            print("5) Go back to Main Menu")
            choice = input("Enter choice:")
            choice = choice.strip()
            if choice == "1":
                timeInput = input("Enter a time of day:")
                timeInput = int(timeInput)
                time = time + timeInput
                generate_weather()
                print("It is now", timeList[dayPart])
                print("Today's date is:", todayDate.strftime("%A"), todayDate.strftime("%B"), todayDate.strftime("%d"),
                      ",",
                      todayDate.strftime("%Y"))
            elif choice == "2":
                time = time + 180
                generate_weather()
                print("It is now", timeList[dayPart])
                print("Today's date is:", todayDate.strftime("%A"), todayDate.strftime("%B"), todayDate.strftime("%d"),
                      ",",
                      todayDate.strftime("%Y"))
            elif choice == "3":
                time = time + 1440
                generate_weather()
                print("It is now", timeList[dayPart])
                print("Today's date is:", todayDate.strftime("%A"), todayDate.strftime("%B"), todayDate.strftime("%d"),
                      ",",
                      todayDate.strftime("%Y"))
            elif choice == "4":
                time = time + 10080
                generate_weather()
                print("It is now", timeList[dayPart])
                print("Today's date is:", todayDate.strftime("%A"), todayDate.strftime("%B"), todayDate.strftime("%d"),
                      ",",
                      todayDate.strftime("%Y"))
            elif choice == "5":
                break
            else:
                print("Invalid option. Please try again.")

    elif choice == "10" or "q":
        break
    else:
        print("Invalid option. Please try again.")
