# Date Created: 3/10/20
# Date last modified: 3/12/20
# Name: Aydyn Baily
# Description: Dictionaries that contain locations, items, and stats


# Dictionary that contains locations in the game
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


# Nested dictionary that contains starting items and their stats
starting_items = {1: {'Shortsword': '3 ATK'},
                  2: {'Health Potion': '25 HP'},
                  3: {'Leather Armor': '2 DEF'}}

# Prints out the dictionary of starting items
for weapon, value in starting_items.items():
    print(value)
print("\n")

# Prints out a sentence describing the stats of each starting item
print(f"The shortsword has a base stat of {starting_items[1]['Shortsword']}")
print(f"Health potions heal {starting_items[2]['Health Potion']}")
print(f"Leather armor has a base stat of {starting_items[3]['Leather Armor']}")
