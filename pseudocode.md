Use Code:
INPUT What item do you want to use
IF the item is in players Inventory
    USE the item
ELSE print "You do not have this item"
END Use Code


Movement Code:
INPUT "North, East, South, or West"
IF INPUT = North
    Move North

ELIF INPUT = East
    Move East

ELIF INPUT = South
    Move South

ELIF INPUT = West
    Move West

ELIF INPUT = West
    Move West

END Movement


Inventory Code:
START inventory
    PRINT inventory
END Inventory


Combat Code:
START Battle
PRINT "You are under attack! What will you choose to do?"

INPUT "Attack, Inventory, or Run"
IF INPUT=Attack
    Roll a random number determining the amount you hit for

ELIF INPUT=inventory
    PRINT inventory
END Inventory when an item is used

ELIF INPUT=Run
    Roll a random number determining if the escape is successful
END Combat if successful

ELIF Player Health < 0
    PRINT "You have died, will you try again?"
INPUT "Yes or No"
    IF INPUT = Yes
        Restart Game
ELIF INPUT = NO
    Close Game

END Combat


Item Interaction Code:
START Interaction
PRINT "You have found an item! What will you do?"

INPUT "Take item, leave item"
IF INPUT = Take item
    Item is added to Inventory

IF INPUT = Leave Item
    Item is left

END Interaction
