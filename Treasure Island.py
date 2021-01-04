'''print("""
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
""")'''
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
while 1:
    choice1=input("You are at a cross road. Where do you want to go? LEFT or RIGHT\nType 'L' for LEFT or 'R' for RIGHT:  ")
    choice1=choice1.upper()             # If user has entered choice1 in lower case, No worry. This statement will make it upper case
    if choice1=='R':
        print("You met with a road accident. You are dead. Game over.")
        break 

    elif choice1=='L':
        while 1:
            choice2=input('''\nYou came to a lake.here is an island in the middle of the lake. You wanna swim or wait for a boat? 
                            Type 'W' to wait for a boat. Type 'S' to swim across:  ''').upper()
            if choice2=='S':
                print("You are attacked by a big fish. You are dead. Game over.")
                break

        
            elif choice2=='W':
                while 1:
                    choice3=input('''\nYou arrive at the island unharmed. There is a house with 3 doors.One red, one yellow and one blue.
                                    Which door you wanna open? Type 'R' foe RED, 'Y' for YELLOW and 'B' for BLUE:  ''').upper()
                    if choice3=='R':
                        print("You got attacked by an angry trout.You are dead. Game Over.")
                        break
               
                    elif choice3=='Y':
                        print("You choosed a door that doesn't exist. Game over.")
                        break

                    elif choice3=='B':
                        print("You came across the treasure. You won.")
                        break

                    else:
                        print("Invalid choice!!")
                        continue
        
                break
            else:
                print("Invalid choice!!")
                continue
        break

    else:
        print("Invalid choice!!")
        continue


                