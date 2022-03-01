# ASCII Art for Treasure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("\n\nWelcome to the Treasure Island!\n")
print("Your mission is to find Treasure.")

if input("You're at a crossroad, where do you want to go? Type \"left\" or \"right\". ").lower() == 'left':
    if input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across. ").lower() == 'wait':
        if input("You arrive at the island unharmed. There is a house with 3 doors. One red, one blue and one yellow. Which color do you choose? ").lower() == "yellow":
            print("You found the Treasure, You Win!")
        else:
            print("You couldn't find right door, Game Over")
    else:
        print("You got attacked by an angry trout, Game Over")
else:
    print("You fell into a hole, Game Over!")
