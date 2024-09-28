# print('''*******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/[TomekK]
# *******************************************************************************''')
print("Welcome to Treasure Hunt")
print("your mission is to find the treasure")

choice1 = input('you\'re at cross road, where do you want to go? '
               'Type here "left" or "right"\n').lower()

if choice1 == "left":
    choice2 = input('you\'ve come to lake. There is an island in the middle of the lake. '
          'Type "wait" to wait for a boat. '
          'Type "swim" to swim across\n').lower()
    if choice2 == "wait":
        choice3 = input('you have reached the island  unharmed. '
                        'Now there is a house with 3 Doors. One RED, ONE Yellow, One Blue. '
                        'Which color do you want to Choose\n').lower()
        if choice3 == 'red':
            print("You are attacked by fire. GAME OVER")
        elif choice3 == 'yellow':
            print("You found the TREASURE. YOU WIN!!")
        elif choice3 == 'blue':
            print("You are attacked by water. GAME OVER")

else:
    print("you fell into the hole."
          " Game Over.")