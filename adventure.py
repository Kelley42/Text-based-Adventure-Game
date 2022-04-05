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
print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.\n") 

#defs
def beach():
    beach_response = input("What do you do? Run into the water, check out the bushes, or stay put?\n").lower()

    beach_answer1 = [
        "run into the water",
        "run",
        "water"
    ]
    beach_answer2 = [
        "check out the bushes",
        "check",
        "bushes"
    ]
    beach_answer3 = [
    "stay put",
    "stay",
    "put"
    ]
  
    if beach_response in beach_answer1:
        print("Oh, no! A very large sea monster has eaten you. That's too bad.\nGAME OVER")
        start_over()
        return 1
    elif beach_response in beach_answer2:
        see_shape()
    elif beach_response in beach_answer3:
        hungry()
    else:
        print("!!!Incorrect response - try again!!!")
        beach()

#Intro
print("     A storm has shipwrecked you and your crew on a tropical island. There are rumors that the island had a terrible curse put upon it long ago. Numerous treasure ships have mysteriously sunk along its coast, and the few who survived insisted that anyone who stepped foot on land was never seen again.\n     Night has fallen and you have woken up on the beach alone in the cold rain. You can't see or hear any of your crew members. Cold and wet, you can't stop shivering. Suddenly you hear rustling in the bushes behind you.\n")

beach()
