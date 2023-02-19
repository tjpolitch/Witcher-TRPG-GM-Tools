x_coord = 2 #horizontal
y_coord = 2 #vertical

testMap = [[3, 1, 0, 0, 0],
           [3, 1, 1, 0, 0],
           [3, 1, 1, 0, 0],
           [3, 1, 2, 2, 2],
           [3, 1, 2, 2, 2]]

terrain_types = ["forest", "plains", "hills", "coast"]
current_terrain = 0
# direction = ["North", "North East", "East", " South East", "South", "South West", "West", "North West"]
direction = ""

def setLocation():
    global x_coord, y_coord, current_terrain
    current_terrain = testMap[x_coord][y_coord]


def goNorth():
    global y_coord, direction
    y_coord -= 1
    direction = "North"


def goNorthEast():
    global x_coord, y_coord, direction
    y_coord -= 1
    x_coord += 1
    direction = "North East"


def goEast():
    global x_coord, direction
    x_coord += 1
    direction = "East"


def goSouthEast():
    global x_coord, y_coord, direction
    y_coord += 1
    x_coord += 1
    direction = "South East"


def goSouth():
    global y_coord, direction
    y_coord += 1
    direction = "South"


def goSouthWest():
    global x_coord, y_coord, direction
    y_coord += 1
    x_coord -= 1
    direction = "South West"


def goWest():
    global x_coord, direction
    x_coord -= 1
    direction = "West"


def goNorthWest():
    global x_coord, y_coord, direction
    y_coord -= 1
    x_coord -= 1
    direction = "North West"


while True:

    print("-----N----------8-----")
    print("---NW-NE------7---9---")
    print("--W-----E----4-----6--")
    print("---SW-SE------1---3---")
    print("-----S----------2-----")

    choice = input("\nEnter choice:")
    choice = choice.strip()

    if choice == "8": # or "N":
        goNorth()
    elif choice == "7": # or "NW":
        goNorthWest()
    elif choice == "9": # or "NE":
        goNorthEast()
    elif choice == "4": # or "W":
        goWest()
    elif choice == "6": # or "E":
        goEast()
    elif choice == "1": # or "SW":
        goSouthWest()
    elif choice == "3": # or "SE":
        goSouthEast()
    elif choice == "2": # or "S":
        goSouth()
    else:
        print("That is not a valid selection. Please choose again.")

    setLocation()

    print(f"You travelled {direction}")
    print(f"Your current location is {x_coord}, {y_coord}.")
    print(f"Terrain: {terrain_types[current_terrain]}")