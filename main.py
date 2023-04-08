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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

first_choice = input("Please choose a path, left or right?: ")
first = first_choice.lower()

if first == "right":
  print("You have fallen into a hole GAME OVER")

elif first == "left":
  print("You enter the dark forest")
  print("You find yourself at the giant lake")

  second_choice = input("will you swim or wait?")
  second = second_choice.lower()

  if second == "swim":
    print("You drowned! GAME OVER!")

  elif second == "wait":
    print("You are taken by the red eagle and taken to the caste!")
    print("You enter the castle and see three doors, a blue, a red and a yellow.")

    third_choice = input("Please enter one of the three doors, red, blue, or yellow")
    third = third_choice.lower()

    if third == "red":
      print("You open the red door and a giant snake eats you! GAME OVER")

    elif third == "blue":
      print("You open the red door and are drowned in fish, GAME OVER")

    elif third == "yellow":
      print("You open the door and find a giant reasure chest. You open it...")
      print("It's full of gold coins, congratulations, YOU WIN!")
    else: 
      print("You didn't choose one of the three doors, another adventurer kills you and takes the treasures. GAME OVER!")
      
else: print("Your indecisiveness led to your demise an angry God curses you and you die. GAME OVER!")



  