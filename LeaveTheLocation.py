locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             3: "You are at the top of the hill",
             4: "You are on the valley beside the stream",
             5: "yOu are in the forest"}
exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 5},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 1}}

vocabulary = {"quit": "Q",
              "north": "N",
              "south": "S",
              "east": "E",
              "west": "W",
              "ROAD": "1",
              "HILL": "2",
              "BUILDING": "3",
              "VALLEY": "4",
              "FOREST": "5"}
print(locations[0].split())
print(locations[3].split(","))
print(" ".join(locations[0].split()))
#lists require square brackets
#traditional dictionary look
loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    # for direction in exits[loc].keys():
    #     availableExits += direction + ", "

    print(locations[loc])

    if loc == 0:
        break

    directions = input("Available exits are " + availableExits + " ").upper()
    print()
    if len(directions) > 1:
        words = directions.split()
        for word in vocabulary:
            if word in directions:
                direction = vocabulary[word]
                break
    if directions in exits[loc]:
        loc = exits[loc][directions]
    else:
        print("You cannot go in the direction")
