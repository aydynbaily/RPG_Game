# Course: CS30
# Period: 4
# Date Created: 2/13/20
# Date last modified: 2/24/20
# Name: Aydyn Baily
# Description: Creates an RPG Inventory

# This list handles consumables
consumables = ['Shark', 'Health Potion', 'Cake', 'Apple', 'Defense Potion']
print(consumables)

# Adds an Attack potion to the inventory
consumables.append('Attack Potion')
print(consumables)

# Adds Bread to the inventory at position 1
consumables.insert(1, 'Bread')
print(consumables)

# Removes shark from the inventory
del consumables[0]
print(consumables)

# Pops bread from the list for later use
popped_consumable = consumables.pop(0)
# Prints new list
print(consumables)
# Prints the popped consumable
print(popped_consumable)

# Removes apple from the players Inventory
consumables.remove('Apple')
print(consumables)

# Sorts the list alphabetically
consumables.sort()
print(consumables)

# Temporarily sorts the list in reverse alphabetical order and prints it
print(sorted(consumables, reverse=True))
# Prints the list in alphabetical order, showing sorted() is temporary
print(consumables)

# Sorts the list in reverse
consumables.reverse()
print(consumables)

# Finds the length of the consumable list
print(len(consumables))


# This list handles weapons
weapons = ['Longsword', 'Shortsword', 'Bow', 'Dagger', 'Slingshot']
print(weapons)

# Adds a spear to the inventory
weapons.append('Spear')
print(weapons)

# Adds a mace to the inventory at position 0
weapons.insert(0, 'Mace')
print(weapons)

# Removes the shortsword from the players inventory
del weapons[2]
print(weapons)

# Pops the dagger from the players inventory and stores it for later use
popped_weapon = weapons.pop(3)
# Prints the new list
print(weapons)
# Prints the popped weapons
print(popped_weapon)

# Removes the slingshot from the players Inventory
weapons.remove('Slingshot')
print(weapons)

# Sorts the list of weapons alphabetically
weapons.sort()
print(weapons)

# Temporarily sorts the list in a reverse alphabetical order
print(sorted(weapons, reverse=True))
# Prints again to show that the sorting was temporary
print(weapons)

# Reverses the list, but permanently
weapons.reverse()
print(weapons)

# Finds the length of the list
print(len(weapons))


# Creates printed statements showing each inventory
# This statement is for consumables
print(f"You have 1 {consumables[0].title()}, 1 {consumables[1].title()}, "
      f"1 {consumables[2].title()}, and 1 {consumables[3].title()}.")

# This statement is for weapons
print(f"You have 1 {weapons[0].title()}, 1 {weapons[1].title()}, "
      f"1 {weapons[2].title()}, and 1 {weapons[3].title()}.")
