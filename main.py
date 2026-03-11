# snake water gun game

import random # to generate random number for computer

computer = random.choice([-1, 0, 1]) # randomly choose from -1, 0, 1 for computer

youstr = input("enter your choice: ") # take input from user, it can be "s", "w", "g" for snake, water, gun respectively

youDict = {"s": 1, "w": -1, "g": 0} # we can use a dictionary to map the user input to a number, for example, "s" for snake can be mapped to 1, "w" for water can be mapped to -1, and "g" for gun can be mapped to 0

reverseDict = {1: "snake", -1: "water", 0: "gun"} # we can also use a reverse dictionary to map the number back to the string for printing the result

you = youDict[youstr] 

# by now we have 2 numbers, computer and you

print(f"you choose {reverseDict[you]} and computer choose {reverseDict[computer]}")

if (computer == you):
    print("tie")

else:
    if(computer == 1 and you == -1):
        print("you lose")
    elif(computer == -1 and you == 0):
        print("you lose")
    elif(computer == 0 and you == 1):
        print("you lose")

    else:
        print("you win")