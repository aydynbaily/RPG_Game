# Dictionary of locations that are in the game
locations = {
    'floor 1': 'skeletons and goblins',
    'floor 2': 'orcs and knights',
    'floor 3': 'dragons and demons',
}

# Individual floors printed out
print("The game consists of three locations:")
for location in locations:
    print(location.title())
print("\n")

# Prints floors and the monsters that are in each floor
for floor, monsters in locations.items():
    print(f"{floor.title()} contains {monsters.title()}")
print("\n")


# Dictionary of main characters base stats
character = {
    'health': '100HP',
    'attack': '3 ATK',
    'defense': '3 DEF',
    'max carry': '5 items',
}

# Individual stat names printed out without values
print("The game has 4 main stats:")
for stats in character:
    print(stats.title())
print("\n")

# Prints stats along with their base values
for stat, value in character.items():
    print(f" Your {stat.title()} stat has a base value of {value.title()}")
print("\n")


# Dictionary that contains items found throughout the game
