# 1 for snake
# -1 for water
# 0 for gun

import random as rd

computer = rd.choice([-1, 0, 1])
user = int(input("Enter 1 for snake, -1 for water, and 0 for gun: "))

userDict = {1: "snake", -1: "water", 0: "gun"}

if user not in userDict:
    print("Invalid input!")
else:
    print("Computer chose:", userDict[computer])
    print("User chose:", userDict[user])

    if computer == user:
        print("It's a tie!")
    elif (computer == -1 and user == 1) or \
        (computer == 1 and user == 0) or \
        (computer == 0 and user == -1):
        print("Computer wins!")
    else:
        print("User wins!")